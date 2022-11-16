from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    creates custom user model from default user.

    Attribs:
        phone_number (int): phone number of the user.
        name (char): full name of the user.
        dob(date): Date of birth of user.
        profile_image (img): user image.
        monthly_budget (int): monthly budget limit of the user.

    Inherited Attribs:
        password(char): Password of the user.
        is_staff(bool): field which shows the staff status of user..

    """
    phone_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    dob = models.DateField(null=True, default=None)
    profile_image = models.ImageField(
        upload_to='profile_images/', null=True, blank=True, default='')
    monthly_budget = models.IntegerField(blank=True, null=True, default=0)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'password']

    class Meta:
        """Meta class for the above model."""
        
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """string representation of user name."""
        return self.name

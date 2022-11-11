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
    """
    phone_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    dob = models.DateTimeField(null=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # is_staff = models.BooleanField(_('staff'), default=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    profile_image = models.ImageField(
        upload_to='profile_images/', null=True, blank=True)
    monthly_budget = models.IntegerField(blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.name
    
    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     '''
    #     Returns the short name for the user.
    #     '''
    #     return self.first_name

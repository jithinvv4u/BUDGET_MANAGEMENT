from django.db import models
from v1.accounts.models import User
# Create your models here.


class Account(models.Model):
    """
    Model to store account informations.
    Account is created with a specific user that availabe in User model.

    Attributes:
        account_name(char)          : Name of account.
        account_inintial_amt(float)          :inintial amount in account, default is zero.
        account_type(char)   : Type of account(3 choices).

    Inherited Attribs:
        user(obj): user object to represent account holder.
    """
    
    ACCOUNT_CHOICES = (
        ('Saving', 'Saving'),
        ('Investment', 'Investment'),
        ('FD', 'FD'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=30)
    account_inintial_amt = models.FloatField(null=True, blank=True, default=0)
    account_type = models.CharField(
        max_length=30, choices=ACCOUNT_CHOICES, default='Saving')

    def __str__(self):
        return self.account_type


class Income(models.Model):
    """
    Model to store Income Details.
    Income is created with a specific user that availabe in User model with type of
    account that avaliable in Account model.

    Attributes:
        income_date(date)          : Date which income amount credited.
        income_category(char)      : Type of income category(4 choices).
        income_amount(float)       : Income amount(default 0).
        income_note(text)          : Add a short note on income.

    Inherited Attribs:
        user(obj): user object to assign income to user.
        account_type(char)   : Type of account(3 choices) inherited from model Account.
        
    """
    
    INCOME_CHOICE = (
        ('Salary', 'Salary'),
        ('Gift', 'Gift'),
        ('Interest', 'Interest'),
        ('Returns', 'Returns'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(
        Account, on_delete=models.CASCADE, choices=Account.ACCOUNT_CHOICES)
    income_date = models.DateField(default=None)
    income_category = models.CharField(
        max_length=30, choices=INCOME_CHOICE, default='Salary')
    income_amount = models.FloatField(default=0)
    income_note = models.TextField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.account_type

    # def __str__(self):
    #     return self.account_type,self.user_id.name


class Expense(models.Model):
    """
    Model to store Expense Details.
    Income is created with a specific user that availabe in User model with type of
    account that avaliable in Account model.

    Attributes:
        expense_date(date)          : Date which expense amount debited.
        expense_category(char)      : Type of expense category(6 choices).
        expense_amount(float)       : Expense amount(default 0).
        expense_note(text)          : Add a short note on Expense.

    Inherited Attribs:
        user(obj): user object to assign income to user.
        account_type(char)   : Type of account(3 choices) inherited from model Account.
        
    """
    
    EXPENSE_CHOICE = (
        ('Travel', 'Travel'),
        ('Entertainment', 'Entertainment'),
        ('Vehicle', 'Vehicle'),
        ('Shopping', 'Shopping'),
        ('Food', 'Food'),
        ('Investment', 'Investment'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(
        Account, on_delete=models.CASCADE, choices=Account.ACCOUNT_CHOICES)
    expense_date = models.DateField(default=None)
    expense_category = models.CharField(
        max_length=30, choices=EXPENSE_CHOICE, default='Salary')
    expense_amount = models.FloatField(default=0)
    expense_note = models.TextField(max_length=80, null=True, blank=True)

    # def __str__(self):
    #     return self.account_type,self.user_id.name

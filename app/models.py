from django.db import models
from accounts.models import User
# Create your models here.


class Account(models.Model):
    ACCOUNT_CHOICES = (
        ('Saving', 'Saving'),
        ('Investment', 'Investment'),
        ('FD', 'FD'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=30)
    account_inintial_amt = models.FloatField()
    account_type = models.CharField(
        max_length=30, choices=ACCOUNT_CHOICES, default='Saving')

    def __str__(self):
        return self.account_type

    def balance_amount():
        pass

class Income(models.Model):
    INCOME_CHOICE = (
        ('Salary', 'Salary'),
        ('Gift', 'Gift'),
        ('Interest', 'Interest'),
        ('Returns', 'Returns'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(
        Account, on_delete=models.CASCADE, choices=Account.ACCOUNT_CHOICES)
    income_date = models.DateField()
    income_category = models.CharField(
        max_length=30, choices=INCOME_CHOICE, default='Salary')
    income_amount = models.FloatField()
    income_note = models.TextField(max_length=80)

    def __str__(self):
        return self.account_type

    # def __str__(self):
    #     return self.account_type,self.user_id.name


class Expense(models.Model):
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
    expense_date = models.DateField()
    expense_category = models.CharField(
        max_length=30, choices=EXPENSE_CHOICE, default='Salary')
    expense_amount = models.FloatField()
    expense_note = models.TextField(max_length=80)

    # def __str__(self):
    #     return self.account_type,self.user_id.name
    

# today=datetime.date.today()
# total=Income.objects.aggregate(Sum('income_amount'))
# Income.objects.filter(income_date__year=today.year,income_date__month=today.month).values('income_category').annotate(Sum('income_amount'),percent=F('income_amount__sum') / total['income_amount__sum'] * 100 )


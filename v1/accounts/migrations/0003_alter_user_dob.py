# Generated by Django 4.1.3 on 2022-11-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=None, null=True),
        ),
    ]

# Generated by Django 4.0 on 2021-12-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0005_rename_loan_time_loaner_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='loan_status',
        ),
    ]
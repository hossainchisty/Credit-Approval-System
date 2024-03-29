# Generated by Django 5.0.1 on 2024-02-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_loan_interest_rate_alter_loan_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='tenure',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

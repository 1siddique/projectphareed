# Generated by Django 4.2.5 on 2023-10-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTHREE_RI', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Message',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='user',
            name='Message',
            field=models.TextField(max_length=80),
        ),
    ]

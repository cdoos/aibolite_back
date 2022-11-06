# Generated by Django 4.1.3 on 2022-11-06 14:15

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('iin', models.CharField(blank=True, max_length=12, verbose_name='IIN')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='middle name')),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=12, region=None)),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

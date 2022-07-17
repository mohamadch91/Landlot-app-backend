# Generated by Django 4.0.6 on 2022-07-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Tenant', 'Tenant'), ('Landlord', 'Lanlord'), ('Agency', 'Agency')], db_column='RoleName', max_length=10, null=True),
        ),
    ]

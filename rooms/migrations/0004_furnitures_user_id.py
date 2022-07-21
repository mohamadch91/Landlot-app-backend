# Generated by Django 4.0.6 on 2022-07-21 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_furnitures_is_default_furnituresinrooms_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnitures',
            name='user_id',
            field=models.ForeignKey(blank=True, db_column='userId', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

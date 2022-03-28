# Generated by Django 3.2.12 on 2022-03-16 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0007_remove_petphoto_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.petstagramusermodel'),
            preserve_default=False,
        ),
    ]
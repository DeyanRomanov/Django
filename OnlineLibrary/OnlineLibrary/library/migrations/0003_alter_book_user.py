# Generated by Django 3.2.12 on 2022-02-25 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20220225_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='library.profile'),
        ),
    ]

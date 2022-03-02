# Generated by Django 3.2.12 on 2022-03-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('name', 'artist')},
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
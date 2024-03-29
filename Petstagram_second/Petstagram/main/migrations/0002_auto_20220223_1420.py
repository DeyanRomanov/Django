# Generated by Django 3.2.12 on 2022-02-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petsphoto',
            options={'ordering': ('likes', 'date_and_time_of_publication')},
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(default='https://www.freepik.com/free-photo/blue-morning-natural-mountains-bamboo_1171002.htm#query=free%20pic&position=2&from_view=keyword'),
            preserve_default=False,
        ),
    ]

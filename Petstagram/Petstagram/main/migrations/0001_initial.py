# Generated by Django 3.2.12 on 2022-02-22 19:55

import Petstagram.main.validators_custom
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Petstagram.main.validators_custom.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Petstagram.main.validators_custom.validate_only_letters])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PetsPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[Petstagram.main.validators_custom.ValidatePhotoMaxSizeMb(5)])),
                ('description', models.TextField(blank=True, null=True)),
                ('date_and_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user_profile', 'name')},
        ),
    ]
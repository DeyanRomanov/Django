import os
from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from Petstagram.accounts.models import Profile
from Petstagram.main_app.models import PetPhoto


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        MIN_BIRTH_DATE = '1920-01-01'
        MAX_BIRTH_DATE = datetime.now()
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'min': MIN_BIRTH_DATE,
                    'max': MAX_BIRTH_DATE,
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            pets = self.instance.pet_set.all()
            photos = PetPhoto.objects.filter(tagged_pets__in=pets).all()
            for photo in photos:
                os.remove(photo.photo.path)
                photo.delete()
            self.instance.delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()

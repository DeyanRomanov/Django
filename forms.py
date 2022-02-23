from django import forms
from django.forms import ModelForm

from Petstagram.main.models import Profile, Pet


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'profile_picture',
        )

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


class CreatePet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'name',
            'type',
            'date_of_birth',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.ChoiceField(
                attrs={
                    'class': 'form-control',
                }
            ),
            # 'date_of_birth': forms.ChoiceField(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # ),
        }

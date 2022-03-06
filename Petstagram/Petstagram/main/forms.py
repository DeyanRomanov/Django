import datetime

from django import forms

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


class EditProfile(forms.ModelForm):
    class Meta:

        END_YEAR = datetime.date.today().year
        START_YEAR = 1920

        YEARS = [i for i in range(END_YEAR, START_YEAR, -1)]

        model = Profile
        fields = (
            'first_name',
            'last_name',
            'profile_picture',
            'date_of_birth',
            'email',
            'gender',
            'description',
        )

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'date_of_birth': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control'
                },
                years=YEARS,
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                },
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                },
            ),
        }


class CreatePet(forms.ModelForm):
    class Meta:
        start_year = 1920
        end_year = datetime.date.today().year

        YEARS = [i for i in range(start_year, end_year + 1)]

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
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS,
                attrs={
                    'class': 'form-control',
                }
            ),
        }

from django import forms

from musciapp.main.models import Profile, Album


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }

    def _clean_form(self):
        pass


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'genre': forms.Select(),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbum(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
        }

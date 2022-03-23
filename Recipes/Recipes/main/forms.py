from django import forms
from django.core.exceptions import ValidationError

from Recipes.main.models import Recipe


class CreateRecipe(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    def clean_bot_catcher(self):
        value = self.changed_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Recipe
        fields = '__all__'


class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipe(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'readonly': 'readonly',
                },
            ),
            'ingredients': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
            'time': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
        }

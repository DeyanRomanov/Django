import os

from django import forms

from djangoProject1.web.models import Profile, Expense


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget',
                  'first_name',
                  'last_name',
                  'profile_image',
                  )


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget',
                  'first_name',
                  'last_name',
                  'profile_image',
                  )


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            if Profile.objects.all()[0].profile_image:
                profile_image = self.instance.profile_image.path
                os.remove(profile_image)
            self.instance.delete()
            Expense.objects.all().delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price',
                  )


class EditExpense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price',
                  )


class DeleteExpense(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price',
                  )
        # widgets = {}
        # for field in fields:
        #     widgets[field] = forms.TextInput(attrs={'readonly': 'readonly'})

from django import forms

from Petstagram.main_app.models import Pet, PetPhoto


class AddPetForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AddPetForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user_profile = self.user
        if commit:
            pet.save()
        return pet

    # def clean_date_of_birth(self):
    #     birthday = self.cleaned_data['date_of_birth']
    #     age = int((date.today() - birthday).days / 365)
    #     return age

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
                    'placeholder': 'Enter pet name'
                }
            ),
        }


class EditPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class DeletePetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeletePetForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'readonly': 'readonly'})

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instace

    class Meta:
        model = Pet
        fields = '__all__'


class AddPhotoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AddPhotoForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = PetPhoto
        fields = (
            'photo',
            'description',
            'tagged_pets',
        )

        # widgets = {
        #     'photo': forms.ImageField(
        #     ),
        #     'description': forms.Textarea(
        #         attrs={
        #             'rows': 3,
        #             'placeholder': 'Enter description',
        #         }
        #     ),
        #     'tagged_pets': forms.SelectMultiple(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        # }


class EditPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPhotoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = PetPhoto
        fields = (
            'photo',
            'description',
            'tagged_pets',
        )

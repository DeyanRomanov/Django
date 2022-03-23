from django.contrib import admin

from Petstagram.main.models import Profile, Pet, PetsPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (
        PetInlineAdmin,
    )


@admin.register(PetsPhoto)
class PetsPhotoAdmin(admin.ModelAdmin):
    pass

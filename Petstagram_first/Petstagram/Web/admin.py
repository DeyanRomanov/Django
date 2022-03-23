from django.contrib import admin

from Petstagram.Web.models import Profile, Pet, PetsPhoto


class PetAdminInline(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'picture',
        'date_of_birth',
        'description',
        'email',
        'gender',
    )
    inlines = [
        PetAdminInline,
    ]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'types',
    )


@admin.register(PetsPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'likes',

    )

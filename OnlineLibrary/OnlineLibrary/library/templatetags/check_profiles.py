from django import template

from OnlineLibrary.library.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]

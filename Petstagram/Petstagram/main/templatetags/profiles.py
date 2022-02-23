from django import template

from Petstagram.main.models import Profile

register = template.Library()


@register.simple_tag
def has_profile():
    profile = Profile.objects.count()
    if profile > 0:
        return True
    # hardcore have profile

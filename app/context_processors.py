from . import models

def sidebar(request):
    top_tags = models.Tag.objects.get_top()
    top_profiles = models.Profile.objects.get_top_by_rating()

    return {'top_tags': top_tags,
            'top_users': top_profiles}

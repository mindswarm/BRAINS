def media_url(request):
    from django.conf import settings
    return {'static_url': settings.STATIC_URL}

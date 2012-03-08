# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    context = {}
    return render_to_response('main/index.html',
                              context,
                              context_instance=RequestContext(request))


def cohorts(request):
    context = {}
    return render_to_response('main/cohorts.html',
                              context,
                              context_instance=RequestContext(request))


def about_founders(request):
    context = {}
    return render_to_response('main/about_founders.html',
                              context,
                              context_instance=RequestContext(request))


def about_collaborators(request):
    context = {}
    return render_to_response('main/about_collaborators.html',
                              context,
                              context_instance=RequestContext(request))


def about_security(request):
    context = {}
    return render_to_response('main/about_security.html',
                              context,
                              context_instance=RequestContext(request))


def about_privacy(request):
    context = {}
    return render_to_response('main/about_privacy.html',
                              context,
                              context_instance=RequestContext(request))


def about_mission(request):
    context = {}
    return render_to_response('main/about_mission.html',
                              context,
                              context_instance=RequestContext(request))


def about_faq(request):
    context = {}
    return render_to_response('main/about_faq.html',
                              context,
                              context_instance=RequestContext(request))


def media_videos(request):
    context = {}
    return render_to_response('main/media_videos.html',
                              context,
                              context_instance=RequestContext(request))


def media_slides(request):
    context = {}
    return render_to_response('main/media_slides.html',
                              context,
                              context_instance=RequestContext(request))


def media_documents(request):
    context = {}
    return render_to_response('main/media_documents.html',
                              context,
                              context_instance=RequestContext(request))


def news(request):
    context = {}
    return render_to_response('main/news.html',
                              context,
                              context_instance=RequestContext(request))


def volunteer(request):
    context = {}
    return render_to_response('main/volunteer.html',
                              context,
                              context_instance=RequestContext(request))

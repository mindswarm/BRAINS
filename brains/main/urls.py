from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    url(r'^$',
        'brains.main.views.index',
        name='root_index'),

    url(r'^index.html$', redirect_to, {'url': '/'}),

    url(r'^cohorts$',
        'brains.main.views.cohorts',
        name='root_cohorts'),

    url(r'^cohorts/$', redirect_to, {'url': '/cohorts'}),

    url(r'^about/founders$',
        'brains.main.views.about_founders',
        name='about_founders'),

    url(r'^about$', redirect_to, {'url': '/about/founders'}),

    url(r'^about/$', redirect_to, {'url': '/about/founders'}),

    url(r'^about/founders/$', redirect_to, {'url': '/about/founders'}),

    url(r'^about/collaborators$',
        'brains.main.views.about_collaborators',
        name='about_collaborators'),

    url(r'^about/collaborators/$', redirect_to, {'url': '/about/collaborators'}),

    url(r'^about/security$',
        'brains.main.views.about_security',
        name='about_security'),

    url(r'^about/security/$', redirect_to, {'url': '/about/security'}),

    url(r'^about/privacy$',
        'brains.main.views.about_privacy',
        name='about_privacy'),

    url(r'^about/privacy/$', redirect_to, {'url': '/about/privacy'}),

    url(r'^about/mission$',
        'brains.main.views.about_mission',
        name='about_mission'),

    url(r'^about/mission/$', redirect_to, {'url': '/about/mission'}),

    url(r'^about/faq$',
        'brains.main.views.about_faq',
        name='about_faq'),

    url(r'^about/faq/$', redirect_to, {'url': '/about/faq'}),

    url(r'^media/videos$',
        'brains.main.views.media_videos',
        name='media_videos'),

    url(r'^media/videos/$', redirect_to, {'url': '/media/videos'}),

    url(r'^media/slides$',
        'brains.main.views.media_slides',
        name='media_slides'),

    url(r'^media/slides/$', redirect_to, {'url': '/media/slides'}),

    url(r'^media/documents$',
        'brains.main.views.media_documents',
        name='media_documents'),

    url(r'^media/documents/$', redirect_to, {'url': '/media/documents'}),

    url(r'^news$',
        'brains.main.views.news',
        name='root_news'),

    url(r'^news/$', redirect_to, {'url': '/news'}),

    url(r'^volunteer$',
        'brains.main.views.volunteer',
        name='root_volunteer'),

    url(r'^volunteer/$', redirect_to, {'url': '/volunteer'}),

)

from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'the_blog'
urlpatterns = [
    # Landing Page
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^about/$', views.about, name='about'),
    re_path(r'^post/(?P<entry_id>\d+)/$', views.post, name='post'),
    re_path(r'^comment/(?P<entry_id>\d+)/$', views.comment, name='comment'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




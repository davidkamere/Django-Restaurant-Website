from django.urls import path, re_path, include
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
    path('logout', views.logout_request, name='logout'),
    path('', include("django.contrib.auth.urls")),
    re_path(r'^post/(?P<entry_id>\d+)/$', views.post, name='post'),
    re_path(r'^comment/(?P<entry_id>\d+)/$', views.comment, name='comment'),
    url(r'^download/(?P<entry_id>\d+)/$', views.render_pdf, name='pdf'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('new/', views.post_view, name='create'),
    re_path(r'^delete/(?P<entry_id>\d+)/$', views.delete, name='delete'), 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




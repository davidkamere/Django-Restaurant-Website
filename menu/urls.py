from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'the_menu'
urlpatterns = [
    # Landing Page
    url(r'^gallery/$', views.menu, name='menu'),
    ]




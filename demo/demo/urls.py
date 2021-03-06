"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basic/$','demo1.views.last_fm'),
    url(r'^game/$','demo1.views.game'),
    url(r'^auth_view/$','demo1.views.auth_view'),
    url(r'^logout/$','demo1.views.logout'),
    url(r'^history/$','demo1.views.history'),
    url(r'^$','demo1.views.home'),
    url(r'^get/(?P<artist_id>\w+)/$','demo1.views.repeat')	
   		
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

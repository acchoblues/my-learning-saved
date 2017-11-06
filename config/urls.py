import allauth
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    # admin pages
    url(r'^mls-admin/', include(admin.site.urls)),

    # Authentication
    url(r'^accounts/', include('allauth.urls')),

]

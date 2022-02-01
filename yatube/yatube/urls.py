"""yatube URL Configuration"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('posts.urls', namespace='post')),
    path('admin/', admin.site.urls),
]

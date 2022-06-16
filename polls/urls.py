from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import polls_view, like_poll

app_name = 'polls'
urlpatterns = [
    path('', polls_view, name='poll-list'),
    path("like/", like_poll, name="like-poll")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

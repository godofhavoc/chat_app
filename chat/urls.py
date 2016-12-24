from django.conf.urls import url, include
from chat import views

urlpatterns = [
    url(r'^$', views.chat_room, name='chat_room'),
]

from django.urls import path
from .views import *

urlpatterns = [
    # path('', RoomsList.as_view()),
    path('', MessagesList.as_view()),
]

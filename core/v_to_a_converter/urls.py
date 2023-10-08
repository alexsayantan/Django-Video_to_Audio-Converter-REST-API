from django.urls import path
from .views import UserView, MediaView


urlpatterns = [
    path('user/', UserView.as_view()),
    path('upload-media/', MediaView.as_view())
] 
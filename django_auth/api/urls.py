from django.conf.urls import url
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
from api import views

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^obtain_token/$', views.authenticate_user),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
]
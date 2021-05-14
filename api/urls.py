from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from api import views
from api.views import TemplatesView, UploadView, InformationView, DisplayView, GetPPTView, LoginView

route = routers.DefaultRouter()

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^templates$', TemplatesView.as_view()),
    url(r'^upload$', UploadView.as_view()),
    url(r'^information$', InformationView.as_view()),
    url(r'^display$', DisplayView.as_view()),
    url(r'^getPPT$', GetPPTView.as_view()),
]

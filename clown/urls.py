from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import AppointmentView, AppointmentDetailView, AppointmentViewSet

app_name = 'clown'
router = routers.DefaultRouter()
router.register(r'appointment', AppointmentViewSet)
urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'^api-auth/$', obtain_auth_token, name='api-token-auth'),
    url(r'^appointment/$', AppointmentView.as_view(), name='appointment'),
    url(r'^appointment/detail/$', AppointmentDetailView.as_view(), name='appointmen-detail'),

]

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.photo_category,name='photoCategory'),
    url(r'^about/',views.about,name='about'),
    url(r'^contact/',views.contact,name='contact'),


   
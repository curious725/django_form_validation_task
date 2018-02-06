from django.conf.urls import url
from . import views

app_name = 'contacts'
urlpatterns = [
    # ex: /contacts
    url(r'^$', views.index, name='index'),
]
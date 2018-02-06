from django.conf.urls import url
from . import views

app_name = 'contacts'
urlpatterns = [
    # ex: /contacts
    url(r'^$', views.index, name='index'),
    # ex: /contacts/new
    url(r'^new/$', views.new_contact, name='new_contact'),
]
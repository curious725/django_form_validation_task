from django.conf.urls import url

app_name = 'contacts'
urlpatterns = [
    # ex: /contacts
    url(r'^$', views.index, name='index'),
]
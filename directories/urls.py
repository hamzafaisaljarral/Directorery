from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, SearchResultsView,Profile,SearchResultsViewSubject

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)$',views.Profile,name='Profile'),
    url(r'^import/$', views.simple_upload, name='import'),
    url(r'^search/', SearchResultsView.as_view(), name='search_results'),
    url(r'^subject/', SearchResultsViewSubject.as_view(), name='search_subject'),
    url('', HomePageView.as_view(), name='home'),
    

    ]

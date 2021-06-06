from django.conf.urls import url                                                                                                                              
from . import views
from django.urls import path
from trip.views import FoliumView

app_name = "trip"
urlpatterns = [ 
    url(r'', views.default_map, name="default"),
    path('', views.FoliumView.as_view(), name="default"),
                  
    ]
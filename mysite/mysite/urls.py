
from django.contrib import admin
from django.urls import include, path
from main import views
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.SubscriberEmail),
    path('trip/', include('trip.urls')),
    path('timetable/', include('timetable.urls')),
   
    
    #path('', FoliumView.as_view(template_name="default.html"), name="default"),
]

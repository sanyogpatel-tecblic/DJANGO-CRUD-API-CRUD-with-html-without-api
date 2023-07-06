
from django.contrib import admin
from django.urls import path,re_path
from task_app import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('region',views.GetRegion,name='region'),
    path('state/',views.GetState,name='state'),
    path('zone/',views.GetZone,name='zone'),
    path('district/',views.GetDistrict,name='district'),
]


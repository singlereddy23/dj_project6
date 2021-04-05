from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('',views.index,name="index"),
    path('sample/',views.sample,name="sample"),
    path("sample_app1/",views.sample_view,name="sample_view"),
]

from django.urls import path
from app1 import views
app_name="app2"

urlpatterns = [
    path('',views.index,name="index"),
    path('sample/',views.sample,name="sample"),
    path("sample_app2/",views.sample_view,name="sample_view"),
]

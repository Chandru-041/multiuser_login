from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('admin/', views.admin, name='admin'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
]

from django.urls import path
from . import views

app_name = 'timeline'

urlpatterns = [
    path('global/', views.global_timeline, name='global_timeline'),
    path('personal/', views.personal_timeline, name='personal_timeline'),
]
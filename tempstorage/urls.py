from django.urls import path
from . import views

urlpatterns = [
    path('store-data/', views.store_data, name='store_data'),
    path('get-data/', views.get_data, name='get_data'),
]
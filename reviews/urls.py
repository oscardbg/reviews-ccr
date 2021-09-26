from .views import index, storeList
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index'),
	path('tiendas/', storeList, name='stores'),
]
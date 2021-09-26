from .views import index, StoreListView
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index'),
	path('tiendas/', StoreListView.as_view(), name='stores'),
]
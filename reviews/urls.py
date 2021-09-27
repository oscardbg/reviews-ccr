from .views import index, storeList, createReview, StoreDetailView
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index'),
	path('tiendas/', storeList, name='stores'),
	path('tiendas/<int:pk>/', StoreDetailView.as_view(), name='store'),
	path('review/<int:storeId>', createReview, name='create'),
]
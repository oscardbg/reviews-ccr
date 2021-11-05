from .views import index, about, storeList, createReview, StoreDetailView
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index'),
	path('categorias/<int:ctg>/', storeList, name='stores'),
	path('tiendas/<int:pk>/', StoreDetailView.as_view(), name='store'),
	path('review/<int:storeId>/', createReview, name='create'),
	path('about/', about, name='about')
]
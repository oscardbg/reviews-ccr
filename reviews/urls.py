from .views import index, storeList, createReview
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index'),
	path('tiendas/', storeList, name='stores'),
	path('review/', createReview, name='review')
]
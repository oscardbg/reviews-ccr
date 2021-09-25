from .views import index
from django.urls import path

app_name = 'reviews'

urlpatterns = [
	path('', index, name='index')
]
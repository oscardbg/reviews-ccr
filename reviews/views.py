from django.db import models
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Category, Store, Review

def index(request):
	return render(request, 'reviews/index.html')

class StoreListView(ListView):
	model = Store
	paginate_by = 20
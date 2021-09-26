from os import name
from django.db import models
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Category, Store, Review

def index(request):
	return render(request, 'reviews/index.html')

def storeList(request):
	categories = Category.objects.all()
	
	storeTxt = request.GET.get('storeTxt') or ''
	categTxt = request.GET.get('categTxt') or ''
	if storeTxt and categTxt:
		store_list = Store.objects.filter(name__icontains=storeTxt, category=Category.objects.get(id=categTxt))
	elif storeTxt != '' and categTxt == '':
		store_list = Store.objects.filter(name__icontains=storeTxt)
	elif storeTxt == '' and categTxt != '':
		store_list = Store.objects.filter(category=Category.objects.get(id=categTxt))
	else:
		store_list = Store.objects.all()

	context = {
		'store_list': store_list,
		'categories': categories
	}

	return render(request, 'reviews/store_list.html', context)

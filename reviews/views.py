from django.views.generic import ListView, DetailView
from .models import Category, Store, Review
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
	return render(request, 'reviews/index.html')

def storeList(request):
	categories = Category.objects.all()
	
	storeTxt = request.GET.get('storeTxt') or ''
	categTxt = request.GET.get('categTxt') or ''
	catObj = Category.objects.get(id=categTxt) if categTxt else None

	if storeTxt and categTxt:
		store_list = Store.objects.filter(name__icontains=storeTxt, category=catObj)
	elif storeTxt != '' and categTxt == '':
		store_list = Store.objects.filter(name__icontains=storeTxt)
	elif storeTxt == '' and categTxt != '':
		store_list = Store.objects.filter(category=catObj)
	else:
		store_list = Store.objects.all()

	page = request.GET.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1
	
	paginator = Paginator(store_list, 20)
	page_obj = paginator.get_page(page)

	context = {
		'store_list': store_list,
		'categories': categories,
		'page_obj': page_obj
	}

	return render(request, 'reviews/store_list.html', context)

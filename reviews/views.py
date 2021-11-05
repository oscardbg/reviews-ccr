from django.core import paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Category, Store, Review
from django.core.paginator import Paginator
from .forms import ReviewForm

def index(request):
	return render(request, 'reviews/index.html')

def about(request):
	return render(request, 'reviews/about.html')

def storeList(request, ctg):
	categories = Category.objects.all()
	
	storeTxt = request.GET.get('storeTxt') or ''
	catObj = None

	if ctg == 0:
		if storeTxt:
			store_list = Store.objects.filter(name__icontains=storeTxt)
		else:
			store_list = Store.objects.all()
	else:
		catObj = Category.objects.get(id=ctg)
		if storeTxt:
			store_list = Store.objects.filter(name__icontains=storeTxt, category=catObj)
		else:
			store_list = Store.objects.filter(category=catObj)

	page = request.GET.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1
	
	paginator = Paginator(store_list, 10)
	page_obj = paginator.get_page(page)

	context = {
		'catObj': catObj,
		'categories': categories,
		'page_obj': page_obj
	}

	return render(request, 'reviews/store_list.html', context)

class StoreDetailView(DetailView):
	model = Store

def createReview(request, storeId):
	store = Store.objects.get(id=storeId)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.store=store
			instance.save()
			return redirect('reviews:store', storeId)
	else:
		form = ReviewForm()

	context = {
		'form': form,
		'store': store
	}
	return render(request, 'reviews/review_add.html', context)

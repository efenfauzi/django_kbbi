from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def main_page(request):

	data = KBBIData.objects.all()

	if request.method == 'GET':
		katakunci = request.GET.get('katakunci')

		print katakunci


		kosong = '<b>Pencarian <span class="red-text">%s</span> tidak ditemukan</b>' %katakunci

		if katakunci is None:
			kosong = ''

		try:
			hasil = KBBIData.objects.filter(katakunci__istartswith=katakunci)
		except:
			return render(request, 'kbbi/main_page.html', {'kosong' : kosong})



		print hasil.count()

		paginator = Paginator(hasil, 3) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			hasil_search = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			hasil_search = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			hasil_search = paginator.page(paginator.num_pages)

		index = hasil_search.number - 1  # edited to something easier without index
		max_index = len(paginator.page_range)
		start_index = index - 3 if index >= 3 else 0
		end_index = index + 4 if index <= max_index - 4 else max_index
		page_range = list(paginator.page_range)[start_index:end_index]

		return render(request, 'kbbi/main_page.html' , 
								{'hasil_search' : hasil_search, 
								'katakunci' : katakunci,
								'page_range' : page_range,
								'kosong' : kosong})



	return render(request, 'kbbi/main_page.html')


def search_api(request):
	

	return HttpResponse("API Ok")
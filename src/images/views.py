from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Image
from .forms import AddImage


def add_images(request):
	form = AddImage(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		obj = Image.objects.create(
				title = form.cleaned_data.get('title'), 
				description = form.cleaned_data.get('description'),
				img_url = form.cleaned_data.get('image')
			)
		return HttpResponseRedirect('/view-images/')
	if form.errors:
		errors = form.errors

	template_name = 'images/add_images.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)

def display_images(request):
	template_name = 'images/display_images.html'
	queryset = Image.objects.all()
	context = {"object_list": queryset}
	return render(request, template_name, context)

def image_details(request, slug):
	template_name = 'images/image_details.html'
	obj = get_object_or_404(Image, slug=slug)
	context = {"object": obj}
	return render(request, template_name, context)
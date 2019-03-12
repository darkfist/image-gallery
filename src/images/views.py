from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Image, ImageUpload
from .forms import AddImage


@login_required()
def add_images(request):
	form = AddImage(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():

			# saving the details in the db
			obj = Image.objects.create(
					title = form.cleaned_data.get('title'), 
					description = form.cleaned_data.get('description'),
					uploaded_by = request.user
				)

			# uploading the first image with same id
			query = Image.objects.latest('id')
			obj = ImageUpload.objects.create(
					image_id = query.id,
					name = form.cleaned_data.get('title'),
					image_url = form.cleaned_data.get('image'),
				)

			# looping through all other images and uploading with same id
			for i in range(2,11):
				extra = 'image' + str(i)
				if (str(form.cleaned_data.get(extra)) != 'None'):
					obj = ImageUpload.objects.create(
						image_id = query.id,
						name = form.cleaned_data.get('title'), 
						image_url = form.cleaned_data.get(extra),
					)
			return redirect('images:view')
			
	if form.errors:
		errors = form.errors

	template_name = 'images/add_images.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)


def display_images(request):
	template_name = 'images/display_images.html'
	
	# querying Image table from db
	queryset1 = Image.objects.all().order_by('-pk')

	# querying ImageUpload table from db
	queryset2 = ImageUpload.objects.all()
	
	context = {"object_list": queryset1, "image_list":queryset2}
	return render(request, template_name, context)


@login_required()
def user_images(request):
	template_name = 'images/user_images.html'

	# querying Image table from db
	queryset1 = Image.objects.filter(uploaded_by=request.user).order_by('-pk')

	# querying ImageUpload table from db
	queryset2 = ImageUpload.objects.all()

	context = {"object_list": queryset1, "image_list":queryset2}
	return render(request, template_name, context)



def image_details(request, slug):
	template_name = 'images/image_details.html'
	
	# querying Image table from db to get single row
	obj = get_object_or_404(Image, slug=slug)

	# querying ImageUpload table from db
	queryset = ImageUpload.objects.all()
	
	context = {"object": obj, "image_list":queryset}
	return render(request, template_name, context)

@login_required()
def delete_image(request, pk):
	# querying Image table from db to get single row and deleting it
	instance1 = get_object_or_404(Image, pk=pk).delete()
	instance2 = ImageUpload.objects.filter(image_id=pk).delete()
	
	messages.success(request, "successfully deleted the image")
	return redirect('images:user_img')
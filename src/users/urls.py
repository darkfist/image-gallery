from django.conf.urls import url

from .views import display_images, add_images, image_details


urlpatterns = [
    url(r'^view-images/$', display_images, name='view'),
    url(r'^image-details/(?P<slug>[\w-]+)/$', image_details, name='details'),
    url(r'^add/$', add_images, name='add'),
] 
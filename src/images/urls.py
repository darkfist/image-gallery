from django.conf.urls import url

<<<<<<< HEAD
from .views import display_images, add_images, image_details, user_images
=======
from .views import display_images, add_images, image_details
>>>>>>> parent of 2122c2c... temp. commit


urlpatterns = [
    url(r'^view-images/$', display_images, name='view'),
<<<<<<< HEAD
    url(r'^my-images/$', user_images, name='user_img'),
=======
>>>>>>> parent of 2122c2c... temp. commit
    url(r'^image-details/(?P<slug>[\w-]+)/$', image_details, name='details'),
    url(r'^add/$', add_images, name='add'),
]
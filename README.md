[![Python](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](http://www.python.org/download/)
# Django Image Gallery

A simple Image Gallery made with Python and Django.

## Description

Django Image Gallery is a platform where users can register and then upload their images. These images can be viewed by anyone.
Accepted Image Formats : JPEG, JPG, PNG, GIF

## Installation and Dependencies

After cloning the repository on your machine move into the ```src\``` directory and install the dependencies by ```pip install requirements.txt```


##### Connecting to database:
This application requires MySQL Database. Check [this link](https://goo.gl/85wAeM) if you don't know how to install MySQL.
Create a database with name "imagesDB" and set the MySQL username and password in the ```base.py``` file present at ```src\image_gallery\settings```.

## Starting the App
from the ```src\``` directory run the following commands:
```
~/src$ python manage.py makemigrations
~/src$ python manage.py migrate
~/src$ python manage.py collectstatic
~/src$ python manage.py createsuperuser
```
then enter the details which will be asked, like username, email and password.

Now the app is fully setup.
Run the following command to start the app in your browser:
```
~/src$ python manage.py runserver
```
Now just go to ```http://127.0.0.1:8000``` in your browser to access the app.
You can also go to ```http://127.0.0.1:8000/admin``` in your browser and login with your 'superuser' credentials (created in previous step) to access the admin panel.

## Features

- Users can register for a new account.
- Users can login and upload images on behalf of themselves.
- Users can upload multiple images at a time (Max=10).
- Users can give title and description to the images.
- Users can view the images (with or without login).
- Users can delete their own images.

## Development

This project was made as a screening task for the [FOSSEE Fellowship 2019 Collaborative Communities](https://fossee.in/)
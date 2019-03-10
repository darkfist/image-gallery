from django import forms
from django.core.validators import FileExtensionValidator

class AddImage(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	image 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)])
	image2 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image3 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image4 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image5 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image6	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image7 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image8 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image9 	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
	image10	= forms.ImageField(validators=[FileExtensionValidator(
												allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
												)], required=False)
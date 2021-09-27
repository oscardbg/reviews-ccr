from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Review

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['score', 'name', 'description']
		labels = {
			'score': _(''),
			'name': _('Nombre:'),
			'description': _('Descripcion:')
		}
	
	def clean_score(self):
		score = self.cleaned_data.get('score')
		if score < 1:
			raise ValidationError('Debes ingresar un valor...')
		return score

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == '':
			raise ValidationError('Debes ingresar un nombre...')
		return name

	def clean_description(self):
		description = self.cleaned_data.get('description')
		if description == '':
			raise ValidationError('Ingresar algo aqui...')
		if description == 'create':
			raise ValidationError('Anything but create...')
		return description
from django.forms import Form, ModelForm, ValidationError, RadioSelect, TextInput, Textarea
from django.utils.translation import gettext_lazy as _
from .models import Review

SCORES = [(1, ''),(2, ''),(3, ''),(4, ''),(5, ''),]

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['score', 'name', 'description']
		labels = {
			'score': _(''),
			'name': _('Nombre:'),
			'description': _('Descripcion:')
		}
		widgets = {
			'score': RadioSelect(choices=SCORES),
			'name': TextInput(attrs={'autocomplete': 'off'}),
			'description': Textarea(attrs={'autocomplete': 'off'})
		}
			
	def clean_score(self):
		score = self.cleaned_data.get('score')
		if score < 0:
			raise ValidationError('Debes ingresar un valor...')
		return score

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == '':
			raise ValidationError('Debes ingresar un nombre...')
		return name

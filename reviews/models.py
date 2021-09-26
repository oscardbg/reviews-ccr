from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Store(models.Model):
	name = models.CharField(max_length=150)
	room = models.CharField(max_length=150,  null=True, blank=True)
	description = models.TextField( null=True, blank=True)
	score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	logo = models.TextField( null=True, blank=True)
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, related_name='stores', null=True, blank=True
	)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Review(models.Model):
	score = models.IntegerField()
	name = models.CharField(max_length=150)
	description = models.TextField( null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	store = models.ForeignKey(
		Store, on_delete=models.SET_NULL, related_name='reviews', null=True, blank=True
	)

	def __str__(self):
		return f'{self.name}, {self.score}'

	class Meta:
		ordering = ['-created']
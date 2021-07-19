from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	tags = models.ManyToManyField(Tag, blank=True)
	title = models.CharField(max_length=255)
	content = models.TextField()
	description = models.TextField(blank=True)
	image = models.CharField(max_length=255)
	image_text = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	published_at = models.DateTimeField(blank=True, null=True)
	is_published = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)

	class Meta:
		ordering = ['-created_at']

	def save(self, *args, **kwargs):
		if self.is_published and not self.published_at:
			self.published_at = timezone.now()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
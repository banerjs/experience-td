from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from djangotoolbox import fields

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=1000)
	email = models.EmailField(db_index=True)
	url = models.URLField(max_length=1000)
	articles = fields.DictField(fields.EmbeddedModelField('Article'))

	class Meta:
		app_label = 'articles'

	def __unicode__(self):
		return self.name + '(' + self.email + ')'

	def get_absolute_url(self):				# This is the URL for the User Homepage
		return reverse('homepage', args=[slugify(self.id), slugify(self.name)])

	def get_article_url(self):				# This is the URL for the User's articles
		return reverse('articles', args=[slugify(self.id), slugify(self.name)])

	def get_edit_url(self):					# This is the URL for the User to edit their articles
		return reverse('edit', args=[slugify(self.id), slugify(self.name)])

class Article(models.Model):
	article_id = models.CharField(max_length=1000)
	title = models.CharField(max_length=1000)
	author = models.CharField(max_length=1000)
	url = models.URLField(max_length=1000)
	reasons = models.TextField()
	comments = models.TextField()
	creation_date = models.DateTimeField()
	quotes = fields.ListField()

	class Meta:
		app_label = 'articles'

	def __unicode__(self):
		return self.title + (' - ' + self.author if self.author is not None else '')

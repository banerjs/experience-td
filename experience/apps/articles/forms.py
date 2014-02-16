from django import forms

from experience.apps.articles.models import User, Article

# Create the forms here

class ArticleForm(forms.Form):
	article_title = forms.CharField()
	article_author = forms.CharField(required=False)
	article_url = forms.URLField(max_length=10000, required=False)
	article_reasons = forms.CharField(required=False)
	article_comments = forms.CharField(required=False)

	def __init__(self, data=None, *args, **kwargs):
		super(ArticleForm, self).__init__(data=data, *args, **kwargs)
		self.quote_fields = self.process_quotes(data)

	def save(self, user):
		article = Article(title=self.cleaned_data['article_title'], \
						  author=self.cleaned_data['article_author'], \
						  url=self.cleaned_data['article_url'], \
						  reason=self.cleaned_data['article_reasons'], \
						  comments=self.cleaned_data['article_comments'], \
						  quotes=[self.cleaned_data.get(k) for k in self.quote_fields])
		user.articles.append(article)
		user.save()

	def process_quotes(self, data=None):
		quotes = []

		# First check if there are any quotes that have been entered
		if not (data and data.get('article_quote_0')):
			return quotes

		# Then parse through each of the quotes and show them
		for k, v in data.iteritems():
			if not k.startswith('article_quote'):
				continue
			field_name = k
			self.fields[k] = forms.CharField(required=False)
			quotes.append(k)

		return quotes
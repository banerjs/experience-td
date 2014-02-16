from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from experience.apps.articles.forms import ArticleForm
from experience.apps.articles.models import User, Article

# Create your views here.

def render_home(request, template_name="home.html"):
	if request.POST.get("email") is not None:
		try:
			user = User.objects.get(email=request.POST.get('email'))
		except User.DoesNotExist:
			user = User(email=request.POST.get('email'), name=request.POST.get('name'), url=request.POST.get('url'))
			user.save()
		response = redirect(user.get_absolute_url())
		response.set_signed_cookie("user_id", user.id)
		response.set_signed_cookie("user_name", user.name)
		return response
	response = render(request, template_name)
	response.delete_cookie("user_id")
	response.delete_cookie("user_name")
	return response

def render_homepage(request, id, name, template_name="homepage.html"):
	try:
		user = User.objects.get(id=id)
		if request.get_signed_cookie("user_id") != user.id:
			raise PermissionDenied
		return render(request, template_name, { 'friends': User.objects.exclude(id=id), 'user': user })
	except:
		raise PermissionDenied

def render_articles(request, id, name, template_name="articles.html"):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404
	return render(request, template_name, { 'articles': user.articles, 'user': User.objects.get(id=id), 'login_id': request.get_signed_cookie("user_id"), 'login_name': slugify(request.get_signed_cookie("user_name")) })

def render_edit(request, id, name, template_name="edit.html"):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404

	form = ArticleForm(data=request.POST or None)
	if form.is_valid():
		form.save(user)
		messages.success(request, "The Article has been submitted successfully")
	elif request.POST:
		messages.error(request, "There are errors in this form. Title is a Required Field")

	return render(request, template_name, { 'articles': user.articles, 'user': user, 'login_id': request.get_signed_cookie("user_id"), 'login_name': slugify(request.get_signed_cookie("user_name")) })

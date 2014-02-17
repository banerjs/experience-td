from django.conf import settings

# Context Processors for experience

# Adds in the settings object to every template
def include_settings(request):
	return { 'settings': settings }

from django.views import View
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Project, User





def projects(request, username):
	if username:
		user = User.objects.get(login=username)
		list_projects = Project.objects.filter(user=user.id)
		return render(request, 'projects/projects.html', {'projects': list_projects, 'user': username})
	else:
		list_projects = Project.objects.all().count()
		return render(request, 'projects/projects.html')
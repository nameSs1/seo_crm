from django.views import View
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Project, User, Task


def projects(request, username):
	if username:
		user = User.objects.get(login=username)
		list_projects = Project.objects.filter(user=user.id)
		return render(request, 'projects/projects.html', {'projects': list_projects, 'user': username})
	else:
		list_projects = Project.objects.all().count()
		return render(request, 'projects/projects.html')


def project_tasks(request, title_project):
	project = Project.objects.filter(domain_names__iendswith="{}/".format(title_project))[0]
	list_tasks_project = Task.objects.filter(project=project.id)
	return render(request, 'projects/projecttasks.html', {'list_tasks_project': list_tasks_project})
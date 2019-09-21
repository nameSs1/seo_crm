from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, User


def projects(request, username):
	if username:
		user = User.objects.get(login=username)
		list_projects = Project.objects.filter(user=int(user.id))
		list_projects = [project.domain_names for project in list_projects]
		return HttpResponse('Тут будет список проектов пользователя {}'.format(list_projects))
	else:
		list_projects = Project.objects.all().count()
		return render(request, 'projects/projects.html')
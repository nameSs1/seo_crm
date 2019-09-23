
from django.shortcuts import render


from .models import Project, User


def projects(request, username):
	if username:
		user = User.objects.get(login=username)
		list_projects = Project.objects.filter(user=user.id)
		m = Project._meta.get_fields()
		return render(request, 'projects/projects.html', {'projects': list_projects, 'user': username, 'm': m})
	else:
		list_projects = Project.objects.all().count()
		return render(request, 'projects/projects.html')
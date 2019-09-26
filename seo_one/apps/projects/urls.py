from django.urls import path, re_path


from . import views

urlpatterns = [
	re_path(r'^(?P<username>\w+$)', views.projects, name='projects'),
	re_path(r'^\w+/(?P<title_project>[a-z0-9]+[.][a-z]{2,3}$)', views.project_tasks, name='project tasks'),
]  # /projects/Lesha/onliner.by
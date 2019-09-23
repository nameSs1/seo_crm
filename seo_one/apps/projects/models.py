import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	login = models.CharField(max_length=30, unique=True)
	status = models.CharField(max_length=30, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.login)


class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	domain_names = models.CharField(max_length=30, unique=True)
	period_date = models.DateField(help_text = 'дата начала отчетного месяца')
	admin_panel = models.ForeignKey('Admin_panel', on_delete=models.SET_NULL, null=True, blank=True)
	server = models.ForeignKey('Server', on_delete=models.SET_NULL, null=True, blank=True)
	yandex_account = models.ForeignKey('Yandex_account', on_delete=models.SET_NULL, null=True, blank=True)
	google_account = models.ForeignKey('Google_account', on_delete=models.SET_NULL, null=True, blank=True)
	priority_options = (('A', 'высокий'), ('B', 'средний'), ('C', 'низкий'))
	priority = models.CharField(max_length=1, choices=priority_options, default='B')
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{} {} {}".format(self.domain_names, self.user, self.period_date)

	def get_title(self):
		return self.domain_names.lstrip('https://').lstrip('www.').rstrip('/')


class Admin_panel(models.Model):
	link = models.CharField(max_length=30)
	login = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.login)


class Server(models.Model):
	link_to_server_FTP = models.CharField(max_length=30)
	login = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.login)


class Yandex_account(models.Model):
	link = models.CharField(max_length=30)
	login = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30, blank=True)
	counter_number_metric = models.CharField(max_length=20)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.login)


class Google_account(models.Model):
	link = models.CharField(max_length=30)
	login = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30, blank=True)
	analytics_counter = models.CharField(max_length=10)
	code_GTM = models.CharField(max_length=10)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.login)


class Standart_task(models.Model):
	standart_task_tatle = models.CharField(max_length=30, unique=True)
	standart_task_text = models.TextField(blank=True)
	norm_of_time = models.TimeField(blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.standart_task_tatle)


class Task(models.Model):
	standart_task = models.ForeignKey(Standart_task, on_delete=models.PROTECT)
	project = models.ForeignKey(Project, on_delete=models.PROTECT)
	status_options = (('P', 'запланирована'), ('W', 'в работе'), ('D', 'выполнена'))
	task_status = models.CharField(max_length=1, choices=status_options, default='P')
	priority_options = (('A', 'высокий'), ('B', 'средний'), ('C', 'низкий'))
	priority = models.CharField(max_length=1, choices=priority_options, default='B')
	planned_time = models.TimeField(blank=True)
	elapsed_time = models.TimeField(blank=True)
	comments = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{} {} {} {}".format(self.project, self.standart_task, self.task_status, self.priority)


class Reqest(models.Model):
	project = models.ForeignKey(Project, on_delete=models.PROTECT)
	value = models.CharField(max_length=255)
	page_promotion = models.ForeignKey('Page_url', on_delete=models.PROTECT)
	priority_options = (('A', 'высокий'), ('B', 'средний'), ('C', 'низкий'))
	priority = models.CharField(max_length=1, choices=priority_options, default='B')
	# request_cost
	# request_characteristic
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{} {}".format(self.page_promotion, self.value)


class Page_url(models.Model):
	page_url = models.CharField(max_length=50, unique=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "{}".format(self.page_url)


class Result(models.Model):
	request = models.ForeignKey(Reqest, on_delete=models.PROTECT)
	position_in_google = models.PositiveSmallIntegerField()
	position_in_yandex = models.PositiveSmallIntegerField()
	page_url = models.ForeignKey(Page_url, on_delete=models.PROTECT)
	page_result = models.CharField(max_length=50, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "{} {} {}".format(self.page_url, self.position_in_google, self.position_in_yandex)


# class Request_cost(models.Model):
# 	request_cost_id
# 	request_cost_value


# class Request_characteristic(models.Model):
# 	request_characteristic_id
# 	request_characteristic_value

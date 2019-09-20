# Generated by Django 2.2.5 on 2019-09-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Google_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('analytics_counter', models.CharField(max_length=10)),
                ('code_GTM', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(max_length=50, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_names', models.CharField(max_length=30, unique=True)),
                ('period_date', models.DateField(help_text='дата начала отчетного месяца')),
                ('priority', models.CharField(choices=[('A', 'высокий'), ('B', 'средний'), ('C', 'низкий')], default='B', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('admin_panel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Admin_panel')),
                ('google_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Google_account')),
            ],
        ),
        migrations.CreateModel(
            name='Reqest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('A', 'высокий'), ('B', 'средний'), ('C', 'низкий')], default='B', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('page_promotion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Page_url')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_to_server_FTP', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Standart_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standart_task_tatle', models.CharField(max_length=30, unique=True)),
                ('standart_task_text', models.TextField(blank=True)),
                ('norm_of_time', models.TimeField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, unique=True)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yandex_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('counter_number_metric', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_status', models.CharField(choices=[('P', 'запланирована'), ('W', 'в работе'), ('D', 'выполнена')], default='P', max_length=1)),
                ('priority', models.CharField(choices=[('A', 'высокий'), ('B', 'средний'), ('C', 'низкий')], default='B', max_length=1)),
                ('planned_time', models.TimeField(blank=True)),
                ('elapsed_time', models.TimeField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Project')),
                ('standart_task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Standart_task')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_in_google', models.PositiveSmallIntegerField()),
                ('position_in_yandex', models.PositiveSmallIntegerField()),
                ('page_result', models.CharField(blank=True, max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('page_url', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Page_url')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Reqest')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Server'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='yandex_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Yandex_account'),
        ),
    ]

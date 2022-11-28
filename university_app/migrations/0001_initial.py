g# Generated by Django 4.1.3 on 2022-11-27 23:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
import university_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('street', models.CharField(max_length=200, verbose_name='Street Name')),
                ('city', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField(default=1000)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('level', models.CharField(choices=[(1, 'FirstClass'), (2, 'SecondClass'), (3, 'ThirdClass'), (4, 'MasterClass'), (5, 'DoctoralClass')], default=university_app.models.StudyLevel['FirstClass'], max_length=100)),
                ('speciality', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='email of group')),
                ('student_number', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'std_group',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('due', models.DecimalField(decimal_places=2, default=21, max_digits=4)),
                ('model_type', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[(1, 'FirstClass'), (2, 'SecondClass'), (3, 'ThirdClass'), (4, 'MasterClass'), (5, 'DoctoralClass')], default=university_app.models.StudyLevel['FirstClass'], max_length=100)),
                ('study', models.ManyToManyField(to='university_app.group')),
            ],
            options={
                'db_table': 'module',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('familyName', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('birthDate', models.DateField(default=datetime.date(2004, 1, 1))),
                ('email_work', models.EmailField(blank=True, max_length=150, null=True, verbose_name='workemail')),
                ('photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/teachers')),
                ('grade', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='TeacherModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2022)),
                ('nb_Hours', models.IntegerField(default=1)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.module')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.teacher')),
            ],
            options={
                'db_table': 'teacher_modules',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_modules',
            field=models.ManyToManyField(through='university_app.TeacherModules', to='university_app.module'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('familyName', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('birthDate', models.DateField(default=datetime.date(2004, 1, 1))),
                ('photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/students')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university_app.address')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university_app.group')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]

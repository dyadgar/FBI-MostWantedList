# Generated by Django 3.0.1 on 2020-01-01 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0003_auto_20200101_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBImostwanteddata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('place_ofbirth', models.CharField(blank=True, max_length=30, null=True)),
                ('hair', models.CharField(blank=True, max_length=30, null=True)),
                ('eyes', models.CharField(blank=True, max_length=30, null=True)),
                ('height_max', models.CharField(blank=True, max_length=30, null=True)),
                ('height_min', models.CharField(blank=True, max_length=30, null=True)),
                ('weight', models.CharField(blank=True, max_length=30, null=True)),
                ('build', models.CharField(blank=True, max_length=30, null=True)),
                ('sex', models.CharField(blank=True, max_length=30, null=True)),
                ('race_raw', models.CharField(blank=True, max_length=30, null=True)),
                ('nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('reward', models.CharField(blank=True, max_length=500, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('caution', models.CharField(blank=True, max_length=500, null=True)),
                ('warning', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_dateofbirth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_posters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('wanted_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.FBImostwanteddata')),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
                ('caption', models.CharField(blank=True, max_length=50, null=True)),
                ('wanted_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.FBImostwanteddata')),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('wanted_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.FBImostwanteddata')),
            ],
        ),
        migrations.CreateModel(
            name='Informant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FBIOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('FBI Intelligence Branch', 'FBI Intelligence Branch'), ('FBI National Security Branch', 'FBI National Security Branch'), ('FBI Criminal, Cyber, Response, and Services Branch', 'FBI Criminal, Cyber, Response, and Services Branch'), ('FBI Science and Technology Branch', 'FBI Science and Technology Branch'), ('FBI Information and Technology Branch', 'FBI Information and Technology Branch'), ('FBI Human Resources Branch', 'FBI Human Resources Branch'), ('Other', 'Other')], default='available', max_length=100)),
                ('division', models.CharField(choices=[('Directorate of Intelligence', 'Directorate of Intelligence'), ('Office of Partner Engagement', 'Office of Partner Engagement'), ('Counterterrorism Division', 'Counterterrorism Division'), ('Counterintelligence Division', 'Counterintelligence Division'), ('Weapons of Mass Destruction Directorate', 'Weapons of Mass Destruction Directorate'), ('Criminal Investigative Division', 'Criminal Investigative Division'), ('Cyber Division', 'Cyber Division'), ('Critical Incident Response Group', 'Critical Incident Response Group'), ('International Operations Division', 'International Operations Division'), ('Operational Technology Division', 'Operational Technology Division'), ('Laboratory Division', 'Laboratory Division'), ('Criminal Justice Information Services Division', 'Criminal Justice Information Services Division'), ('IT Customer Relationship and Management Division', 'IT Customer Relationship and Management Division'), ('IT Applications and Data Division', 'IT Applications and Data Division'), ('IT Infrastructure Division', 'IT Infrastructure Division'), ('Training Division', 'Training Division'), ('Cyber Division', 'Cyber Division'), ('Human Resources Division', 'Human Resources Division'), ('Security Division', 'Security Division'), ('Faculties and Logistics Services Division', 'Faculties and Logistics Services Division'), ('Finance Division', 'Finance Division'), ('Inspection Division', 'Inspection Division'), ('Records Management Division', 'Records Management Division'), ('Resource Planning Office', 'Resource Planning Office')], default='available', max_length=100)),
                ('branch_office_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fbimostwanteddata',
            name='date_ofbirth',
            field=models.ManyToManyField(to='profile_app.Most_wanted_dateofbirth'),
        ),
        migrations.AddField(
            model_name='fbimostwanteddata',
            name='languages',
            field=models.ManyToManyField(to='profile_app.Most_wanted_languages'),
        ),
    ]

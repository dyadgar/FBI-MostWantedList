# Generated by Django 3.0.1 on 2019-12-31 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Most_wanted_alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
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
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Most_wanted_posters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=5000)),
                ('message', models.CharField(max_length=500000)),
                ('is_read', models.BooleanField(default=False)),
                ('creation_date', models.DateField()),
                ('receive_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_recieved', to=settings.AUTH_USER_MODEL)),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
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
        migrations.CreateModel(
            name='FBImostwanteddata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('place_ofbirth', models.CharField(max_length=30)),
                ('hair', models.CharField(max_length=30)),
                ('eyes', models.CharField(max_length=30)),
                ('height_max', models.CharField(max_length=30)),
                ('height_min', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=30)),
                ('build', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('race_raw', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=30)),
                ('reward', models.CharField(max_length=500)),
                ('remarks', models.CharField(max_length=500)),
                ('caution', models.CharField(max_length=500)),
                ('warning', models.CharField(max_length=200)),
                ('aliases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Most_wanted_alias')),
                ('date_ofbirth', models.ManyToManyField(to='profile_app.Most_wanted_dateofbirth')),
                ('languages', models.ManyToManyField(to='profile_app.Most_wanted_languages')),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Most_wanted_photos')),
                ('posters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Most_wanted_posters')),
            ],
        ),
    ]

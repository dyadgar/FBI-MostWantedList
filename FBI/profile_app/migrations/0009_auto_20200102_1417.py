# Generated by Django 3.0.1 on 2020-01-02 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0008_auto_20200101_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='build',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='caution',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='eyes',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='hair',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='height_max',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='height_min',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='nationality',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='place_ofbirth',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='race_raw',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='reward',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='sex',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='warning',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fbimostwanteddata',
            name='weight',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='most_wanted_photos',
            name='wanted_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='profile_app.FBImostwanteddata'),
        ),
    ]

from django.shortcuts import render
from profile_app import models

# Create your views here.


# FBI Most Wanted List Section

def most_wanted_list(request):

    list_of_wanted_people = models.FBImostwanteddata.objects.all()
    list_of_images = models.Most_wanted_photos.objects.all()

    mostwanted_list_dict = {
    'wantedpeople': list_of_wanted_people,
    'images': list_of_images
    }

    return render(request, "most_wanted_app/mostwantedpeople.html",mostwanted_list_dict )


def wanted_person_details(request, id):
    wanted_person = models.FBImostwanteddata.objects.get(id=id)
    images = models.Most_wanted_photos.objects.filter(wanted_person=wanted_person).all()
    posters= models.Most_wanted_posters.objects.filter(wanted_person__id=id).all()
    aliases = models.Most_wanted_alias.objects.filter(wanted_person__id=id).all()
    date_of_birth =models.Most_wanted_dateofbirth.objects.filter(fbimostwanteddata__id=id).all() #many to many
    languages = models.Most_wanted_languages.objects.filter(fbimostwanteddata__id=id).all()  #many to many
    for image in images:
        print(image.link)
    return render(request, "most_wanted_app/wantedpersondetails.html", {'wanted_person':wanted_person, 'images':images, 'posters':posters, 'aliases':aliases, ' date_of_birth': date_of_birth, 'languages':languages})

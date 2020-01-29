import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FBI.settings')
import django
django.setup()
from profile_app.models import FBImostwanteddata,Most_wanted_alias, Most_wanted_dateofbirth, Most_wanted_languages, Most_wanted_photos, Most_wanted_posters
from datetime import timedelta    #this makes it possible to add days to a previous saved date
from random import randint
import json
import requests
#create objects to input data in tables


response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)

#Most Wanted List
# to add images 2nd
# for i in range(1, 20):
#     data = json.loads(response.content)
#     for q in range(len(data['items'][i]['images'])):
#         images = Most_wanted_photos(link=data['items'][i]['images'][q]['original'], caption=data['items'][i]['images'][q]['caption'], wanted_person=FBImostwanteddata.objects.get(name= data['items'][i]['title']))
#         images.save()

# to add posters 2nd
# for i in range(3, 20):
#     data = json.loads(response.content)
#     for q in range(len(data['items'][i]['files'])):
#         posters = Most_wanted_posters(link=data['items'][i]['files'][q]['url'], language=data['items'][i]['files'][q]['name'], wanted_person=FBImostwanteddata.objects.get(name=data['items'][i]['title']))
#         posters.save()
# #
# # # to add aliases 2nd
# for i in range (3, 20):
#     data = json.loads(response.content)
#     if (data['items'][i]['aliases']) == None:
#             aliases = Most_wanted_alias(name=data['items'][i]['aliases'], wanted_person=FBImostwanteddata.objects.get(name=data['items'][i]['title']))
#             aliases.save()
#     elif (data['items'][i]['aliases']) != 'None':
#         for q in range(len(data['items'][i]['aliases'])):
#             aliases = Most_wanted_alias(name=data['items'][i]['aliases'][q],
#                                         wanted_person=FBImostwanteddata.objects.get(name=data['items'][i]['title']))
#             aliases.save()
#     else:
#         no_aliases= Most_wanted_alias(name=data['items'][i]['aliases'], wanted_person=FBImostwanteddata.objects.get(name=data['items'][i]['title']))
#         no_aliases.save()
#
# # for birthdays 3rd
# for i in range(1, 20):
#     data = json.loads(response.content)
#     if (data['items'][i]['dates_of_birth_used']) != None:
#         for q in data['items'][i]['dates_of_birth_used']:
#             bdays = Most_wanted_dateofbirth(date=q)
#             if not Most_wanted_dateofbirth.objects.filter(date=q).exists():
#                 bdays.save()
#             else:
#                 bdays =Most_wanted_dateofbirth.objects.filter(date=q).first()
#             wantedperson =FBImostwanteddata.objects.get(name=data['items'][i]['title'])
#             wantedperson.date_ofbirth.add(bdays)
#
# # for languages 3rd
# for i in range(1, 20):
#     data = json.loads(response.content)
#     if (data['items'][i]['languages']) != None:
#         for q in data['items'][i]['languages']:
#             language = Most_wanted_languages(name=q)
#             if not Most_wanted_languages.objects.filter(name=q).exists():
#                 language.save()
#             else:
#                 language = Most_wanted_languages.objects.filter(name=q).first()
#             wantedperson =FBImostwanteddata.objects.get(name=data['items'][i]['title'])
#             wantedperson.languages.add(language)

# for suspects first
# for i in range (1, 20):
#     data = json.loads(response.content)
#     suspect = FBImostwanteddata(
#         name=data['items'][i]['title'],
#         description=data['items'][i]['description'],
#         place_ofbirth=data['items'][i]['place_of_birth'],
#         hair=data['items'][i]['hair'],
#         eyes=data['items'][i]['eyes'],
#         height_max=data['items'][i]['height_max'],
#         height_min=data['items'][i]['height_min'],
#         weight=data['items'][i]['weight'],
#         build=data['items'][i]['build'],
#         sex=data['items'][i]['sex'],
#         race_raw=data['items'][i]['race_raw'],
#         nationality=data['items'][i]['nationality'],
#         reward=data['items'][i]['reward_text'],
#         remarks=data['items'][i]['remarks'],
#         caution=data['items'][i]['caution'],
#         warning=data['items'][i]['warning_message'])
#     suspect.save()
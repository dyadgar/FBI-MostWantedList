import null as null
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import options
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Messages(models.Model):
    sent_by = models.ForeignKey(User, related_name= 'sent_messages', on_delete=models.CASCADE)
    receive_by =models.ForeignKey(User, related_name= 'messages_recieved', on_delete=models.CASCADE)
    # sender = db.Column(db.String(255))
    # receiver = db.Column(db.String(255))
    subject = models.CharField(max_length=5000)
    message = models.CharField(max_length=5000)
    is_read = models.BooleanField(default=False)
    creation_date = models.DateField()
    def __repr__(self):
        return f"Message: {self.subject}"


#informant Section
class Informant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=150)
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)
    # email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    # sent = models.ForeignKey(Messages, on_delete=models.CASCADE)
    # recieved = models.ForeignKey(Messages, on_delete=models.CASCADE)

    def __repr__(self):      #dont really understand the point of repr????
        return f"Customer: {self.username} {self.first_name} {self.last_name}  {self.email} {self.phone_number} {self.address} {self.city} {self.country}"
# FBI Officer section
# class FbiBranches(models.Model):
#     branch_name = models.CharField(max_length=150)
#
# class Fbidivision(models.Model):
#     division_name = models.CharField(max_length=150)
#     branch = models.ForeignKey(FbiBranches, on_delete=models.CASCADE)


class FBIOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #linked to django default user model
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)
    # email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=150)
    BRANCHES = (
       ('FBI Intelligence Branch', ('FBI Intelligence Branch')),
       ('FBI National Security Branch', ('FBI National Security Branch')),
       ('FBI Criminal, Cyber, Response, and Services Branch', ('FBI Criminal, Cyber, Response, and Services Branch')),
       ('FBI Science and Technology Branch', ('FBI Science and Technology Branch')),
       ('FBI Information and Technology Branch', ('FBI Information and Technology Branch')),
       ('FBI Human Resources Branch', ('FBI Human Resources Branch')),
       ('Other', ('Other')),
    )
    branch = models.CharField(
       max_length=100,
       choices= BRANCHES,
       default='available',
   )
    DIVISIONS = (
       ('Directorate of Intelligence', ('Directorate of Intelligence')),
       ('Office of Partner Engagement', ('Office of Partner Engagement')),
       ('Counterterrorism Division', ('Counterterrorism Division')),
       ('Counterintelligence Division', ('Counterintelligence Division')),
       ('Weapons of Mass Destruction Directorate', ('Weapons of Mass Destruction Directorate')),
       ('Criminal Investigative Division', ('Criminal Investigative Division')),
       ('Cyber Division', ('Cyber Division')),
       ('Critical Incident Response Group', ('Critical Incident Response Group')),
       ('International Operations Division', ('International Operations Division')),
       ('Operational Technology Division', ('Operational Technology Division')),
       ('Laboratory Division', ('Laboratory Division')),
       ('Criminal Justice Information Services Division', ('Criminal Justice Information Services Division')),
       ('IT Customer Relationship and Management Division', ('IT Customer Relationship and Management Division')),
       ('IT Applications and Data Division', ('IT Applications and Data Division')),
       ('IT Infrastructure Division', ('IT Infrastructure Division')),
       ('Training Division', ('Training Division')),
       ('Cyber Division', ('Cyber Division')),
       ('Human Resources Division', ('Human Resources Division')),
       ('Security Division', ('Security Division')),
       ('Faculties and Logistics Services Division', ('Faculties and Logistics Services Division')),
       ('Finance Division', ('Finance Division')),
       ('Inspection Division', ('Inspection Division')),
       ('Records Management Division', ('Records Management Division')),
       ('Resource Planning Office', ('Resource Planning Office')),
    )
    division = models.CharField(
       max_length=100,
       choices= DIVISIONS,
       default='available',
   )
    branch_office_address = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    # sent = models.ForeignKey(Messages, on_delete=models.CASCADE)
    # recieved = models.ForeignKey(Messages, on_delete=models.CASCADE)

    def __repr__(self):  # dont really understand the point of repr????
        return f"Customer: {self.first_name} {self.last_name}  {self.email} {self.phone_number} {self.branch} {self.division} " \
               f"{self.branch_office_address} {self.city} "
#Most Wanted List


class Most_wanted_photos(models.Model):
    link = models.URLField(max_length=5000)
    caption = models.CharField(max_length=50, null=True, blank=True)
    wanted_person = models.ForeignKey('FBImostwanteddata', on_delete=models.CASCADE, related_name='photos') #if put '' in class section django will know this is the class you want to get it from

    def __repr__(self):
        return f"Most_wanted_photos: {self.link}"

    def __str__(self):
        return self.link


class Most_wanted_posters(models.Model):
    link = models.URLField(max_length=5000)
    language =models.CharField(max_length=50, null=True, blank=True)
    wanted_person = models.ForeignKey('FBImostwanteddata', on_delete=models.CASCADE)

    def __repr__(self):
        return f"Most_wanted_posters: {self.link}"


class Most_wanted_alias(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True)
    wanted_person = models.ForeignKey('FBImostwanteddata', on_delete=models.CASCADE)

    def __repr__(self):
        return f"Most_wanted_alias: {self.name}"


class Most_wanted_dateofbirth(models.Model): #manytomany
    date = models.CharField(max_length=50)

    def __repr__(self):
        return f"Most_wanted_dateofbirth: {self.date}"


class Most_wanted_languages(models.Model):  #manytomany
    name = models.CharField(max_length=150, unique=True)

    def __repr__(self):
        return f"Most_wanted_languages: {self.name}"


class FBImostwanteddata(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True, unique=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    date_ofbirth = models.ManyToManyField(Most_wanted_dateofbirth)  # ManytoMany
    place_ofbirth = models.CharField(max_length=60, null=True, blank=True)
    hair = models.CharField(max_length=60, null=True, blank=True)
    eyes = models.CharField(max_length=60, null=True, blank=True)
    height_max = models.CharField(max_length=60, null=True, blank=True)
    height_min = models.CharField(max_length=60, null=True, blank=True)
    weight = models.CharField(max_length=60, null=True, blank=True)
    build = models.CharField(max_length=60, null=True, blank=True)
    sex = models.CharField(max_length=60, null=True, blank=True)
    race_raw = models.CharField(max_length=60, null=True, blank=True)
    nationality = models.CharField(max_length=60, null=True, blank=True)
    languages = models.ManyToManyField(Most_wanted_languages)  # ManytoMany
    reward = models.CharField(max_length=5000, null=True, blank=True)
    remarks = models.CharField(max_length=5000, null=True, blank=True)
    caution = models.CharField(max_length=5000, null=True, blank=True)
    warning = models.CharField(max_length=2000, null=True, blank=True)

    @property
    def avatar(self):
        return self.photos.first()

    def __repr__(self):
        return f"FBImostwanteddata: {self.name} {self.photos} {self.posters} {self.aliases} {self.description} " \
               f"{self.date_ofbirth} {self.place_ofbirth} {self.hair} {self.eyes} {self.height_min} {self.height_max} " \
               f"{self.weight} {self.build} {self.sex} {self.race_raw} {self.nationality} {self.languages} {self.remarks} " \
               f"{self.reward} {self.caution} {self.warning}"

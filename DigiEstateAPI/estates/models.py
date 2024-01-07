from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Estatedata(models.Model):
    def __str__(self):
        return self.estate_name
    

    first_name_of_estate_representative = models.CharField(max_length=100)
    last_name_of_estate_representative = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    picture = models.ImageField(upload_to='Images', default="Images/None/Noimg.jpg", height_field=None, width_field=None, max_length=100)
    estate_name = models.CharField(max_length=100)
    estate_location = models.CharField(max_length=100)
    excos = models.BooleanField()
    number_of_excos = models.IntegerField()
    estate_worker = models.BooleanField()
    number_of_estate_workers = models.IntegerField()
    residents = models.BooleanField()
    number_of_residents = models.IntegerField()
    # payment_service = models.BooleanField()
    # video_conference = models.BooleanField()
    # chat_forum = models.BooleanField()
    # calendar = models.BooleanField()

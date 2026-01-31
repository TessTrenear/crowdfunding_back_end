from django.db import models
from django.contrib.auth import get_user_model #import user function > set as a config item in crowdfunding>models. During project, django recommends user model don't import direct use helper function to find it for you.

#Create your models here.
class Fundraiser(models.Model): 
    title = models.CharField(max_length=200) #CharField is CLASS we are calling. All rest are function calls. Title field should accept characters - attribute names, define DB table > create title column, goal column etc.
    description = models.TextField() #TextField > data types of the columns > can be as long as you want
    goal = models.IntegerField() #number >
    image = models.URLField() # URLS > address of photo, not storing image in DB directly, only store URL. Don't store images in DB, store images in other location
    is_open = models.BooleanField() # true or false
    date_created = models.DateTimeField(auto_now_add=True) #contain date and time > auto_now_add = sets the field for you
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, #delete linked models. All linked pledges will be deleted. Delete fundraisers as well as user is deleted > a product decision.
        related_name='owned_fundraisers' #django user models special > django relies on user models to do a range of things. User Model is only one configurable in crowdfunding>settings
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser', #send name of Class Foreign key is on. Auto user primary key for Fundraiser class.
        on_delete=models.CASCADE, #what to do DELETE > on delete of a FUNDRAISER cascade > finds all pledges to all that fundraiser and delete the pledges. Stops bad data.
        related_name='pledges' #special property allow you to access all pledges for that fundraiser > by using a special property. Don't need to query the pledges table, DJANGO will do it on our
    )   
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, #an event, on a delete event > delete user, what do we do with pledges > pledges get deleted
        related_name='pledges'
    )

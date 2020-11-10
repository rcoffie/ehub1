from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.


class PublishedAds(models.Manager):

  def get_queryset(self):
    return super().get_queryset().filter(status='pulish')
    
class Ad(models.Model):


  Trending=(
    ('New','New'),
    ('Hot','Hot'),
    ('Normal','Normal')
    
  )

  Option=(
    ('publish','Publish'),
    ('Pending','Pending')
  )

  Category=(

    ('Mobile Phones','Mobile Phones'),
    ('Mobile Accessories','Mobile Phone Accessories'),
    ('Computer Accessories','Computer Accessories'),
    ('TVs','TVs'),
    ('Cameras & Camcorders','Cameras & Camcorders'),
    ('Audio & MP3', 'Audio & MP3'),
    ('Other Electronics','Other Electronics')


  )

  Region=(
    ('Upper West','Upper West'),
    ('Upper East','Upper East'),
    ('North East','North East'),
    ('Northen','Northen'),
    ('Savannah','Savannah'),
    ('Bono East','Bono East'),
    ('Brong Ahafo','Brong Ahafo'),
    ('Oti','Oti'),
    ('Ahafo','Ahafo'),
    ('Ashanti','Ashanti'),
    ('Volta','Volta'),
    ('Greater Accra','Greater Accra'),
    ('Western North','Western North'),
    ('Western','Western'),
    ('Eastern','Eastern'),
    ('Central','Central'),

  )
  
  Condition=(

    ('Used','Used'),
    ('New','New'),
    


  )

  

  title = models.CharField(max_length=100)
  seller = models.ForeignKey(User, on_delete= models.DO_NOTHING)
  location = models.CharField(max_length=100)
  region = models.CharField(max_length=100, choices=Region)
  category = models.CharField(max_length=100, choices=Category)
  trending = models.CharField(max_length=100, choices=Trending,null=True, default='Normal')
  status  = models.CharField(max_length=100, choices=Option,null=True, default='Pending')
  condition = models.CharField(max_length=100, choices=Condition, null=True)
  price = models.IntegerField()
  brand = models.CharField(max_length=200)
  negotiable = models.BooleanField(default=False)
  main_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
  description = models.TextField()
  date_posted = models.DateField(default=datetime.now)
 # objects = PublishedAds()


  class Meta:
    ordering = ['-date_posted']


  def __str__(self):
    return self.title


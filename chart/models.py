from django.db import models

# Create your models here.
class people (models.Model):
    title = models.CharField(max_length = 30)
    
    name = models.CharField(max_length = 30)
    
    biography = models.TextField(max_length = 1000)
    
    images = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    
    images1 = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    
    images2 = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    
# null=True)
    #date_created = models.DateTimeField(auto_now_add=True, null=True)
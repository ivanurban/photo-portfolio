from django.db import models

# Create your models here.
class Images(models.Model):
    alt = models.CharField(max_length=100)
    link = models.CharField(max_length=400, default=None,blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',  default=None,blank=True, null=True)

    

    def __str__(self):
        return self.alt
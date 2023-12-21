from django.db import models


# Create your models here.
class PropertiesDetails(models.Model):
    propertyName = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    location = models.CharField(max_length=50, default="Dubai")
    project = models.CharField(max_length=90, blank=True)
    unitType = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    carParking = models.IntegerField()
    unitSize = models.IntegerField()
    propertyPhoto1 = models.ImageField(upload_to="images/")
    propertyPhoto2 = models.ImageField(upload_to="images/", default="")
    propertyPhoto3 = models.ImageField(upload_to="images/", default="")
    propertyPhoto4 = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.propertyName

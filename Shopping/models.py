from django.db import models
# Create your models here.
class Kitchen(models.Model):
    Name = models.CharField(max_length=25)
    Image = models.ImageField('images/')
    Price = models.IntegerField()
    Discount = models.IntegerField()

    def __str__(self):
        return self.Name

class Household(models.Model):
    Name = models.CharField(max_length=25)
    Image = models.ImageField('images/')
    Price = models.IntegerField()
    Discount = models.IntegerField()


    def __str__(self):
        return self.Name
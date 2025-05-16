from django.db import models

# Create your models here.
class hobbies(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def _str_(self):
        return self.name # esto es para que se muestre el nombre del hobby en el admin de django

class cryptoFacts(models.Model):
    title =  models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def _str_(self):
        return self.title
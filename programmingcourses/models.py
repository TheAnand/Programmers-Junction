from django.db import models

# Create your models here.

class Contactus(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.EmailField(max_length=100,default="")
    message=models.CharField(max_length=1000,default="")
    mobile_number=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name



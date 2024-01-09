from django.db import models

# Create your models here.
 


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
      return f"{self.firstname} {self.lastname}"  

class Court(models.Model):  
    COURT_TYPE = [
        ("G", "草地"),
        ("H", "硬地"),
        ("N", "泥地"),
        ("D", "地毯"),
    ]
    courtname = models.CharField(max_length=100)
    courttype = models.CharField(max_length=1, 
                                 choices=COURT_TYPE)
    city = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.courtname} {self.courttype}" 
  

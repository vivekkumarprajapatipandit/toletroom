from django.db import models

class rentar(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    add=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    dist=models.CharField(max_length=200)
    images=models.ImageField(upload_to="media/")
    
    
class details(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Username  = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    Mnumber = models.CharField(max_length=10)



class contact_team(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Email = models.EmailField()
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    M_No = models.CharField(max_length=15)  # Adjust max_length as necessary

    def __str__(self):
        return self.Name

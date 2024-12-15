from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField("Name",max_length=50,blank=False)
    smobile = models.CharField("Mobile",max_length = 10)
    semail = models.CharField("Email",max_length = 50)
    spassword = models.CharField("Password",max_length = 50)
    createAt = models.DateTimeField("Created",auto_now_add=True)
    
    def __str__(self):
        return self.sname
    
class employee(models.Model):
    ename = models.CharField("Name",max_length=50,blank=False)
    emobile = models.CharField("Mobile",max_length=10)
    eemail = models.CharField("Email",max_length=50)
    epassword = models.CharField("Password",max_length=50)
    createAt = models.DateTimeField("Created",auto_now_add=True)
    
    def __str__(self):
        return self.ename
    
    
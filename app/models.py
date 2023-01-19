from django.db import models

# Create your models here.
class employee(models.Model):
    snum=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    mobile=models.IntegerField()
    deptid=models.IntegerField()

    def __str__(self):
           return self.name

class dept(models.Model):
    deptid=models.OneToOneField(employee, on_delete=models.CASCADE)
    deptlocation=models.CharField(max_length=15)

    def __str__(self):
        return self.deptlocation
    
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Student_Lvl(models.Model):
    Level_ID = models.IntegerField(primary_key=True)
    kyu_level = models.CharField(max_length=50)
    belt_color = models.CharField(max_length=50)
    kata_name = models.CharField(max_length=50)
    kata_image = CloudinaryField('image', default='placeholder')
    syllabus_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-kyu_level"]

    def __str__(self):
        return self.kyu_level


class Student_info(models.Model):
    Student_ID = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Date_of_birth = models.DateField()
    Email = models.EmailField(max_length=50)
    Address_1 = models.CharField(max_length=50)
    Address_2 = models.CharField(max_length=50, null=True)
    Post_code = models.CharField(max_length=10)
    Content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    Student_Grade = models.ForeignKey(Student_Lvl, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-Student_ID"]  # "Student_ID"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Modify the string representation
from django.db import models

# Create your models here.

# DB fileld models - department
class Departments(models.Model):
    dep_image = models.ImageField(upload_to='departments')
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    
# for doctors registering
class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return "Dr " + self.doc_name + " (" + self.doc_spec + ")"

# appointment booking  
class Booking(models.Model):
    pat_name = models.CharField(max_length=255, null=True) 
    pat_age = models.IntegerField(null=True)
    pat_phone = models.CharField(max_length=255, null=True)
    pat_email = models.EmailField(null=True)
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True)
    book_date = models.DateField(null=True)
    booked_on = models.DateField(auto_now=True)

    
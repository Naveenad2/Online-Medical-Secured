from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):

    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    doctor_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=50)
    specialization = models.CharField(max_length=40)
    age = models.IntegerField()
    qualification = models.CharField(max_length=200)
    hospital = models.CharField(max_length=200)
    phoneno =models.IntegerField()


    def __str__(self):
        return self.doctor_name
    
class Patient(models.Model):

    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    patient_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    
    age = models.IntegerField()
    blood_group = models.CharField(max_length=20)
    
    def __str__(self):
        return self.patient_name
    
class Consultation(models.Model):

    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    message  = models.CharField(max_length=100,null=True)
    hospital =  models.CharField(max_length=100,null=True)

    assainged_time = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.Patient.patient_name
    




from django.db import models

# Create your models here.

class Patient(models.Model):
    # SECTOR = [('',''), ('Administrative sector', 'Administrative sector'), ('Service Sector', 'Service Sector')]
    # ROLE = [('',''), ('Admin', 'Admin'), ('Accountaint', 'Accountaint'), ('HR', 'HR'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Helper', 'Helper'), ('Cleaner','Cleaner'), ('technician', 'technician'), ('pharmacist', 'pharmacist'), ('therapist', 'therapist'), ('physician assistant', 'physician assistant'), ('Surgeon', 'Surgeon'), ('Receiption', 'Receiption'), ('Medical records clerk', 'Medical records clerk'), ('patient assignments', 'patient assignments')]
    GENDER_CHOICES = [('Male','Male'), ('Female', 'Female'), ('Other', 'Other')]
    Insurance = [('yes', 'yes'), ('No', 'No')]
    
    created_at = models.DateTimeField(auto_now_add=True)
    patient_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10) #double column
    birth_date = models.DateField()
    email = models.CharField(max_length=100,unique = True)
    phone = models.CharField(max_length=50)
    full_address = models.CharField(max_length=100)
    insurance = models.CharField(choices=Insurance, max_length=50, default='')
    description = models.CharField(max_length=20)
    facility = models.CharField(max_length=50)
    amount = models.IntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



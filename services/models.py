from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalService(Service):
    pass

class DiagnosticTest(Service):
    pass

class Procedure(Service):
    pass

class LaboratoryService(Service):
    pass

class EmergencyService(Service):
    pass



# from django.db import models

# # Create your models here.

# # class Service(models.Model):

# #     created_at = models.DateTimeField(auto_now_add=True)
# #     service_code = models.CharField(max_length=10)
# #     service_name = models.CharField(max_length=50)
# #     service_category = models.CharField(max_length=10)
# #     amount = models.IntegerField()
# #     description = models.CharField(max_length=20)

# class Service(models.Model):
#     CATEGORY_CHOICES = [
#         ('Medical', 'Medical services'),
#         ('Diagnostic', 'Diagnostic tests'),
#         ('Procedure', 'Procedures and treatments'),
#         ('Laboratory', 'Laboratory services'),
#         ('Emergency', 'Emergency services')
#     ]

#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    


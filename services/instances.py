from .models import *

# Medical services
consultations = MedicalService.objects.create(name='Consultations', description='Medical consultations with doctors')
surgeries = MedicalService.objects.create(name='Surgeries', description='Various surgical procedures')

# Diagnostic tests
x_rays = DiagnosticTest.objects.create(name='X-rays', description='Diagnostic imaging technique')
mris = DiagnosticTest.objects.create(name='MRIs', description='Magnetic Resonance Imaging')
ct_scans = DiagnosticTest.objects.create(name='CT scans', description='Computed Tomography scans')

# Procedures and treatments
chemotherapy = Procedure.objects.create(name='Chemotherapy', description='Chemotherapy treatment')
radiation_therapy = Procedure.objects.create(name='Radiation therapy', description='Radiation therapy treatment')
dialysis = Procedure.objects.create(name='Dialysis', description='Kidney dialysis treatment')
rehabilitation = Procedure.objects.create(name='Rehabilitation services', description='Rehabilitation services for patients')

# Laboratory services
blood_tests = LaboratoryService.objects.create(name='Blood tests', description='Routine blood tests')
urine_tests = LaboratoryService.objects.create(name='Urine tests', description='Urine analysis tests')
microbiology_tests = LaboratoryService.objects.create(name='Microbiology tests', description='Microbiology diagnostic tests')

# Emergency services
emergency_ambulance = EmergencyService.objects.create(name='Emergency ambulance', description='Emergency transportation services')
trauma_care = EmergencyService.objects.create(name='Trauma care', description='Emergency medical care for trauma patients')
emergency_visit = EmergencyService.objects.create(name='Emergency ticket/visit', description='Emergency room visit')


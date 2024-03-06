# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import Patient

# Create Add record form
class AddPatientForm(forms.ModelForm):
    # created_at= models.DateTimeField(auto_now_add=True)
    first_name = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    full_address = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    patient_id = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Patient_ID", "class":"form-control"}), label="")
    gender = forms.ChoiceField(required=True, choices=Patient.GENDER_CHOICES, widget = forms.Select(attrs={"placeholder":"Gender", "class":"form-control"}), label="")
    birth_date = forms.DateField(required=True, widget = forms.DateInput(attrs={"type": "date", "class":"form-control", "placeholder":"Birth Date"}), label="", )
    insurance = forms.ChoiceField(choices=Patient.Insurance, widget = forms.Select(attrs={"placeholder":"insurance", "class":"form-control"}), label="insurance")
    description = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Remarks", "class":"form-control"}), label="")
    facility = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Facility", "class":"form-control"}), label="")
    amount = forms.IntegerField(widget = forms.widgets.NumberInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")

    class Meta:
        model = Patient
        exclude = ("user",)


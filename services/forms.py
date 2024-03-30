from django import forms
from .models import Service

# Create Add record form
class AddPatientForm(forms.ModelForm):

    first_name = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="First Name")

    class Meta:
        model = Service
        exclude = ("user",)


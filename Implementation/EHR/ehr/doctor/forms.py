from django import forms
from patient.models import patient
from doctor.models import report,user,prescription,patient_medicine,patient_rays,patient_analytics
from django.contrib.auth.hashers import make_password

class GetPatianTIDForm (forms.ModelForm):
    class Meta():
        model = user
        fields = ('email_1' , 'New_Password')

class PrescriptionForm (forms.ModelForm):
    class Meta():
        model = prescription
        exclude = ['prescription_id']

class AddmedicenForm (forms.ModelForm):
    class Meta():
        model = patient_medicine
        fields = ('med','number_of_potions','number_of_pills')

class AddRaysForm (forms.ModelForm):
    class Meta():
        model = patient_rays
        fields = ['ray']

class AddanalyticsForm (forms.ModelForm):
    class Meta():
        model = patient_analytics
        fields = ['analy']

from django import forms
from .models import booking

class DateInput(forms.DateInput):
    input_type = 'date'
     


class booking_form(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name' : "patient Name :",
            'p_phone' : "patient phone :",
           ' p_email' : "patient Email :",
            'doc_name' : "doctor Name :",
           ' booking_date' : "Booking Date :"

        }


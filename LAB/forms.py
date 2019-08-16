from django import forms
from .models import Customer, Sample

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'company'] 
        widgets = {
            'First_name' : forms.TextInput(
                attrs={'class': 'field-wrapper'}),
            'Company': forms.TextInput(
                attrs={'class': 'field-wrapper'})
        }   

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['customer', 'sample_id', 'package', 'Fuel']
        widgets = {
            'sample id' : forms.TextInput(
                attrs={'class': 'field-wrapper'}),
                  


        }

class uploadform(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()


from django import forms

class PincodeSearchForm(forms.Form):
    pincode = forms.CharField(max_length=6, required=True, label='Enter Pincode')


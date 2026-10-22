from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

        widgets = {
            'doj': forms.DateInput(attrs={'type': 'date'}),}

    def clean_mobile(self):
        value = self.cleaned_data.get('mobile')
    
        if value:
            value_str = str(value)
            if len(value_str) < 10:
                raise forms.ValidationError("Enter 10 Digit Mobile Number.")
        return value
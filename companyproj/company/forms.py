from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        widgets = {
            "company_name": forms.TextInput(attrs={'class': 'form-control'}),
            "company_address": forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            "about_company": forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            "number_of_employee": forms.NumberInput(attrs={'class': 'form-control'}),
            "company_ceo": forms.TextInput(attrs={'class':'form-control'}),
            "work_mode": forms.Select(attrs={'class': 'form-control'}),
        }

from django import forms
from testapp.models import student
class studentregistration(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
    
    def clean(self):
        cleaned_data =  super().clean()
        name = cleaned_data['name']
        if len(name)<4:
            raise forms.ValidationError("Name must contains atleast 4 character")
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import HouseApplication, LegalService, TenantForm, BlogPost, Job
from django.forms.widgets import SelectDateWidget



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'peer h-8 w-full bg-transparent p-0 placeholder-transparent  focus:outline-none focus:ring-0 sm:text-sm',
        'placeholder': 'Email'
    }))
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ["username", 'last_name', 'email', 'password1', 'password2']




class HouseApplicationForm(ModelForm):
    class Meta:
        model = HouseApplication
        fields = '__all__'
        exclude = ['customer']


class LegalServiceForm(ModelForm):
    class Meta:
        model = LegalService
        fields = '__all__'
        exclude = ['customer']

class BlogPosts(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ['customer']

class TenantForms(forms.ModelForm):
    class Meta:
        model = TenantForm
        fields = '__all__'
        widgets = {
            'date_of_birth': SelectDateWidget(years=range(1900, 2021)),
            'status': forms.HiddenInput(),
        }
    

    def __init__(self, *args, **kwargs):
        super(TenantForms, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'Please select')] + list(self.fields['gender'].choices)
        self.fields['employment'].choices = [('', 'Please select')] + list(self.fields['employment'].choices)


class ApplicationForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
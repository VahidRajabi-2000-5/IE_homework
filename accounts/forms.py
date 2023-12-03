
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields =['username', 'email','first_name', 'last_name', 'phone_number', 'brith_date']
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields =['username', 'email','first_name', 'last_name', 'phone_number', 'brith_date']
        
        
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # user_creation_fields = ['username','email','national_code','phone_number','age','discription', 'first_name', 'last_name']
        # for field_name in user_creation_fields:
        #     self.fields[field_name] = CustomUserCreationForm.base_fields[field_name]
        self.fields.update(CustomUserCreationForm.base_fields)
        self.fields.pop('password2', None)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
            
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.brith_date = self.cleaned_data['brith_date']
        user.save()
        return user
    
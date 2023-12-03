from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','first_name','last_name','brith_date']
    
    add_fieldsets = UserAdmin.add_fieldsets+(
        (None,{'fields':['phone_number','brith_date','first_name','last_name'],}),
        )
    
    
    fieldsets = UserAdmin.fieldsets+(
        (None,{'fields':['phone_number','brith_date'],}),
    )
    
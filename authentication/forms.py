from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
    	model = User
    	fields = ['first_name','last_name','email', 'password1', 'password2']
    def save(self):
        self.instance.username = self.instance.email
        return super(CreateUserForm, self).save()
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

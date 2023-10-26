from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.models import User
from .models import user ,feedback,contact
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




class Feedback(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['Name','Email','Rating','Message']


class Contact(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['Name','Email','Mobile_Number','Message']




# C
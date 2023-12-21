from django import forms
from .models import Main, FirstName, LastName, Patronymic, Street

class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['first_name', 'last_name', 'patronymic', 'street', 'house', 'building', 'apartment', 'phone']
        
class FirstNameForm(forms.ModelForm):
    class Meta:
        model = FirstName
        fields = ['value']

class LastNameForm(forms.ModelForm):
    class Meta:
        model = LastName
        fields = ['value']

class PatronymicForm(forms.ModelForm):
    class Meta:
        model = Patronymic
        fields = ['value']

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['value']

class DeleteForm(forms.Form):
    data = forms.CharField(max_length=30)



class MainEditForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['first_name', 'last_name', 'patronymic', 'street', 'house', 'building', 'apartment', 'phone']

    

from django import forms

class RegisterForm(forms.forms):
    firstname=forms.charField(label="enter firstname",max_length=150)
    lastname=forms.charField(label="enter lastname",max_length=150)
    age=forms.intergerField
    address = forms.CharField(label="enter address",max_length=250)

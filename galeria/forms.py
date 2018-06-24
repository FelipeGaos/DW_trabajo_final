from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from galeria.models import Usuario, Galeria, Foto


class SingUpForm(UserCreationForm):
    class Meta:
        model= Usuario

        fields=[
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'edad',
            'imagen',
        ]
        labels={
            'username':'Usuario',
            'password1':'Contraseña',
            'password2':'Vuelva a introducir contraseña',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'edad':'Edad',
            'imagen':'Foto de perfil',

        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
        }

    def save(self,commit=True):
        user=super(SingUpForm,self).save(commit=False)

        if commit:
            user.save()
        return user

class CrearGaleria(forms.ModelForm):
    class Meta:
        model= Galeria

        fields=[
            'nombre',
            'descripcion',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripción',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }

    def save(self,commit=True):
        galeria=super(CrearGaleria,self).save(commit=False)
        if commit:
            galeria.save()
        return galeria

class CrearFoto(forms.ModelForm):
    class Meta:
        model= Foto

        fields=[
            'imagen',
            'fecha',
            'descripcion',
        ]
        labels={
            'imagen':'Nombre',
            'fecha':'Fecha',
            'descripcion':'Descripción',
        }
        widgets={
            'fecha':forms.DateInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }

    def save(self,commit=True):
        foto=super(CrearFoto,self).save(commit=False)
        if commit:
            foto.save()
        return foto

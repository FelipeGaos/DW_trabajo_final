from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from galeria.forms import SingUpForm, CrearGaleria, CrearFoto
from galeria.models import Usuario, Galeria, Foto

# Create your views here.
def UsuarioCrear(request):
    template_name=''

    if request.method=='POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            request.session['id']=user.id
            return HttpResponseRedirect(reverse(''))

    else:
        form=SingUpForm()

    return render(request,template_name,{'form':form})

def GaleriaCrear(request):
    id_usuario=request.session.get('id')
    template_name=''

    if request.method=='POST':
        form = CrearGaleria(request.POST)
        if form.is_valid():
            galeria=form.save()
            Galeria.objects.filter(id=galeria.id).update(usuario=Usuario.objects.get(id=id_usuario))
            return HttpResponseRedirect(reverse(''))
    else:
        # borrar usuario
        form=CrearGaleria()

    return render(request,template_name,{'form':form})

def FotoCrear(request, id_galeriar):
    id_usuario=request.session.get('id')
    template_name=''

    if request.method=='POST':
        form = CrearFoto(request.POST)
        if form.is_valid():
            foto=form.save()
            Foto.objects.filter(id=foto.id).update(usuario=Usuario.objects.get(id=id_usuario), galeria=Galeria.objects.get(id=id_galeriar))
            return HttpResponseRedirect(reverse(''))
    else:
        # borrar usuario
        form=CrearFoto()

    return render(request,template_name,{'form':form})

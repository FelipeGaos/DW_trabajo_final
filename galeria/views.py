# Redireccion:
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse

# Usuario y mensajes
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Modelos y Forms
from galeria.forms import SingUpForm, CrearGaleria, CrearFoto
from galeria.models import Usuario, Galeria, Foto

# Paginacion de resultados:
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Bienvenida(request):
    logout(request)
    template_name='base/index.html'
    data={}
    return render(request,template_name,data)

def UsuarioCrear(request):
    template_name='usuarios/registro.html'

    if request.method=='POST':
        form = SingUpForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            # request.session['id']=user.id
            return HttpResponseRedirect(reverse('bienvenida'))
        else:
            print('no valido')

    else:
        form=SingUpForm()

    return render(request,template_name,{'form':form})

def UsuarioEditar(request, id_usuario):
    template_name='usuarios/editar.html'
    usuario= Usuario.objects.get(id=id_usuario)
    if request.method=='GET':
        form=SingUpForm(instance=usuario)
    else:
        form = SingUpForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listarUsuario'))
    return render(request, template_name,{'form':form})

def login_usuario(request):
    template_name='usuarios/login.html'
    data={}

    logout(request)
    username=password=''
    if request.POST:
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            if user.is_active:

                request.session['id']=user.id
                login(request, user)

                return HttpResponseRedirect(reverse('listarGaleria'))
            else:
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )

    return render(request, template_name,data)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def GaleriaCrear(request):
    id_usuario=request.session.get('id')
    template_name='galerias/agregar.html'

    if request.method=='POST':
        form = CrearGaleria(request.POST, request.FILES)
        if form.is_valid():
            galeria=form.save()
            Galeria.objects.get(id=galeria.id).usuario.add(Usuario.objects.get(id=id_usuario))
            # Galeria.objects.filter(id=galeria.id).update(usuario=Usuario.objects.get(id=id_usuario))
            return HttpResponseRedirect(reverse('listarGaleria'))
    else:
        # borrar usuario
        form=CrearGaleria()

    return render(request,template_name,{'form':form})

def GaleriaEditar(request, id_galeria):
    template_name='galerias/editar.html'
    galeria= Galeria.objects.get(id=id_galeria)
    if request.method=='GET':
        form=CrearGaleria(instance=galeria)
    else:
        form = CrearGaleria(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listarGaleria'))
    return render(request, template_name,{'form':form})

def VerMiembros(request, id_galeria):
    template_name='fotos/agregarMiembro.html'
    data=Usuario.objects.all()
    idGaleria=id_galeria

    return render(request,template_name,{'lista_objetos':data, 'idGaleria':idGaleria})

def AgregarMiembro(request, id_galeria, id_usuario):
    galeria=Galeria.objects.get(id=id_galeria).usuario.add(Usuario.objects.get(id=id_usuario))
    idGaleria=id_galeria

    return HttpResponseRedirect(reverse('listarFoto',kwargs={'id_galeria':id_galeria}))

def EliminarMiembro(request, id_galeria, id_usuario):
    Galeria.objects.get(id=id_galeria).usuario.remove(Usuario.objects.get(id=id_usuario))
    idGaleria=id_galeria

    if Galeria.objects.filter(usuario=None):
        print("galeria vacia")
        Galeria.objects.filter(id=id_galeria).delete()
        return HttpResponseRedirect(reverse('listarGaleria'))
    else:
        return HttpResponseRedirect(reverse('listarFoto',kwargs={'id_galeria':id_galeria}))


def FotoCrear(request, id_galeria):
    id_usuario=request.session.get('id')
    template_name='fotos/agregar.html'

    if request.method=='POST':
        form = CrearFoto(request.POST, request.FILES)
        if form.is_valid():
            foto=form.save()
            Foto.objects.filter(id=foto.id).update(usuario=Usuario.objects.get(id=id_usuario), galeria=Galeria.objects.get(id=id_galeria))
            return HttpResponseRedirect(reverse('listarFoto',kwargs={'id_galeria':id_galeria}))
    else:
        # borrar usuario
        form=CrearFoto()

    return render(request,template_name,{'form':form})

def FotoEditar(request, id_foto, id_galeria):
    id_usuario=request.session.get('id')
    template_name='fotos/editar.html'
    foto= Foto.objects.get(id=id_foto)
    if request.method=='GET':
        form=CrearFoto(instance=foto)
    else:
        form = CrearFoto(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            foto=form.save()
            Foto.objects.filter(id=foto.id).update(usuario=Usuario.objects.get(id=id_usuario), galeria=Galeria.objects.get(id=id_galeria))
            return HttpResponseRedirect(reverse('listarFoto',kwargs={'id_galeria':id_galeria}))
    return render(request, template_name,{'form':form})

def UsuarioListar(request):
    data = {}
    data=Usuario.objects.all()
    page=request.GET.get('page',1)
    paginator=Paginator(data,10)

    try:
        lista_objetos=paginator.page(page)
    except PageNotAnInteger:
        lista_objetos=paginator.page(1)
    except EmptyPage:
        lista_objetos=paginator.page(paginator.num_pages)

    template_name='usuarios/listar.html'

    return render(request, template_name,{'lista_objetos':lista_objetos})

def GaleriaListar(request):
    id_usuario=request.session.get('id')

    data = {}
    try:
        data=Galeria.objects.filter(usuario=id_usuario)
    except Galeria.DoesNotExist:
        data=None



    if data!=None:
        print(len(data))
        page=request.GET.get('page',1)
        paginator=Paginator(data,10)

        try:
            lista_objetos=paginator.page(page)
        except PageNotAnInteger:
            lista_objetos=paginator.page(1)
        except EmptyPage:
            lista_objetos=paginator.page(paginator.num_pages)
    else:
        lista_objetos=data

    template_name='galerias/listar.html'

    return render(request, template_name,{'lista_objetos':lista_objetos})

def FotoListar(request, id_galeria):
    idGaleria={}
    idGaleria=id_galeria
    usuarios={}
    usuarios=Galeria.objects.get(id=id_galeria).usuario.all()
    data = {}
    try:
        data=Foto.objects.filter(galeria=id_galeria)
    except Galeria.DoesNotExist:
        data=None


    if data!=None:
        print(len(data))
        page=request.GET.get('page',1)
        paginator=Paginator(data,10)

        try:
            lista_objetos=paginator.page(page)
        except PageNotAnInteger:
            lista_objetos=paginator.page(1)
        except EmptyPage:
            lista_objetos=paginator.page(paginator.num_pages)
    else:
        lista_objetos=data

    template_name='fotos/listar.html'

    return render(request, template_name,{'lista_objetos':lista_objetos, 'idGaleria':idGaleria, 'usuarios':usuarios})

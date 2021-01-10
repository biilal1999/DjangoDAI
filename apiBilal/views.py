from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from apiBilal.models import Libro, Prestamo
from apiBilal.forms import LibroForm, PrestamoForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.


def validarDatosLibro(titulo, autor):
    if titulo != "" and autor != "" and titulo.isalpha() and autor.isalpha():
        return True

    else:
        return False


def validarTitulo(titulo):
    if titulo != "" and titulo.isalpha():
        return True

    else:
        return False


def validarAutor(autor):
    if autor != "" and autor.isalpha():
        return True

    else:
        return False


def index(request):
    #return HttpResponse('Hello World')
    return render(request, 'index.html')


@staff_member_required(login_url="http://localhost:8000/authError")
def nuevolibro(request):
    form = LibroForm
    context = {'titulo': "Nuevo libro", 'ruta': "../addlibro", 'form': form, 'msg': "Nuevo libro"}
    return render(request, 'formulario.html', context)


@staff_member_required(login_url="http://localhost:8000/authError")
def addlibro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            tupla = form.save(commit=False)
            tupla.save()

            form = LibroForm
            context = {'titulo': "Nuevo libro", 'mensaje': "Se ha añadido el libro", 'ruta': "../addlibro", 'form': form, 'msg': "Nuevo libro"}

            return render(request, 'formulario.html', context)


@staff_member_required(login_url="http://localhost:8000/authError")
def accioneslibro(request):
    if request.method == "POST":
        accion = request.POST.get('accion')
        tit = request.POST.get('tit')
        aut = request.POST.get('aut')
        form = LibroForm

        if accion == "editar":
            # Deberia rescatar los valores de titulo y autor de la base de datos a partir del id del libro
            context = {'titulo': "Editar libro", 'ruta': "../modlibro", 'form': form, 'tit': tit, 'aut': aut, 'msg': "Modificando libro"}
            return render(request, 'formulario.html', context)


        if accion == "borrar":
            l = Libro.objects.filter(titulo=tit, autor=aut)
            l.delete()
            todos = Libro.objects.all()
            context = {'libros': todos}

            return render(request, 'listalibros.html', context)


@staff_member_required(login_url="http://localhost:8000/authError")
def modlibro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        titAntiguo = request.POST.get('titantiguo')
        autAntiguo = request.POST.get('autantiguo')
        titNuevo = request.POST.get('titulo')
        autNuevo = request.POST.get('autor')

        if form.is_valid():
            Libro.objects.filter(titulo=titAntiguo, autor=autAntiguo).update(titulo=titNuevo, autor=autNuevo)

            todos = Libro.objects.all()
            context = {'libros': todos}
            #context = {'mensaje': "Se ha modificado el libro", 'form': form}

            return render(request, 'listalibros.html', context)




@login_required(login_url="http://localhost:8000/authError")
def nuevoprestamo(request):
    form = PrestamoForm
    context = {'titulo': "Nuevo préstamo", 'ruta': "../addprestamo", 'form': form, 'msg': "Nuevo préstamo", 'pres': ""}
    return render(request, 'formulario.html', context)



@login_required(login_url="http://localhost:8000/authError")
def addprestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)

        if form.is_valid():
            tupla = form.save(commit=False)
            tupla.usuario = request.user
            tupla.save()

            form = PrestamoForm
            context = {'titulo': "Nuevo préstamo", 'mensaje': "Se ha realizado el préstamo", 'ruta': "../addprestamo", 'form': form, 'msg': "Nuevo préstamo", 'pres': ""}

            return render(request, 'formulario.html', context)




@login_required(login_url="http://localhost:8000/authError")
def accionesprestamo(request):
    if request.method == "POST":
        accion = request.POST.get('accion')
        usu = request.POST.get('usu')
        lib = request.POST.get('lib')
        iden = request.POST.get('id')
        form = PrestamoForm

        if accion == "editar":
            # Deberia rescatar los valores de titulo y autor de la base de datos a partir del id del libro

            context = {'titulo': "Editar préstamo", 'ruta': "../modprestamo", 'form': form, 'usu': usu, 'lib': lib, 'iden': iden, 'msg': "Modificando préstamo"}
            return render(request, 'formulario.html', context)


        if accion == "borrar":
            p =  Prestamo.objects.filter(libro=iden, usuario=usu)
            p.delete()
            todos = Prestamo.objects.all()
            context = {'prestamos': todos}

            return render(request, 'listaprestamos.html', context)


@login_required(login_url="http://localhost:8000/authError")
def modprestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        libAntiguo = request.POST.get('iden')
        usuAntiguo = request.POST.get('usuantiguo')
        libNuevo = request.POST.get('libro')
        usuNuevo = request.POST.get('usuantiguo')

        if form.is_valid():
            Prestamo.objects.filter(libro=libAntiguo, usuario=usuAntiguo).update(libro=libNuevo, usuario=usuNuevo)

            todos = Prestamo.objects.all()
            form = PrestamoForm
            context = {'prestamos': todos, 'form': form}

            return render(request, 'listaprestamos.html', context)



def verlibros(request):
    todos = Libro.objects.all()

    context = {'libros': todos}
    return render(request, 'listalibros.html', context)




def verprestamos(request):
    todos = Prestamo.objects.all()

    context = {'prestamos': todos}
    return render(request, 'listaprestamos.html', context)



def authError(request):
    return render(request, 'autherror.html', {})


def logout(request):
    response = HttpResponseRedirect('http://localhost:8000/')
    response.delete_cookie('sessionid')

    return response


def test_template(request):
    context = {}                # Aquí van las variables para la plantilla
    return render(request, 'test.html', context)

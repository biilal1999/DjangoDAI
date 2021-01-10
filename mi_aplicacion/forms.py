from django.forms import ModelForm
from mi_aplicacion.models import Libro, Prestamo


class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']


class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'usuario']

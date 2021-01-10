from django.forms import ModelForm
from apiBilal.models import Libro, Prestamo


class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']


class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro']


class PrestamoModForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['usuario']

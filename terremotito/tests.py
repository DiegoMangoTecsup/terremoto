from django.test import TestCase
from .models import *

# Create your tests here.
from terremotito.models import Usuario
def test_user_creation():
    user=Usuario.objects.all(
        usuario='dy',
        correo = 'd@gamil.com',
        clave='123'
    )
    assert user.Usuario == 'dy'
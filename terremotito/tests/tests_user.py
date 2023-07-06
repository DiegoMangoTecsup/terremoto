import pytest
from terremotito.models import Usuario
def test_user_creation():
    user=Usuario.objects.all(
        usuario='dy',
        correo = 'd@gamil.com',
        clave='123'
    )
    assert user.Usuario == 'dy'
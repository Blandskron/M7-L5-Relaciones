import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relaciones.settings')
django.setup()

from muchos_a_uno.models import Region, Estado
from muchos_a_muchos.models import Cliente, Producto, Compra
from uno_a_uno.models import Trabajador, Curriculum
from datetime import date

# Poblar tablas de Relaciones Muchos a Uno
def poblar_muchos_a_uno():
    region1 = Region.objects.create(nombre="Región Metropolitana")
    region2 = Region.objects.create(nombre="Región de Valparaíso")

    Estado.objects.create(nombre="Santiago", region=region1)
    Estado.objects.create(nombre="Puente Alto", region=region1)
    Estado.objects.create(nombre="Valparaíso", region=region2)
    Estado.objects.create(nombre="Viña del Mar", region=region2)

    print("Tablas de Relaciones Muchos a Uno pobladas con éxito.")

# Poblar tablas de Relaciones Muchos a Muchos
def poblar_muchos_a_muchos():
    cliente1 = Cliente.objects.create(nombre="Juan Pérez")
    cliente2 = Cliente.objects.create(nombre="Ana López")
    cliente3 = Cliente.objects.create(nombre="Carlos Gómez")

    producto1 = Producto.objects.create(nombre="Producto A")
    producto2 = Producto.objects.create(nombre="Producto B")
    producto3 = Producto.objects.create(nombre="Producto C")

    Compra.objects.create(cliente=cliente1, producto=producto1, fecha=date(2023, 12, 1))
    Compra.objects.create(cliente=cliente1, producto=producto2, fecha=date(2023, 12, 5))
    Compra.objects.create(cliente=cliente2, producto=producto3, fecha=date(2023, 12, 10))
    Compra.objects.create(cliente=cliente3, producto=producto1, fecha=date(2023, 12, 15))

    print("Tablas de Relaciones Muchos a Muchos pobladas con éxito.")

# Poblar tablas de Relaciones Uno a Uno
def poblar_uno_a_uno():
    trabajador1 = Trabajador.objects.create(nombre="Luis Martínez")
    trabajador2 = Trabajador.objects.create(nombre="María Torres")

    Curriculum.objects.create(trabajador=trabajador1, documento="Curriculum de Luis Martínez")
    Curriculum.objects.create(trabajador=trabajador2, documento="Curriculum de María Torres")

    print("Tablas de Relaciones Uno a Uno pobladas con éxito.")

# Ejecutar el script
if __name__ == "__main__":
    poblar_muchos_a_uno()
    poblar_muchos_a_muchos()
    poblar_uno_a_uno()
    print("¡Datos iniciales cargados con éxito!")

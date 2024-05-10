# convierte desde python a objeto JSON para envio y respuesta de las consultas a los modelos
from rest_framework import serializers
from .models import Marca, Producto

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # Define un campo para representar la marca asociada
    marca = MarcaSerializer(read_only=True)  # Usa read_only=True para campos relacionales anidados

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'marca']


# convierte desde python a objeto JSON para envio y respuesta de las consultas a los modelos
from rest_framework import serializers
from .models import Marca, Producto

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = '__all__'


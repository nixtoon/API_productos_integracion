from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MarcaSerializer, ProductoSerializer
from .models import Marca, Producto

# Create your views here.

# views de productos

# get all products
@api_view(['GET']) 
def getProductos(request):
  productos = Producto.objects.all()
  serializer = ProductoSerializer(productos, many=True)
  return Response(serializer.data)

# get single product
@api_view(['GET'])
def getProducto(request, pk):
  producto = Producto.objects.get(id=pk)
  serializer = ProductoSerializer(producto, many=False)
  return Response(serializer.data)

# add product
@api_view(['POST'])
def addProducto(request):
  serializer = ProductoSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)

# update product
@api_view(['PUT'])
def updateProducto(request, pk):
  producto = Producto.objects.get(id=pk)
  serializer = ProductoSerializer(instance=producto, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# delete product
@api_view(['DELETE'])
def deleteProducto(request, pk):
  producto = Producto.objects.get(id=pk)
  producto.delete()

  return Response('Item eliminado')


# views de marca

# get all marcas
@api_view(['GET']) 
def getMarcas(request):
  marcas = Marca.objects.all()
  serializer = MarcaSerializer(marcas, many=True)
  return Response(serializer.data)

# add marca
@api_view(['POST'])
def addMarca(request):
  serializer = MarcaSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)
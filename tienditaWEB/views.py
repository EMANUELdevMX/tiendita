from django.shortcuts import render,get_object_or_404

# Create your views here.
"""VISTAS PARA EL CATALOGO DEL PRODUCTO """

from . models import Categoria,Producto

def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    print(listaProductos)
    context = {

        'productos':listaProductos,
        'categorias':listaCategorias
    }
    return render(request,'index.html',context)

def productosPorCategoria(request,categoria_id):
    """vista para filtrar productos por categoria"""

    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()

    listaCategorias = Categoria.objects.all()

    context = {
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)

def productosPorNombre(request):
    """lista para filtrado de prpoductos por nombres"""
    nombre = request.POST['nombre']

    listaProductos = Producto.objects.filter(nombre__contains=nombre)
    listaCategorias = Categoria.objects.all()

    context = {
        'categorias':listaCategorias,
        'productos':listaProductos


    }
    return render(request,'index.html',context)


def productoDetalle(request,producto_id):
    """vista para el detalle del producto """

    #objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)

    context= {
        'producto':objProducto
    }

    return render(request,'producto.html',context)
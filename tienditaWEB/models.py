from django.db import models

# aque se van a creear los modelos que va a tener las clases que se van a tener en los productos  y categorias 

class Categoria (models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Producto (models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)

    def __str__(self):
        return self.nombre
    

from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    dni = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1,default='M')
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.dni


class Pedido(models.Model):


    ESTADO_CHOISES = (
        ('0' , 'Solicitado'),
        ('1' , 'Pagado')

    )


    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=20,null=True)
    monto_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado = models.CharField(max_length=1,default='0')

    def __str__(self):
        return self.nro_pedido

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.producto.nombre
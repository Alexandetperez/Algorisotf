from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name = 'tipos'
        ordering = ['id']
       
class category(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name = 'categoria'
        ordering = ['id']


class employee(models.Model):
    categ = models.ManyToManyField(category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    cedula = models.CharField(max_length=10,unique=True, verbose_name='Cedula')
    date_joines = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    saley = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d',null=True , blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d',null=True , blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'empleado'
        verbose_name = 'empleados'
        db_table = 'empleado'
        ordering = ['id']
        



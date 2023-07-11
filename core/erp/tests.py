from config.wsgi import *
from core.erp.models import Type, employee

#Listar 

#select * from tabla 
#query =Type.objects.all()
#print(query)

#insercion 

#t=Type()
#t.name = 'presidente'
#t.save()

#edicion

#t=Type.objects.get(id=1)
#print(t.name)

#edicion
#try:
# t=Type.objects.get(pk=1)
 #t.name = 'Accionista'
 #t.save()
#except Exception as e:
 # print(e)

#eliminacion 
#t = Type.objects.get(pk=1)
#t.delete()

#obj=Type.objects.filter(name__contains='p').count()
#print(obj)

employee=Type.objects.filter(Type)

for i in Type.objects.filter():
    print(i.name)
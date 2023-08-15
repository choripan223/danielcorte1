print('figuras validas: \n',\
    '1. calcula el are de un circulo \n',\
         '2. calcula el area de un rectangulo\n',\
             '3. triangulo')
fig=input('igrasar la maldita figura para calcular area')
a='NaN'
if (fig=='circulo'):
    r=int(input('ingrese el valor del radio'))
    a=3.1416*r**2
elif(fig=='rectangulo'):
    b=int(input('ingrese el valor de la base'))
    h=int(input('ingrese el valor de la altura'))
    a=b*h
elif(fig=='triangulo'):
    b=int(input('ingrese el valor de la base'))
    h=int(input('ingrese el valor de la altura'))
    a=b*h/2
else:print('ingreso invalido') 
print('el valor del area es: ',a)   
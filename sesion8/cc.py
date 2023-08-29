import random as r

def app():
    pal=''
    nombre='que ponemos'
    while pal !='exit':
        
      #x=r.randint(100,180)
      x=r.choice(nombre)
      print(x)
      pal=input('para saleri escriba exit')

if __name__=="__main__":
    app()


    #radint para los enteros aleatorios



    #uniforme par numeros decimales
def agregar(milista):
    num=int(input('que numero desea agregar:'))
    milista.append(num)
    print(milista)

def insertar(milista):
    var=int(input('que numeor quiere agregar:'))
    idx=int(input('en que posicion:'))  
    milista.insert(idx,var) 
    print(milista)


def borrar(milista):
    milista.clear()
    print(milista)
def remover(milista):
    milista.remove(var)
    print(milista)


def main():
    milista=[2,4,7,8]
    opc=''
    while opc!='exit':
        print('selecione una de las siguientes opciones:\n'
          '1. agregar \n 2.insertar \n 3. borrar')
        opc=input('=>')

        if opc =='1':
            agregar(milista)
        elif opc=='2':
            insertar(milista)
        elif opc=='3':
            borrar(milista)    
            



if __name__=='__main__':
    main()
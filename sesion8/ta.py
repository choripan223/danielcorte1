import tt

def main():
    a=int(input('ingresa un numero'))
    b=int(input('ingresa otro numero'))
    r=tt.suma(a,b)
    print(r)
    print(f'ejecutado desde{__name__}')

if __name__=="__main__":
    main()                    
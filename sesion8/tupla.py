
def app(a,*args,**kwargs):
    print(args)
    print(kwargs)


if __name__=="__main__":
    app(1,2,5,7,9,z=56,b=90)

14
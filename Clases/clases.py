import math



class Circulo:
    def __init__(self, radio):
        self.radio = radio
        

    def myArea(self):
        print("El area del circulo es: ", pow(self.radio,2)*math.pi)
    
    def myPerimetro(self):
        print("El perimetro del circulo es: ", 2*math.pi*self.radio)

def main():
    print("inicio")
    flag=True
    while(flag):
        try:
            radio=float(input("Por favor, ingrese el radio del circulo: "))
            if(radio>0):
                myCircle=Circulo(radio)
            myCircle.myArea()
            myCircle.myPerimetro()
            #MULTIPLICACION DEL CIRCULO YA EXISTENTE POR UN VALOR n
            try:
                n=int(input("Desea multiplicar el circulo por un numero n? recuerde que debe ser mayor a 0. Ingrese 0 si no desea multiplicar: "))
                if(n>0):
                    print("radio anterior: ", myCircle.radio, "n: ", n, "radio anterior*n: ", myCircle.radio*n)
                    newCircle=Circulo(myCircle.radio*n)
                    newCircle.myArea()
                    newCircle.myPerimetro()
            except ValueError:
                print("Debe ingresar un numero mayor a 0, no se permite el ingreso de caracteres no numericos")
            except:
                print("Debe ingresar un numero mayor a 0")    
        except ValueError:
            print("Debe ingresar un numero mayor a 0, no se permite el ingreso de caracteres no numericos")
        except:
            print("Debe ingresar un numero mayor a 0")  
        #CONSULTA SI DESEA CONTINUAR UTILIZANDO LA CLASE CIRCULO
        try:
            ex=int(input("ingrese 1 para continuar o cualquier tecla parra terminar: "))
            if(ex==1):
                flag=True
            else:
                flag=False
                print("Gracias")
        except ValueError:
            flag=False
            print("Gracias")
        
        
        
        
    
main()




    
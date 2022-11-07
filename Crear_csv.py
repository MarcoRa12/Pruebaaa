import csv
#Clase libro
class Libro :
    def __init__(self,id,titulo,genero,ibsn,editorial,autor) :
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.ibsn=ibsn
        self.editorial=editorial
        self.autor=autor
    
    
    def __del__(self):
        return "El libro fue elminado"


#Funcion que me reduce mucho para pasarlo a u objeto
def datos_tuplas():
        i=input("Id:")
        t=input("titulo:")
        g=input("genero:")
        s=input("ibsn:")
        e=input("editorial")
        a=input("autor:")
        return i,t,g,s,e,a
#Funcion que me sirve para convertir los atributos del objeto a lista para asi poder guardar en csv 
def Convertira_listas(valore):
    lista=[]
    for i in valore :
        lista.append(i)
    return lista

e=datos_tuplas()
libro_1=Libro(*e)
i=datos_tuplas()
libro_2=Libro(*i)
o=datos_tuplas()
libro_3=Libro(*o)





with open ('libros.csv','w',newline='') as lol :
  lee=csv.writer(lol)
  lee.writerow(Convertira_listas(e))
  lee.writerow(Convertira_listas(i))
  lee.writerow(Convertira_listas(o))




#Ahora crea una funcion que te permita mostrar por pantalla la lista por defecto de los libros


#Primero tienes que abrir el arhivo en modo lectura
import csv
import os 
#Este sito va a ser para colocar las funciones que mas adelante se utilizaran para algunas de las opciones 
#/////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////
#ES la opcion1: Esta funcion sirve para mostrar el texto que se encuentra en el csv ; primero abrimos el archivo en modo lectura para 
#asi poder iterar sobre ella en cada linea mediante un for ;de tal manera que en cada linea me muestre sus valores mediante n[posicion]
def MostrarCsvTexto():
    with open('libros.csv','r',newline='') as archivo :
        leer=csv.reader(archivo)
        for l in leer :
            print(f"\t\t///El id es : {l[0]}///Titulo : {l[1]} ///Genero : {l[2]} ///ISBN : {l[3]} ///Editorial : {l[4]} ///Autor(es):{l[5]}")




#/////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////
#Esta funcion es para la opcion 2 ; esta comprueba si el titulo proporcionado por el usario se encuentra ;
#de ser asi crea una lista para con el titulo agregado ; enc caso no debes agregar abajo en la principal un if con bool para saber si la lista esta vacia ....
def opcion_2(nombtitulo):
    with open ('libros.csv','r',newline="") as archivo :
        leer = csv.reader(archivo)
        #Con el for recorremos cada linea y en este caso ;nos concentraremos en la posicion 1 ya que 
        #ahi se encuentra el titulo
        lista =[] #Aqui se guardaran los libros que existen pero solo sus titulos 
        for i in leer : 
            if i[1] == nombtitulo :
                lista.append(nombtitulo)
            else :
                pass
            
                         
    return lista               
#///Esta funcion tambien es para la opcion dos 
def pa_mo_list(nlista):
    cadena = ""
    for i in nlista:
        if nlista[0] == i :  #Hago estas condiciones para que en el primer valor no me cuente la coma 
          cadena += str(i)
        elif nlista[1]== i:  #Por ende despues del primer valor se podra poner la coma
          cadena +="," + str(i)
    return cadena 
#/////Esta funcion tambien es para la opcion 2 :
def reci_titulo():
    titulo=input("\nIngrese el libro a listar :")
    return titulo




#/////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////
#-----Esta funcion lo que hace es devolverme o retornarme los valores de cada caracteristica de un libro;claro esta que solo sirve para la opcion 3:s
def datos_tuplas():#Esta es para la opcion ---3
        i=input("Id:")
        t=input("titulo:")
        g=input("genero:")
        s=input("ibsn:")
        e=input("editorial:")
        a=input("autor(es) !recuerda que si ingresas mas de un autor debes separarlos por una coma ejemp: n,n !:")
        return i,t,g,s,e,a
#///Esta tambien es para la opcion 3 :Con esta funcion lo que hacemos es crear un objeto de la clase libro para asi poder asi devolver un objeto
#Recuerda que esta funcion recibe como parametro los datos de otra funcion que fueron almacenados en una lista
def Crear_Libro(nvalor):
    #Primero creamos una clase libro para poder hacer este procedimento 
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
    
    Objeto_Creado = Libro(*nvalor)
    return Objeto_Creado




#///Esta es tambien para la funcion3 : Esta sirve para que me devuelva en una lista los atributos de un objeto de clase libro
def Mostrar_los_Atributos(nobjeto):
    i = nobjeto.id
    t = nobjeto.titulo
    g = nobjeto.genero
    s = nobjeto.ibsn   #Si cuando utilizes esta funcion utilzas la otra que es la pa_mo_list;te la transforma en una cadena 
    e = nobjeto.editorial #REcueda que que que esto igualmente lo puedes llamar de acurdo a su posicion ,por emjemplo me refiero a su titulo
    a=  nobjeto.autor
    lista_nueva =[i,t,g,s,e,a]
    return lista_nueva  
            
#Con esta funcion puedo mostrar los las lineas del csv ; en otras palabras los libro ;de esta forma solo se mostra cuando yo lo quiera 
#////////////////////////////////////////
#////////////////////////////////////////

#En esta parte va lo de la opcion 4 .
#Esta funcion lo que hace es recibir lo que el usuario quiera eliminar ;a
#entonces recorre la lista donde se encuentra los objetos creados y si alguna de esta concuerda con lo pedido se eliminara
def EliminarObj(ntitulo,nlista): #Esta funcion recibira por parametro lo que el usuario quiera eliminar ;claro este solo a de poner el titulo.
  y=0 #Contador 
  il=0 #indice
  tipo_objeto_Eliminar =None
  for i in nlista : #Lo que hace el ciclo for es recorrer cada objeto libro;
    if i.titulo == ntitulo :#Asi cuando se encuentre por el objeto pedido por su titulo este sera eliminado
        print("El objeto :",i.titulo,"ha sido eliminado")
        #y = y +1
        il = nlista.index(i) + 1
        tipo_objeto_Eliminar=i #Por alguna razon no me elimina el objeto ; entoncres e de eliminarlo fuera de la fuuncion ;tengo que llevarme le registro de ese oobjeto.
        break
    else :
        pass
        #y = y + 1 #En caso contrario me suma el valor 
  return y , il ,tipo_objeto_Eliminar
#////////////////////////////////////////////////////
#////////////////////////////////////////////////////
#Crear una funcion que reciba como parametro un objeto y este busque en que parte de la lista se encuentra este objeto ; para asi poder devolverme el indice de este .
def indiceObjeto(nobjeto,nlista):
    valor_in = None
    valor_verdarero = 0
    lista=[]
    for i in nlista :
        if nobjeto == i :
            valor_verdarero = valor_verdarero +nlista.index(nobjeto)
            break
    lista=[valor_verdarero,valor_in]
    return valor_in,valor_verdarero   #Esta funcion lo que me retorna el indice de la posicion del objeto encontrado


#No te olvides agregar abajo el if para comprobar si el libro no existe !!!

#//////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////
#//////////Esta es de la opcion 5:///////////////////////////////////
def Mostrar_Opcion5_OBL(nlista):#Esta me sirve para poder mostrar los libros ya existentes .
    for i in nlista :
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         print(f"El id : {i.id}; El titulo es : {i.titulo}; El genero es : {i.genero}; El ibsn es :{i.ibsn}; El editorial es : {i.editorial}; El autor es :{i.autor}")
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")


#////////////////////////////////////////////////////////////////////////
#/////////////////Esta tambien es de la opcion 5

def Econtrar_T_O_Ibsn(nlista,ncadena):
    n=0
    dc = 0
    for i in nlista :
        if i.titulo == ncadena or i.ibsn == ncadena:
            print(f"El id : {i.id} ; El titulo es : {i.titulo} ; El genero es : {i.genero} , El ibsn es :{i.ibsn};\n El editorial es : {i.editorial}; El autor es :{i.autor}")
            dc = nlista.index(i) + 1 #Lo que se hace aca es que si se encuentra un el libro ; quiero que me guarde el indice de este mas 1 ;
            n+=1 #Ademas que n me sume mas 1 tambien;lo que hago es que siempre cuando el objeto exista los dos valores dc y n van a ser lo mismo
            break
        else :
            n+=1 #En cambio cuando un objeto no se encuentra estos valores van a ser diferentes por ende no existiria el objeto
      
    return n ,dc 
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#////////////////////ESTA FUNCION ES PARA LA OPCION 6//////////////////////
#Esta funcion sirve para ordenar la lista de objetos de libros ; NO  olvidar que abajo en la opcion  6 debes vaciar a fuera la lista original despues de llamar la funcion ;
#para que esta pueda recibir los datos de los objetos ya ordenados 
#//////Despues utilizar la funcion de la opcion5 para poder mostrar los datos de los  libros libros ya ordenados
def Ordenar_obj(nlista): #Primero lo que hago es crear una funcion que reciba como objeto una lista de objtos libros

    n=0
    lista_temporal = [] #Creo una lista temporal
    lista_titulos = [] #Esta me servira para comprobar 
    for i in nlista : #Pongo un for por el hecho que primero tengo que extraer los valorestitulos de cada objeto ;para asi poder luego ordenarlo
        
        lista_titulos.append(i.titulo) #Hasta el momento lo que hace esto es retornarmelo en con cierto numero
        n = n+1
    lista_titulos.sort() #De esta forma lo ordeno 
    
    for k in lista_titulos : #Ahora que tengo los datos (titulos en lista) ordenados ;tengo que iterar en cada valor de la lista titulos
        pass
        for h in nlista : # Ahora con otro for dentro compruebo si el titulo correspondiente coincide o no con el objeto libro;solo se agregara en este for si coincide
           if k == h.titulo :
             lista_temporal.append(h)
             
     #Ahora vaciamos la lista original que contenia los libros
     #Despues recuperamos esos datos pero ordenados gracias a lo que hicimos antes
    return lista_temporal #Por eso terminando se obtiene la lista original ya ordenada

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#OPCION7/////////////////////////////
#Ahora como primera parte crea una funcion que detecte dos autores , para eso en el atributo autor cada autor tiene que estar separado por una coma .
#Esta funcion lo que hace es devolverme cero si no encontro nada y uno si encontro ;Su funcionalidad es que me dectecta si el nombre se encuentra en alguno de los libros
#de ser asi imprime por pantalla este libro ; ademas tiene la funcion que me encuentra los autores de un libro ;siempre y cuando los libros esten separados por comas

def Encontra_A_E_G (nnombre,nlista):
    s = 0
    lista_autores =[]
    for h in nlista :
        if "," in h.autor :
            lista_autores.append(h) #Esto lo que hace es guardar los objetos que tienen dos autores
            
      
    
    for i in nlista :
        if lista_autores == [] and i.autor == nnombre  :
                print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print(f"El id : {i.id}; El titulo es : {i.titulo}; El genero es : {i.genero}; El ibsn es :{i.ibsn}; El editorial es : {i.editorial}; El autor es :{i.autor}")
                print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                s=+1
                break
        
        elif lista_autores == [] and i.editorial == nnombre :#
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         print(f"El id : {i.id}; El titulo es : {i.titulo}; El genero es : {i.genero}; El ibsn es :{i.ibsn}; El editorial es : {i.editorial}; El autor es :{i.autor}")
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         s=+1
         break

        elif lista_autores == [] and i.genero == nnombre :
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         print(f"El id : {i.id}; El titulo es : {i.titulo}; El genero es : {i.genero}; El ibsn es :{i.ibsn}; El editorial es : {i.editorial}; El autor es :{i.autor}")
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         s+=1
         break
        else :
            for x in lista_autores:
                if  nnombre in x.autor : #Aca lo que se hace es que al recorrer el nombre en la lista de los autores ;si se encuentra el nombre se imprime o imprimira
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    print(f"El id : {x.id}; El titulo es : {x.titulo}; El genero es : {x.genero}; El ibsn es :{x.ibsn}; El editorial es : {x.editorial}; El autor es :{x.autor}")
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    s += 1  #Este for solo recorrera dentro de la lista autores nada mas .
                elif nnombre in x.editorial :  
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    print(f"El id : {x.id}; El titulo es : {x.titulo}; El genero es : {x.genero}; El ibsn es :{x.ibsn}; El editorial es : {x.editorial}; El autor es :{x.autor}")
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    s += 1  #Este for solo recorrera dentro de la lista autores nada mas .
                elif nnombre in x.genero :
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    print(f"El id : {x.id}; El titulo es : {x.titulo}; El genero es : {x.genero}; El ibsn es :{x.ibsn}; El editorial es : {x.editorial}; El autor es :{x.autor}")
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    s += 1  #Este for solo recorrera dentro de la lista autores nada mas .
        
        
         
       
        
    return s #Si la s que es una variable me retorna cero quiere decir que no encontro nada ;en cambio si se encontro algo devolvera uno

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Esta es la opcion8 //////////////////

#Esta funcion lo que me retorna es en una lista sublista donde se contiene informacion del objeto y su respectivo numero o ncantidad de autores
def detectarncantidad(nlista):
    lista_new =[] #Aca se guardara el objeto con un valor que va indicar la n cantidad de autores ejemp = [[obj.dadad,2],[obj.deeee,1]]
    for i in nlista :
        entegrar =[i,i.autor.count(",")+1 ]#Si la coma se encuentra una vez significa que hay dos autores
        lista_new.append(entegrar) #Por ende en cada iteracion me guardara el objeto en especifico y su cantidad de autores.
    return lista_new


#///////////Esta tambien pertene a al funcion 8 
#Esta funcion recibe como parametro la lista ya ordenada con su ncantidad e autores ; y su otro parametro es que la ncantida que indique el usuario 
def ImprimirOpcion8(nlista,ncatidad):
    s=0
    for i in nlista:
        if int(ncatidad) in i   : #Me imprime la ncantida de autores indicada con sus libros respectivos ;osea me refiero que solo me imprime si ncantidad concuerda con lo pedido por el usuario.
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         print(f"El id : {i[0].id}; El titulo es : {i[0].titulo}; El genero es : {i[0].genero}; El ibsn es :{i[0].ibsn}; El editorial es : {i[0].editorial}; El autor es :{i[0].autor}")
         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
         s= s +1
        
    return s  #Esto quiere decir cuando ese sea cero no habra encontrado nada por ende pondremos en un if  o condicional que si es esa cantida no hubo libro que encontrar y listar

#/////////////////////////////////////////Esta funcion le pertenece a la opcion 9 
#//////////Esta se encarga de obtener el objeto que el usuario quiere modificar ;ademas te devuelve su indice de donde se encuentra de la lista de objetos creados
#////
def ACtualizar_Opcion9(nlista,ntitulo):
    temporal =[]
    b=0
    for i in nlista :
        if i.titulo == ntitulo :
            temporal.append([i,nlista.index(i)]) #Esto hace refencia a que este el valor que quiere modificar mas su indice .
            
            break
    return temporal #me regrea dentro de una sublista el objeto y su indice 

#////Esta funcion que viene acontinuacion tambien es la que pertenece a la opcion 9 .
def Modifi_obj_Opcion9(nlistatempol):
    extraer_obj =[]
    for i in nlistatempol :
        extraer_obj.append(i[0])
    print("Usted modificará este libro :")
    t=input("Ingrese el titulo a modificar :")
    g=input("Ingrese el genero a modificar :")
    s=input("Ingrese el ibsn a modificar :")
    e=input("Ingrese la editorial a modificar :") 
    a=input("Ingrese el autor(es) a modificar :")
    extraer_obj[0].titulo=t
    extraer_obj[0].genero=g #De esta forma modifico los valores 
    extraer_obj[0].ibsn=s
    extraer_obj[0].editorial=e
    extraer_obj[0].autor=a
    
    return extraer_obj #Recuerda que lo que me devuelve es una lista asi que para poder cambiar sus datos tienes que hacer asi n[0].atributo(cambiar)

#Esta se encarga de recibir en una lista el objeto libro mas su indice [[obj,indice]] ;esta luego adentro extrae el objeto ;luego pide al usuario las
#nuevas caracteristicas a poner .Recuerda que esta solo retorna el objeto ya modificado ;para poder cambiarlo dentro de la lista de objetos necesitas
#su indice para asi poder modificarla ;ese indice la obtienes en la funcion anterior en la posicion uno [[obj,i]]  == [0][1] 

#/////////////////////////////////////////////////////////Esta es la opcion10
#////////ESta funcion se encarga de recibir como parametro la respuesta si y la lista de objetos creados
#Despues estos dentro de la funcion se se guardaran en el csv y se vaciaran
#Comprobar si el valor es 1 quiere decir que se añadio correctamente ; en caso contrario si es cero pues la respuesta;fue diferente a 'si'
def GuardarOpcion10(ncadena,nlista):
    t=0
    if ncadena.lower()== "si" :
        with open ('libros.csv','a',newline="") as arch :
          o = None 
          escribir=csv.writer(arch)
          for i in nlista :
            o=[i.id,i.titulo,i.genero,i.ibsn,i.editorial,i.autor]
            escribir.writerow(o)
        t= t +1 
    return t

#Crear una funcion que permita eliminar dependiendo del sistema operativo.
def clear():
    if os.name =="nt":
        os.system("cls")
    else :
        os.system("clear")









#////////////En esta parte es para poner las variables fuera del ciclo while 
lista_objetos_creados=[] #Aca se podran guardar en una lista cada objeto creado 
lista_de_libro_listados=[] #Esta lista no te olvides ponerlo fuera del while ;para que cuando el usuario entre de nuevo sin cerrar el programa se puede mostrar
#la lista de libros 
Palanca = True 


while Palanca == True :


    print("Opción 1: Leer archivo de disco duro.")
    print("Opción 2: Listar libros.Recuerda solo le lista los libros que han sido guardados en el disco duro .")
    print("Opción 3: Agregar libro.")
    print("Opción 4: Eliminar libro.Recuerda solo elimina los libros que han sido agregados en el espacio temporal")
    print("Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.")
    print("Opción 6: Ordenar libros por título.")
    print("Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.")
    print("Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.")
    print("Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")
    print("Opción 10: Guardar libros en archivo de disco duro .")


    #///////Esta es la opcion 1 (Aun falta ponerlo en el ciclo while):
    zq=input("Ingrese el numero de la opcion que desea entrar : ")
     
        


    if zq == str(1) :
    #////////Esta es la opcion 1 : Si quieres saber como funciona esta opcion ve a donde su creacion para poder saber


        MostrarCsvTexto()
        
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break








#///////Esta es la opcion 2 
    elif zq == str(2) :
        r=reci_titulo() #Llamamos a esta funcion para que me ahorre pensar mas adelante 
        c=opcion_2(r)#La variable r es la cadena que retorna la anterior funcion
        #Aca se comprueba si la lista esta vacia o no 
        if bool(c)== False :
            print("Este libro no se encuentra ,recuerda listar libros que esten guardados en csv .")
        else :
            d=pa_mo_list(c) #primero lo transformamos en cadena con esta funcion
            lista_de_libro_listados.append(d) #Despues de ser texto este se guardara dentro de la lista de libros
            print(f"\nEste libro se ha listado ;ahora podras verlo a continuacion : {pa_mo_list(lista_de_libro_listados)}")
        
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break








#Esta es la opcion 3 :
    elif zq == str(3) :
        
        #Primero llamamos ala funcion que me agrega los datos del usuario :
        datos = datos_tuplas() #este retorna cadenas que estan separadas por sus variables
        datos_li=list(datos)  #Lo transformamos a lista
        cr=Crear_Libro(datos_li) #Esta funcion retornara un objeto creado de clase libro
        lista_objetos_creados.append(cr)
        l_atri=Mostrar_los_Atributos(cr) #Esta funcion me devuelve una lista de los atributos de los objeto creados
        #Recuerda que los atributos los puedes llamar por su posicion ; id es [0],titulo[1];genero [2];ibsn[3];editorial[4];autor[5]
        print(f"Los datos del objeto creado son : id:{l_atri[0]} titulo : {l_atri[1]} , genero : {l_atri[2]} , ibsn : {l_atri[3]}, editorial : {l_atri[4]} , autor : {l_atri[5]} .")
        #Esto lo pongo aca por el hecho que cuando se crea un objeto este sera agregado a una lista ;para que asi despues se pueda utilizar en la opcion 4.
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break





#Opcion4 :
    elif zq == str(4):
        pol=input("Ingrese el titulo correctamente si es que quiere eliminar algun libro agregado : ")
        ki=EliminarObj(pol,lista_objetos_creados)
        kj=list(ki) #De esta forma lo guardo en una lista 
        if ki == (0,0,None): #Este es el tupla que me arroja cuando no encuentra nada
            print("Esta libro que intenta eliminar no existe.")
        elif ki[2] != None  :
            indice=indiceObjeto(kj[2],lista_objetos_creados)#Lo que se hace aca es que esto me devuelve el indice 
            lista_objetos_creados.pop(indice[1])
        #print(ki)
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break






#print(lista_objetos_creados)

    elif zq == str(5):
        #No olvidar que la opcion 5 ya esta hecha en el archivo prueba.py ; Recordar que tienes que arreglar la funcion de la opcion 4 ;
        #su solucion es muy similar a la funcion de la opcion 5 ; por favor no olvidar esto .(correcion ya esta hecho ahora.)
        Mostrar_Opcion5_OBL(lista_objetos_creados)
        koni=input("Ingrese el titulo o el ibsn que desea encontrar de un libro : ")
        oni=Econtrar_T_O_Ibsn(lista_objetos_creados,koni)
        juu=list(oni)
        if juu[0] > juu[1]: #Recuerda que en el indice 0 se encuentra el valor de i de incremento y en la posicion dos el indice
            print("Este libro que intentas buscar no existe.")
        elif juu == 0 :
            print("El libro no existe")
        elif oni == (0,0):
            print("Este libro no existe.")
        else :
            pass
        #print(oni)
        #Recuerda que te falta una funcion que muestre la los libros agregados.
        #if oni == (0,0):
        #    print("El libro no existe")
        
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break



#///////////////////////Esta es la opcion 6 
    elif zq == str(6) :
        hg=Ordenar_obj(lista_objetos_creados) #Esto me devuelve una lista de los objeto ya ordenados
        lista_objetos_creados=[] #Vaciamos la lista de objetos para despues que este reciba los objetos ordenados por el titulo.
        lista_objetos_creados=hg #Se le asigna la lista ya ordenada
        Mostrar_Opcion5_OBL(lista_objetos_creados) #Despues ago que muestre todos los objetos con sus respectivos atributos.
        if hg == []:
            print("No hay archivo que ordenar.")
        else :
            pass
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break


#/////////////////////Esta es la opcion 7 
    elif zq == str(7) :
        print("Recuerda que estos libros son los que anteriormente fueron guardados en un espacio temporal .\nEsto no busca archivos que esten guardados en el disco duro.")
        turu = input("ingrese el autor o editorial o genero para encontra los libros:")
        bbv=Encontra_A_E_G(turu,lista_objetos_creados)
        if bbv ==0 :
            print("No existe el libro que ha intentado buscar.")
        #print(bbv)
        else :
            pass
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break

#/////////////////////ACA va la opcion 8 
    elif zq == str(8) :
        iii=detectarncantidad(lista_objetos_creados) #ESto me retorna la lista ya ordenada dentro de sublista los objetos libros con sus respectivos ncatindad de autores.
        hhh=input("Ingrese la cantidad de autores :")
        if hhh.isdigit() is True :
            fff=ImprimirOpcion8(iii,hhh)
            if fff == 0  :
                print("La cantidad ingresada no es la correcta o no se encuentra libros agregados.Recuerda que esto solo buscan en el espacio temporal.")
        else :
            print("La cantida ingresada no es un digito")
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break

#ESta es la opcion9
    elif zq == str(9):
        clave=input("Ingrese el titulo del libro para asi poder modificar todas las caracteristicas del libro ;exceptuando el id :")
        kkk=ACtualizar_Opcion9(lista_objetos_creados,clave)
        if kkk == []:
            print("El dato que ha ingresado es incorrecto")
        else :
            llll=Modifi_obj_Opcion9(kkk)
            lista_objetos_creados[kkk[0][1]]=llll[0] #Con esto podras modificar tu objeto 
            #print(lista_objetos_creados)
        
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break

#Esta es la opcion10
    elif zq == str(10):
        password=input("Deseas guardar los libros que ha añadido en un espacio temporal ? (si o no ): ")

        bm=GuardarOpcion10(password,lista_objetos_creados)
        if bm > 0 :
            lista_objetos_creados = []
            print("Se ha guardado correctamente")
        if bm == 0 and password.lower() == "no":
            print("No ha guardado nada.")
        elif bm == 0 and password.lower() !="no":
            print("El valor ingresado es incorrecto.") 
            
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break

#Esta condicion es cuando el valor ingresado no sea un digito.
    elif zq != str(1) and zq != str (2) and zq != str(3) and zq != str(4) and zq != str(5) and zq != str(6) and zq != str(7) and zq != str(8) and zq !=str(9) and zq !=str(10):
        print("El valor ingresado es incorrecto o no es un digito.")
        xc = input("\nDesea regresar al menu principal ? De de ser asi escriba la letra s \n-si escribe otro caracter entendere que quiere salir del programa :")
        if xc.lower() == "s":
            clear()
        else :
            break


print("Gracias por ejecutarme al menos una vez :') ")

kaiken = input("Ingresa cualquier caracter para poder descansar.")
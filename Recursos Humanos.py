__author__ = 'Carlos Mario and Otoya'
DapeAdmi=[{"Nombre": "Carlos", "Usuario": "Carlos", "Contraseña": "mario"},{"Nombre": "Alex", "Usuario": "oto", "Contraseña": "123"},{"Nombre": "Jorge Otoya", "Usuario": "jorge", "Contraseña": "321"},{"Nombre": "Fernanda Gonzales","Usuario": "fer", "Contraseña": "2398"}]# Datos personales de los Adminisradores

DapeUsu=[{"Nombre":"Sergio Villafuerte","Cedula":"504080112","Evaluacion":0,"Usuario":"sergio","Contraseña":"p12","Direccion":"casa","Estado":"activo","Fecha de ingreso":"23/04/14","Puesto":"contador"},{"Nombre":"Gabriel Marin","Cedula":"505080112","Evaluacion":0,"Usuario":"marin","Contraseña":"p11","Direccion":"Pocosol","Estado":"activo","Fecha de ingreso":"23/04/13","Puesto":"secretaria"},{"Nombre":"Mario Diaz","Cedula":"604080112","Evaluacion":0,"Usuario":"diaz","Contraseña":"p14","Direccion":"los chiles","Estado":"activo","Fecha de ingreso":"12/06/14","Puesto":"seguridad"},{"Nombre": "Jorge Otoya","Cedula":"604320953","Estado":"activo","Evaluacion":0,"Direccion":"Golfito","Fecha de ingreso":"01/02/15","Puesto":"recursos humanos", "Usuario": "jorge", "Contraseña": "321"},{"Nombre": "Fernanda Gonzales","Cedula":"600230098","Estado":"activo","Evaluacion":0,"Direccion":"San Jose","Fecha de ingreso":"01/12/14","Puesto":"jefe contador","Usuario": "fer", "Contraseña": "2398"},{"Nombre":"Sharon Salazar","Cedula":"50501112","Evaluacion":0,"Usuario":"sha","Contraseña":"p10","Direccion":"San Ramon","Estado":"activo","Fecha de ingreso":"23/02/14","Puesto":"miscelaneo"}]#Datos personales de empleados

Meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

pusts=["contador","secretaria","seguridad","miscelaneo","jefe secretaria","jefe contador","recursos humanos"]

vaca=[{"Nombre":"Sharon Salazar","Solicitud Vacaciones": 0,"Meses Laborados":14,"Vacaciones Disponibles":14},{"Nombre":"Sergio Villafuerte","Solicitud Vacaciones": 0,"Meses Laborados":12,"Vacaciones Disponibles":12},{"Nombre":"Gabriel Marin","Solicitud Vacaciones": 0,"Meses Laborados": 24,"Vacaciones Disponibles": 24},{"Nombre":"Mario Diaz","Solicitud Vacaciones": 0,"Meses Laborados": 10,"Vacaciones Disponibles": 10},{"Nombre":"Jorge Otoya","Solicitud Vacaciones": 0,"Meses Laborados": 2,"Vacaciones Disponibles": 2},{"Nombre": "Fernanda Gonzales","Solicitud Vacaciones": 0,"Meses Laborados": 4,"Vacaciones Disponibles": 4}]

RejisPla=[]

solvaca=[]

planilla=[{"Nombre": "Sergio Villafuerte", "Puesto": "contador"},{"Nombre":"Gabriel Marin","Puesto":"secretaria"},{"Nombre":"Mario Diaz","Puesto":"seguridad"},{"Nombre":"Jorge Otoya","Puesto":"recursos humanos"},{"Nombre":"Sharon Salazar","Puesto":"miscelaneo"},{"Nombre": "Fernanda Gonzales","Puesto":"jefe contador"}]

Puestos={"contador": 2000, "secretaria": 1500, "seguridad": 1500, "miscelaneo": 1000, "jefe secretaria": 2000, "jefe contador": 2500, "recursos humanos": 2500}

def mostrar_planilla(x):
    print("Dijite el año de la planilla")
    año=int(input())
    print("Dijite el mes")
    mes=str(input())
    for m in RejisPla:
        if año == m[1] and mes == m[0]:
                print("La planilla del mes",mes,"y el año",año, "es")
                for ele in m:
                    if ele == m[0]:
                        pass
                    if ele==m[1]:
                        pass
                    if ele!=m[0] and ele!=[1]:
                        print(ele,"\n")
                        
                Admi(x)
    else:
        print("La planilla no se ha generado\nDesea Generarla?")
        generar=(input())
        if generar == "si":
            plani(x)
        if generar == "no":
            Admi(x)

def aguinaldo(x):
    #This function takes the aguinaldo belonging to a user. and it is shown
    #Input: If you want to know your bonus or not
    #Output: the aguinaldo to withdraw
    #Restrictions: it is a Boolean return, therefore nothing else receives whether or not
    for ele in planilla:
        if x in ele.values():
            if ele["Puesto"] in Puestos:
                    m=Puestos[ele["Puesto"]]
    for t in vaca:
        if x in t.values():
            meses=t["Vacaciones Disponibles"]
    if meses >= 12:
        print("Tu aguinaldo es de:", (m*(160*12))//12)
    else:    
        print("Tu aguinaldo es de:", (m*(160*meses))//12)
    llamadausuario(x)
            
def reg_plani(mes,año,total_incentivos,total_salarios):
    total={"total de pagos por incentivos":total_incentivos,"Total de pagos por salario":total_salarios}
    lista=[mes,año]
    for empl in planilla:
        lista.append(empl)
    lista.append(total)
    RejisPla.append(lista)

def empleado_inactivos(m):
    #Here the administrator sees all the inactive user,
    #Input: 'Yes' or not
    #Output: inactive users
    si = "si"
    no = "no"
    print("Quieres ver los empleados inactivos")
    ver=(input())
    while ver==si:
        for x in DapeUsu:
            if x["Estado"]== "inactivo":
                print(x["Nombre"])
        print("Son todos lo empleados")
        print("Quieres volver a verlos?")
        ver=(input())
    if ver==no:
        Admi(m)

def eliminar_puesto(v):
    #Here you can delete posts...
    #Inputs: the post to delete
    #Output: the deleted post
    #Restrictions: If the position is still associated with an employee not deleted it
    print("Que puesto vas a eliminar?")
    puesto=(input())
    for x in DapeUsu:
        if puesto in x.values():
            print("El puesto no se puede eliminar\nhay un empleado")
            Admi(v)
    if puesto in pusts:
        pusts.remove(puesto)
        del Puestos[puesto]
        print("Puesto eliminado")
        Admi(v)
        
def agregar_puestos(v):
    #In this function are added posts to the list of posts,
    #to then be used by the function of the aguinaldo, and administrator
    print("Digite el puesto a agregar")
    nuevo=str(input())
    print("Cuanto va a ganar este puesto por hora")
    gana=int(input())
    pusts.append(nuevo)
    Puestos[nuevo]=gana
    print ("Puesto agregado¡¡¡ ¿Quires agregar otro?")
    otro=(input())
    if otro== "si":
        agregar_puestos(v)
    elif otro== "no":
        Admi(v)

def solici(e):
    soli={}
    print(e["Nombre"],"Ha solicitado",e["Dias Solicitados"],"dias de vacaciones")
    print("Desea aceptar la salicitud de vacaciones")
    res=(input())
    if res == "si":
        e["Solicitud Vacaciones"]= "Aceptada"
        e["Vacaciones Disponibles"]=(e["Vacaciones Disponibles"])-(e["Dias Solicitados"])
        e["Dias Solicitados"]=0
        soli["Nombre"]=e["Nombre"]
        soli["Vacaciones Solicitados"]=e["Dias Solicitados"]
        solvaca.append(soli)
    if res == "no":
        e["Solicitud Vacaciones"]= "Rechazada"
        e["Dias Solicitados"]=0

def buzon(m):
    #Esta función realiza le entrada a buzón la cual contiene si han solicitado vacaciones los usuario o no
    print("Desea verificar las solicitudes de vacaciones..??")
    resp=(input())
    if vaca == []:
        print("No tiene solicitudes de vacaciones")
    if resp == "si":
        for e in vaca:
            if e["Solicitud Vacaciones"]== 1:
                solici(e)
    Admi(m)

def solivaca(x):
    print("Desea solicitar vacaciones..??")
    s=(input())
    if s == "si":
        for p in vaca:
            if x in p.values():
                if p["Meses Laborados"]>=12:
                    print("Digite los dias que va a solicitar")
                    ds=int(input())
                    for u in vaca:
                        if x in u.values():
                            if u["Vacaciones Disponibles"]<ds:
                                print("No cuenta con dias diponibles")
                                solivaca(x)
                            else:
                                for e in vaca:
                                    if x in e.values():
                                        e["Dias Solicitados"] = ds
                                        e["Solicitud Vacaciones"]= 1
                                        llamadausuario(x)
                if p["Vacaciones Disponibles"]<12:
                    print("Usted no ha cumplido con el año de trabajo")
                    llamadausuario(x)
    else:
        print("Comando invalido\nVuelva a intentar")
        llamadausuario(x)

def planillas2(x):
    for z in planilla:
        if x in z.values():
            z["Horas Extras"]=0
            z["Horas Laboradas"]=160
        for m in DapeUsu:
            if x in m.values():
                if m["Evaluacion"]<20:
                    z["Incentivos"]=0
                if m["Evaluacion"]>=20 and m["Evaluacion"]<40:
                    z["Incentivos"]=0.02
                if m["Evaluacion"]>=40 and m["Evaluacion"]<60:
                    z["Incentivos"]=0.03
                if m["Evaluacion"]>=60 and m["Evaluacion"]<80:
                    z["Incentivos"]=0.05
                if 80 <= m["Evaluacion"] < 101:
                    z["Incentivos"]=0.07

    for Z in planilla:
        if x in Z.values():
            if Z["Puesto"] in Puestos:
                    m=Puestos[Z["Puesto"]]
                    Z["Pago x Hora"]=m

def evalu(x):
    #Shows the respective evaluation délos users
    print("----------------------------------------------")
    print("")
    for y in DapeUsu:
        if x in y.values():
            print(y["Evaluacion"])
    print("----------------------------------------------")
    print("")
    llamadausuario(x)

def mostplae(x):
    for y in planilla:
        if x in y.values():
            if "Salario Neto" not in y:
                planillas2(x)
                for y in planilla:
                    #sueldo=(y["Horas Laboradas"]*y["Pago x Hora"])+(2*(y["Horas Extras"]*y["Pago x Hora"]))+y["Bonos/Incentivos"]
                    #y["Salario"]=sueldo
                    if x in y.values():
                        for z in y:
                            print(z,"=",y[z])
                print("Esta es la informacion de tu respectiva planilla\nLa informacion de horas aun no esta actualizada\nSolo un usuario administrador puede proporcionar esta informacion\nVuelve a consultar cuando la informacion este actualizada") 
            else:
                for y in planilla:
                    if x in y.values():
                        for z in y:
                            print(z,"=",y[z])
    print("----------------------------------------------")
    print("")
    llamadausuario(x)
    
def planillas():
    #This generates the returns from the user Assistant
    for x in planilla:
        x["Horas Extras"]=0
        x["Horas Laboradas"]=160
        x["Bonos"]=0
        for m in DapeUsu:
            if x["Nombre"] == m["Nombre"]:
                if m["Evaluacion"]<20:
                    x["Incentivos"]=0
                if m["Evaluacion"]>=20 and m["Evaluacion"]<40:
                    x["Incentivos"]=0.02
                if m["Evaluacion"]>=40 and m["Evaluacion"]<60:
                    x["Incentivos"]=0.03
                if m["Evaluacion"]>=60 and m["Evaluacion"]<80:
                    x["Incentivos"]=0.05
                if 80 <= m["Evaluacion"] < 101:
                    x["Incentivos"]=0.07
    for Z in planilla:
        #if x in Z.values():
        if Z["Puesto"] in Puestos:
                m=Puestos[Z["Puesto"]]
                Z["Pago x Hora"]=m

def agrebono():
    #Here is added the bonds received by the users.
    #Input: Add bonds
    #Output: Aggregate bond
    print("Digite el nombre del empleado")
    nu=(input())
    print("Digite el monto del bono otorgado")
    bono=int(input())
    for z in planilla:
        if nu in z.values():
            z["Bonos"]=(z["Bonos"])+bono
    print("Desea agregar otro bono/incentivo..??")
    R=(input())
    if R=="si":
        agrebono()
    else:
        pass

def modh():
    #This function modifies hours of users:
    #Inputs: the hours that you want to add or remove.
    #Outputs: the added hours or extended hours
    #Restrictions: You can not add more than 22 hours
    print("Digite el nombre del empleado")
    nom=(input())
    print("Dicho empleado laboro horas extras o quedo debiendo horas..??\nSi dicho empleado laboro horas extras escriba==> extras\nSi el empleado quedo debiendo horas escriba==> debe")
    R=(input())
    if R=="extras":
        print("Digite # de horas extras laboradas(NO PUDEN EXCEDER LAS 22 HORAS)")
        he=int(input())
        if he<=22:
            for z in planilla:
                if nom in z.values():
                    z["Horas Extras"]=(z["Horas Extras"])+he
        if he>22:
            print("Numero invalido\nOperacion fallida\nIntente nuevamente")
    if R=="debe":
        print("Digite el # de horas que debe el empleado(NO PUDEN EXCEDER LAS 160 HORAS)")
        hd=int(input())
        if hd<=160:
            for z in planilla:
                if nom in z.values():
                    z["Horas Laboradas"]=(z["Horas Laboradas"])-hd
        if hd>160:
            print("Numero invalido\nOperacion fallida\nIntente nuevamente")
    if R!="debe" and R!="extras":
        print("Comando invalido\nIntente nuevamente")
    print("Desea hacer otro cambio en las horas..??")
    Re=(input())
    if Re=="si":
        modh()
    else:
            pass

def plani(m):
    #This function generates the form and add it to a payroll record for then be consulted.
    #Input: date of form that you want to add
    #Outputs: aggregated payroll.
    #Restrictions: the date does not have to exceed the month in which it is requested, or a future
    z=0
    Z=len(RejisPla)
    print("----------------------------------------------")
    print("")
    print("Escriba la fecha de la planilla que desea generar ")
    print("Digite el año") 
    año=int(input())
    print("Digite el mes") 
    mes=(input())
    if mes in Meses and año<=2015:
        if año==2015:
            if mes=="mayo" or mes=="junio" or mes=="julio" or mes=="agosto" or mes=="septiembre" or mes=="octubre" or mes=="noviembre" or mes=="diciembre":
                print("Fecha invalida\nVuelva a intentar")
                plani(m)
        for fp in RejisPla:
            if mes==fp[0] and año==fp[1]:
                print("Planilla ya existente\nVuelva a intentar")
                plani(m)
            if mes!=fp[0] and año!=fp[1] or mes==fp[0] and año!=fp[1] or mes!=fp[0] and año==fp[1]:
                z=z+1
        if z==Z:
            planillas()
            print("Existen empleados que hayan recibido bono/incentivo en dicho..??")
            r=(input())
            if r == "si":
                agrebono()
            else:
                pass
            print("Existen empleados que hayan trabajado horas extras o trabajado menos horas..??")
            re=(input())
            if re == "si":
                modh()
            else:
                pass
            for x in planilla:
                salarioordinario=(x["Horas Laboradas"]*x["Pago x Hora"])
                x["Salario ordinario"]=salarioordinario
                salarioextraordinaria=(x["Horas Extras"])*(x["Pago x Hora"])*2
                x["Salario Extraordinario"]=salarioextraordinaria
                salariobruto=(x["Salario ordinario"])+(x["Salario Extraordinario"])
                x["Salario Bruto"]=salariobruto
                incen=(x["Salario Bruto"])*(x["Incentivos"])
                x["Incentivos"] = incen
                deducciones= (x["Salario ordinario"])*0.09
                x["Deducciones"]=deducciones
                salarioneto=(x["Salario Bruto"])-(x["Deducciones"])+incen
                x["Salario Neto"] = salarioneto
            total_salarios=0
            total_incentivos=0
            for g in planilla:
                total_salarios=total_salarios+(g["Salario Bruto"])
                total_incentivos=total_incentivos+(g["Incentivos"])
            reg_plani(mes,año,total_incentivos,total_salarios)
            print("Listo..!!!")
            print("Desea mostrar la planilla de empleados del mes de",mes)
            resp=(input())
            if resp=="si":
                mostrarplanilla(m,mes,total_salarios,total_incentivos)
            else:
                pass
            print("----------------------------------------------")
            print("")
            Admi(m)
    if mes not in Meses or año>2015:
        print("comando invalido")
        plani(m)

def mostrarplanilla(m, mes, total_salarios, total_incentivos):
    #This function is to show returns this month: with all employees.
    #Input: the month going to search.
    #Output: the month with their respective return!
    #Restrictions: If an administrator has not generate the return for that month did not show it is
    print("------->Planilla de Empleados del mes de",mes,"<-------")
    print("")
    for x in planilla:
        print("")
        print(x["Nombre"])
        for y in x:
            print(y,"=",x[y])
    print("El total de salarios a pagar es de:",total_salarios)
    print("El total de incentivos pagados es de",total_incentivos)
    print("----------------------------------------------")
    print("")
    Admi(m)

def puestos(ppp, pla):
    #Here the administrator will add the post in the user's personal information.
    #Input: Set to add.
    #Output: since added to personal data
    #Restrictions: If the post is not in the list of positions he take you an error message
    print("Cual es el puesto que va a desempeñar")
    for x in pusts:
        print(x)
    puesto=(input())
    if puesto in pusts:
        ppp["Puesto"]=puesto
        pla["Puesto"]=puesto
    else:
        print ("Puesto invalido")
        print("Vuelva a digitar un puesto Valido")
        puestos(ppp, pla)

def vacaciones(m):
    #This function allows the user to view their holiday, to see how many vacation days you have.
    #Entry: request to see holiday.
    #Outputs: the number of vacation days that has
    for x in vaca:
        if x["Nombre"] == m:
            print("Usted tiene",x["Vacaciones Disponibles"],"dias de vacaciones disponibles")
            llamadausuario(m)

def eliminar(m):
    #This feature allows the administrator to remove a user, in different lists
    #Entry: user name and your ballot paper output: deleted
    #User Restrictions: Write only name and identity card to search for it otherwise it will not be foun
    print("----------------------------------------------")
    print("")
    print("Digite el nombre")
    nomb=(input())
    print("Digite la cedula")
    eli=(input())
    for x in DapeUsu:
        if eli in x.values()and nomb in x.values():
            DapeUsu.remove(x)
            print("Usuario eliminado")
            print("----------------------------------------------")
            print("") 
            #for y in vaca:
                #if eli in y.values()and nomb in y.values():
                    #vaca.remove(x)
            for fg in planilla:
                if nomb in fg.values():
                    planilla.remove(x)
            Admi(m)
    else:
        print("usuario no registrado")
        print(">>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<")
        print("")
        Admi(m)
        
def evaluacion(y):
    #This function evaluates the user , and gives a percentage and then add the incentive
    print("----------------------------------------------")
    print("")
    print("Que usuario vas a evaluar\nEscribir el nombre?")
    nombre=str(input())
    for x in DapeUsu:
        if nombre in x.values():
            print("Que calificacion le das?")
            m=int(input())
            x["Evaluacion"]=m
            print("Evaluacion agregada")
            print("----------------------------------------------")
            print("")
            Admi(y)
            
def buscar_usuario(m):
    #This function seek the user to consult and will show you all the information available to the administrator user
    #Entry: username to consult.
    #Output: user information
    #Restrincciones : just type the name, not the user
    print("----------------------------------------------")
    print("")
    si = "si"
    no = "no"
    print("Escribe el numero de cedula",)
    buscar=str(input())
    for nom in DapeUsu:
        if buscar == nom["Cedula"]:
            print("Esta registrado y esta es su información")
            for x in nom:
                print(x,"=",nom[x])
            print("----------------------------------------------")
            print("")
            Admi(m)
    else:
        print("Usuario no registrado")
        print("----------------------------------------------")
        print("")
        Admi(m)
        
def agregar_usuario(x):
    #Here one may enter the administrator, this may add a new user either
    #administrator or employee if employee sent them to a dictionary where they will
    #be all employees of the company or company , otherwise it is what will add to the dictionary of the administrators
    print("----------------------------------------------")
    print("")
    import time
    from datetime import datetime
    formato="%d/%m/%y"
    admi= "Administrador"
    empleado="Empleado"
    si="si"
    no="no"
    print("Quieres seguir?",x)
    para_seguir=str(input())
    while para_seguir == si:
        print("El roll del nuevo usuario es?\nAdministrador\nEmpleado ")
        nuevo=(input())
        if nuevo == admi:
            pp = {}
            vvv = {}
            ppp = {}
            pla = {}
            print("Escribe el Usuario")
            usuarioadministrador=str(input())
            print("Escribe la Contraseña")
            nuevoadmicontra=str(input())
            print("Escibe el nombre")
            nombre = str(input())
            print("Escribe su numero de cedula")
            cedula = str(input())
            puestos(ppp,pla)
            print("Digite su direccion")
            direc = (input())
            print("Digite su numero de telefono ")
            telefono = (input())
            print("Digite la fecha de ingreso del empleado ")
            print("Formato disponible: DD/MM/YY ")
            fecha=(input())
            fecha=datetime.strptime(fecha,formato)
            fecha1=time.strftime(formato)
            fecha1=datetime.strptime(fecha1,formato)
            meses=((fecha1-fecha).days)//30
            ppp["Nombre"]= nombre
            vvv["Nombre"]= nombre
            vvv["Solicitud Vacaciones"]= 0
            vvv["Vacaciones Disponibles"]= meses
            vvv["Meses Laborados"]= meses
            pp["Nombre"]= nombre
            ppp["Cedula"]= cedula
            ppp["Evaluacion"]=0
            ppp["Usuario"]=usuarioadministrador
            ppp["Contraseña"]=nuevoadmicontra
            pp["Usuario"]=usuarioadministrador
            pp["Contraseña"]=nuevoadmicontra
            ppp["Direccion"]=direc
            ppp["Telefono"]=telefono
            ppp["Fecha de ingreso"]=fecha
            ppp["Estado"]="activo"
            pla["Nombre"]= nombre
            DapeAdmi.append(pp)
            DapeUsu.append(ppp)
            vaca.append(vvv)
            planilla.append(pla)
            print("¿Quieres agregar otro usuario??")
            para_seguir = str(input())
        if nuevo == empleado:
            vvv = {}
            ppp = {}
            pla = {}
            print("El nombre del nuevo empleado")
            nombre = (input())
            print("El numero de cedula")
            cedula = (input())
            print("Escribe el nombre de usuario")
            nueusu = (input())#nuevousuario
            print("Escribe la contraseña")
            contrausu=str(input())#contraseña del nuevo usuario
            puestos(ppp,pla)
            print("Digite su direccion")
            direc=(input())
            print("Digite su numero de telefono ")
            telefono=(input())
            fecha1=time.strftime(formato)
            fecha1=datetime.strptime(fecha1,formato)
            print("Digite la fecha de ingreso del empleado ")
            print("Formato disponible: DD/MM/YY ")
            fecha=(input())
            ppp["Fecha de ingreso"]=fecha
            fecha=datetime.strptime(fecha,formato)
            meses=((fecha1-fecha).days)//30
            ppp["Nombre"]= nombre
            vvv["Nombre"]= nombre
            vvv["Solicitud Vacaciones"]= 0
            vvv["Vacaciones Disponibles"]= meses
            vvv["Meses Laborados"]= meses
            pla["Nombre"]= nombre
            ppp["Cedula"]= cedula
            ppp["Evaluacion"]=0
            ppp["Usuario"]= nueusu
            ppp["Contraseña"]=contrausu
            ppp["Direccion"]=direc
            ppp["Telefono"]=telefono
            ppp["Estado"]="activo"
            vaca.append(vvv)
            DapeUsu.append(ppp)
            planilla.append(pla)
            print("Quieres agregar otro usuario??")
            para_seguir=str(input())
    else:
        print("----------------------------------------------")
        print("")
        Admi(x)
                  
def cambiar_estado(m):
    #This function can only be accessed by the administrator,
    #because it changes the status of the user from active to inactive and vice versa
    #Entry : Administrator Name
    #Output: User status changed
    #Restrinciones : Boolean going to be going to only be active, inactive
    print("----------------------------------------------")
    print("")
    print("Digite el nombre de usuario")
    nombre=(input())
    for x in DapeUsu:
        if nombre in x.values():
            si = "si"
            no = "no"
            print("El usuario esta", x["Estado"])
            print("Desea cambiar su estado")
            cambia = (input())
            if cambia == si:
                print("Digite el nuevo estado?")
                nuevo = str(input())
                x["Estado"] = nuevo
                print("Estado cambio")
                Admi(m)
            if cambia == no:
                print("----------------------------------------------")
                print("")
                Admi(m)
    else:
        print("Usuario no se encuentra")
        print("----------------------------------------------")
        print("")
        Admi(m)
            
def Admi(para):
    #This function is the Administrator menu , here makes calls to
    #other things that can make the administrator such as delete employee
    #Input: the user's name .
    #Output : calls to different functions .
    #Restrictions: You will not be allowed to choose another option which are not in the menu
    print("----------------------------------------------")
    print("")
    primero = 1
    segundo = 2
    tercero = 3
    cuarto = 4
    quinto = 5
    sexto = 6
    septimo = 7
    octavo = 8
    noveno = 9
    decimo = 10
    undecimo = 11
    duodecimo = 12
    print("Bienvenido", para, "Esto es lo que puedes hacer...")
    print("1:Cambiar estado de Usuario\n2:Agregar empleado\n3:Buscar usuario\n4:Evaluacion del usuario\n5:Eliminar usuario\n6:Generar planilla\n7:Buzon Vacaciones \n8:Ver empleados inactivos \n9:Agregar puesto\n10:Eliminar puesto\n11:Revisar planilla\n12:Salir")
    loquehace = int(input())
    if loquehace == primero:
        cambiar_estado(para)
    if loquehace == segundo:
        agregar_usuario(para)
    if loquehace == tercero:
        buscar_usuario(para)
    if loquehace == cuarto:
        evaluacion(para)
    if loquehace == quinto:
        eliminar(para)
    if loquehace == sexto:
        plani(para)
    if loquehace == septimo:
        buzon(para)
    if loquehace == octavo:
        empleado_inactivos(para)
    if loquehace == duodecimo:
        inicio()
    if loquehace == noveno:
        agregar_puestos(para)
    if loquehace == decimo:
        eliminar_puesto(para)
    if loquehace == undecimo:
        mostrar_planilla(para)
        
def llamadausuario(x):
    #This function is the user menu , here the user can make,
    #your transactions as asking vacation or know about your return.
    #This will be restricted to certain system functions for its candicion employee.
    print("----------------------------------------------")
    print("")
    primero = 1
    segundo = 2
    tercero = 3
    cuarto = 4
    quinto = 5
    sexto = 6
    setimo = 7
    print("Bienvenido", x, "Esto es lo que puedes hacer")
    print("1:Ver mi planilla\n2:Ver mi evaluación\n3:Ver vacaciones disponibles\n4:Solicitar Vacaciones\n6:Ver mi aguinaldo\n7:Salir")
    hacer=int(input())
    if hacer == primero:
        mostplae(x)
    if hacer == segundo:
        evalu(x)
    if hacer == tercero:
        vacaciones(x)
    if hacer == cuarto:
        solivaca(x)
    if hacer == sexto:
        aguinaldo(x)
    if hacer == setimo:
        inicio()
        
def inicio():
    #This in here login program will read the passwords and user
    #to enter and submit them to the respective menu .
    #if an employee is inactive this condition could not enter the system until an administrator change your status
    #Entrada: Username and contraseña.
    #Salida:Calls to different menu of sistema.
    #Restrincciones: If no username or password is incorrect you will return one notifying the user does not exist message.
    print("----------------------------------------------")
    print("")
    while True:
        print("Ingresa tu nombre de usuario")
        usuario = (input())
        print("Ingrese su contraseña")
        contraseña = (input())
        for x in DapeAdmi:
            if x["Usuario"] == usuario:
                if x["Contraseña"] == contraseña:
                    return Admi(x["Nombre"])
        for x in DapeUsu:
            if x["Usuario"] == usuario:
                if x["Contraseña"] == contraseña:
                    if x["Estado"] == "activo":
                        llamadausuario(x["Nombre"])
                    else:
                        print("Usted esta inactivo")
                        print("----------------------------------------------")
                        print("")
                        inicio()

        else:
            print("Usuario no Existe")
            print("----------------------------------------------")
            print("")
            inicio()

print("Hola Bienvenido al sistema contable S.A.C\n....Presiona ENTER para continuar....")
x = (input())
print("----------------------------------------------")
print("")
para_volver = inicio()

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import ClientePortal, Comuna, ColorVehiculo, VehiculoPortal, MarcaVehiculo, ModeloVehiculo, SolicitudDiag, EstadoSolicitud, \
    TallerMecanico, DetalleEspecialidad, Especialidad

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def exito(request):
    return render(request, 'core/exito.html')

def exitovehiculo(request):
    return render(request, 'core/exitovehiculo.html')

def exitosol(request):
    return render(request, 'core/exitosol.html')

def exitoreserva(request):
    return render(request, 'core/exitoreserva.html')

def exitoactu(request):
    return render(request, 'core/exitoactu.html')

def registro(request):
    return render(request, 'core/registro.html')

def ingreso(request):
    return render(request, 'core/ingreso.html')

def agregarcliente(request):
    
    if request.method == "POST":
        print("Es POST")
        runcliente = request.POST["runcliente"]
        print(runcliente)
        nombres = request.POST["nombres"]
        apepaterno = request.POST["apepaterno"]
        apematerno = request.POST["apematerno"]
        fechanac = request.POST["fechanac"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"] 
        email = request.POST["email"]
        password = request.POST["password"]

        idcomun = request.POST.get("idcomuna")
        idcom = Comuna.objects.get(idcomuna=idcomun)

        cliente_datos = ClientePortal(runcliente=runcliente, nombres=nombres, apepaterno=apepaterno, apematerno=apematerno, fechanac=fechanac, direccion=direccion, telefono=telefono, email=email, password=password, idcomuna=idcom)
        cliente_datos.save()
        messages.success(request, 'Form submission successful')

        user = User.objects.create_user(email, email, password, first_name=nombres, last_name=apepaterno)
        user.save()
        return redirect('exito')
    else:
        print("Es GET")
        posts = Comuna.objects.all()
    return render(request, 'core/registro.html', {'posts': posts})

@login_required(login_url='/accounts/login/')
def addVehiculo(request):

    useremail = request.user.email
    clienteaux = ClientePortal.objects.get(email=useremail)

    if request.method == "POST":

        print("Es POST")
        patente = request.POST["patente"]

        idcli = ClientePortal.objects.get(idcliente=clienteaux.idcliente)
        idcliaux = idcli.idcliente

        idcolo = request.POST.get("idcolor")
        idco = ColorVehiculo.objects.get(idcolor=idcolo)
        idcoaux = idco.idcolor

        idmodel = request.POST.get("idmodelo")
        idmod = ModeloVehiculo.objects.get(idmodelo=idmodel)
        idmodaux = idmod.idmodelo

        idmarc = request.POST.get("idmarca")
        idmar = MarcaVehiculo.objects.get(idmarca=idmarc)
        idmaraux = idmar.idmarca

        active = 'S'

        vehiculo_datos = VehiculoPortal(patente=patente, activo=active, idcliente=idcliaux, idcolor=idcoaux, idmodelo=idmodaux, idmarca=idmaraux)
        vehiculo_datos.save()

        return redirect('exitovehiculo')
    else:
        print("Es GET")
        color = ColorVehiculo.objects.all()
        modelo = ModeloVehiculo.objects.all()
        marca = MarcaVehiculo.objects.all()
    return render(request, 'core/clienteAgregar.html', {'color': color, 'modelo':modelo, 'marca':marca} )

@login_required(login_url='/accounts/login/')
def clienteHome(request):
    return render(request, 'core/clienteHome.html')

@login_required(login_url='/accounts/login/')
def diagnostico(request):


    useremail = request.user.email
    clienteaux = ClientePortal.objects.get(email=useremail)
    idcli22 = str(clienteaux.idcliente)
    print("Este es el id del cliente actual: N° "+idcli22)


    if request.method == "POST":
        print("Es POST")
        fecha = datetime.now()
        motivo = request.POST["motivo"]

        idcli = ClientePortal.objects.get(idcliente=clienteaux.idcliente)
        test = idcli.idcliente
        print(test)
        idestadosol = EstadoSolicitud.objects.get(idestadosol=1)
        estsol = idestadosol.idestadosol

        patent = request.POST.get("patente")
        pate = VehiculoPortal.objects.get(patente=patent)

        idtalle = request.POST.get("idtaller")
        idta = TallerMecanico.objects.get(idtaller=idtalle)

        idtalleraux = idta.idtaller

        solicitud_datos = SolicitudDiag(fechasol=fecha, motivo=motivo, idcliente=test, idestadosol=estsol, patente=pate, idtaller=idtalleraux)
        solicitud_datos.save()

        return redirect('exitosol')
    else:
        print("Es GET")
        vehiculo = VehiculoPortal.objects.filter(idcliente=clienteaux.idcliente)
        taller = TallerMecanico.objects.all()
    return render(request, 'core/solicitudDiagnostico.html', {'vehiculo': vehiculo, 'taller':taller} )

@login_required(login_url='/accounts/login/')
def listadovehiculo(request):

    useremail = request.user.email
    clienteaux = ClientePortal.objects.get(email=useremail)

    auto = VehiculoPortal.objects.filter(idcliente=clienteaux.idcliente)
    print(auto)

    color = ColorVehiculo.objects.all()
    modelo = ModeloVehiculo.objects.all()
    marca = MarcaVehiculo.objects.all()

    return render(request, 'core/listadoVehiculosCliente.html', {'auto': auto, 'color': color, 'modelo':modelo, 'marca':marca})

@login_required(login_url='/accounts/login/')
def listadosolicitud(request):
    useremail = request.user.email
    clienteaux = ClientePortal.objects.get(email=useremail)
    solicitud = SolicitudDiag.objects.filter(idcliente=clienteaux.idcliente)
    return render(request, 'core/listadoSolicitud.html', {'solicitud': solicitud})

@login_required(login_url='/accounts/login/')
def perfilcliente(request):

    useremail = request.user.email
    clienteaux = ClientePortal.objects.get(email=useremail)

    if request.method == "POST":
        nombres = request.POST["nombres"]
        apepaterno = request.POST["apepaterno"]
        apematerno = request.POST["apematerno"]
        fechanac = request.POST["fechanac"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"] 

        idcomun = request.POST.get("idcomuna")
        idcom = Comuna.objects.get(idcomuna=idcomun)

        updatecli = ClientePortal.objects.get(idcliente=clienteaux.idcliente)
        
        upuser = User.objects.get(id=request.user.id)
        upuser.first_name = nombres
        upuser.last_name = apepaterno
        upuser.save()

        updatecli.nombres = nombres
        updatecli.apepaterno = apepaterno
        updatecli.apematerno = apematerno
        updatecli.fechanac = fechanac
        updatecli.direccion = direccion
        updatecli.telefono = telefono
        updatecli.idcomuna = idcom
        updatecli.save()
            
        return redirect('exitoactu')

    else:
        print("Es GET")
        cliente = ClientePortal.objects.get(idcliente=clienteaux.idcliente)
        print(clienteaux.idcliente)
        cli1 = clienteaux.idcomuna
        print(cli1)
        posts = Comuna.objects.all()
    return render(request, 'core/perfilCliente.html', {'cliente': cliente, 'posts':posts})

@login_required(login_url='/accounts/login/')
def editarVeCli(request, pk):

    useremail = request.user.email


    if request.method == "POST":

        print("Es POST")

        vehi = VehiculoPortal.objects.get(patente=pk)

        idcolo = request.POST.get("idcolor")
        idco = ColorVehiculo.objects.get(idcolor=idcolo)

        idmodel = request.POST.get("idmodelo")
        idmod = ModeloVehiculo.objects.get(idmodelo=idmodel)

        idmarc = request.POST.get("idmarca")
        idmar = MarcaVehiculo.objects.get(idmarca=idmarc)

        vehi.idcolor = idco
        vehi.idmodelo = idmod
        vehi.idmarca = idmar
        vehi.save()

        return redirect('exitoactu')
    else:
        print("Es GET")
        auto = VehiculoPortal.objects.get(patente=pk)
        print(auto.idcolor)
        color = ColorVehiculo.objects.all()
        modelo = ModeloVehiculo.objects.all()
        marca = MarcaVehiculo.objects.all()
    return render(request, 'core/clienteEditarVe.html', {'auto':auto, 'color': color, 'modelo':modelo, 'marca':marca} )

def home2(request):
    taller = TallerMecanico.objects.all()
    print(taller)
    return render(request, 'core/home.html', {'taller':taller})


"""
Funcion para realizar búsqueda de un taller en Página de inicio
"""
def search(request):
    query = request.GET.get('q', '')     
    if query:
        qset = (
            Q(nomespecialidad__icontains=query)
        )
        qs = list(Especialidad.objects.filter(nomespecialidad__icontains=query).
                             values_list("idespecialidad", flat=True))
        ids_talleres = list(DetalleEspecialidad.objects.filter(idespecialidad__in=qs).
                                values_list("idtaller", flat = True))
        results = TallerMecanico.objects.filter(idtaller__in=ids_talleres)      
    else:
        results = []
    return render_to_response("core/home.html", {
        "results": results,
        "query": query
       
    })
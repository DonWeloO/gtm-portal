# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    idagenda = models.AutoField(primary_key=True)
    fechaagenda = models.DateTimeField()
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='idcliente')
    idhora = models.ForeignKey('HoraAgenda', models.DO_NOTHING, db_column='idhora')
    idot = models.ForeignKey('OrdenTrabajo', models.DO_NOTHING, db_column='idot', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    nomcargo = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    runcliente = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=80)
    apepaterno = models.CharField(max_length=80)
    apematerno = models.CharField(max_length=80)
    fechanac = models.DateField()
    direccion = models.CharField(max_length=80)
    telefono = models.IntegerField()
    email = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=25)
    idcomuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='idcomuna')

    class Meta:
        managed = False
        db_table = 'cliente'
    
    def get_idcomuna(self):
        return self.idcomuna.idcomuna


class ColorVehiculo(models.Model):
    idcolor = models.AutoField(primary_key=True)
    nomcolor = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'color_vehiculo'
    
    def __str__(self):
        return self.nomcolor



class Comuna(models.Model):
    idcomuna = models.AutoField(primary_key=True)
    nomcomuna = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
      return self.nomcomuna
        

class DetalleOp(models.Model):
    iddetalleop = models.AutoField(primary_key=True)
    cantidad_prod = models.IntegerField()
    precio = models.IntegerField()
    totallinea = models.IntegerField()
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    idop = models.ForeignKey('OrdenPedido', models.DO_NOTHING, db_column='idop')

    class Meta:
        managed = False
        db_table = 'detalle_op'


class DetalleServ(models.Model):
    iddetallerserv = models.AutoField(primary_key=True)
    cantidadprod = models.IntegerField()
    costoprod = models.IntegerField()
    costototal = models.IntegerField()
    idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idservicio', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'detalle_serv'


class DetalleServot(models.Model):
    iddetalleservot = models.AutoField(primary_key=True)
    cantidad_serv = models.IntegerField()
    precioserv = models.IntegerField()
    totallineaserv = models.IntegerField()
    idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idservicio')
    idot = models.ForeignKey('OrdenTrabajo', models.DO_NOTHING, db_column='idot')

    class Meta:
        managed = False
        db_table = 'detalle_servot'


class DetalleVenta(models.Model):
    iddetallev = models.AutoField(primary_key=True)
    cantidadventa = models.IntegerField()
    precio = models.IntegerField()
    totallinea = models.IntegerField()
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idot = models.ForeignKey('OrdenTrabajo', models.DO_NOTHING, db_column='idot', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoOt(models.Model):
    idestadoot = models.AutoField(primary_key=True)
    nomestadoot = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_ot'


class EstadoSolicitud(models.Model):
    idestadosol = models.AutoField(primary_key=True)
    descripestado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_solicitud'

    def __str__(self):
        return self.descripestado


class HoraAgenda(models.Model):
    idhora = models.IntegerField(primary_key=True)
    rangohora = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'hora_agenda'


class IngresoVehiculo(models.Model):
    idingresovehi = models.AutoField(primary_key=True)
    fechaingreso = models.DateTimeField()
    motivo = models.CharField(max_length=500)
    diagnostico = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    idtaller = models.ForeignKey('TallerMecanico', models.DO_NOTHING, db_column='idtaller')
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='patente')

    class Meta:
        managed = False
        db_table = 'ingreso_vehiculo'


class MarcaVehiculo(models.Model):
    idmarca = models.AutoField(primary_key=True)
    nommarca = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'marca_vehiculo'
    
    def __str__(self):
        return self.nommarca



class MetodoPago(models.Model):
    idmetodo = models.IntegerField(primary_key=True)
    nommetodo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class ModeloVehiculo(models.Model):
    idmodelo = models.AutoField(primary_key=True)
    nommodelo = models.CharField(max_length=30)
    idmarca = models.ForeignKey(MarcaVehiculo, models.DO_NOTHING, db_column='idmarca')

    class Meta:
        managed = False
        db_table = 'modelo_vehiculo'

    def __str__(self):
        return self.nommodelo

    def get_idmarca(self):
        return self.idmarca.idmarca


class OrdenPedido(models.Model):
    idop = models.AutoField(primary_key=True)
    fechaop = models.DateTimeField()
    montoneto = models.IntegerField()
    montoiva = models.IntegerField()
    montototal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_pedido'


class OrdenTrabajo(models.Model):
    idot = models.AutoField(primary_key=True)
    fechaot = models.DateTimeField()
    presupuestoinicial = models.IntegerField()
    costofinal = models.IntegerField()
    idestadoot = models.ForeignKey(EstadoOt, models.DO_NOTHING, db_column='idestadoot')
    idingresovehi = models.ForeignKey(IngresoVehiculo, models.DO_NOTHING, db_column='idingresovehi')

    class Meta:
        managed = False
        db_table = 'orden_trabajo'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nomproducto = models.CharField(max_length=60)
    preciounitario = models.IntegerField()
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    rutproveedor = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    fono = models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RecepcionOp(models.Model):
    idrecepcionot = models.AutoField(primary_key=True)
    fecharecepcion = models.DateTimeField()
    conformidad = models.CharField(max_length=2)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')
    idop = models.ForeignKey(OrdenPedido, models.DO_NOTHING, db_column='idop')

    class Meta:
        managed = False
        db_table = 'recepcion_op'


class Servicio(models.Model):
    idservicio = models.AutoField(primary_key=True)
    nomservicio = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class SolicitudDiag(models.Model):
    idsolicitud = models.AutoField(primary_key=True)
    fechasol = models.DateTimeField()
    motivo = models.CharField(max_length=500)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    idestadosol = models.ForeignKey(EstadoSolicitud, models.DO_NOTHING, db_column='idestadosol')
    patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='patente')
    idtaller = models.ForeignKey('TallerMecanico', models.DO_NOTHING, db_column='idtaller')

    class Meta:
        managed = False
        db_table = 'solicitud_diag'


class StockProducto(models.Model):
    cant_adquirido = models.IntegerField()
    cant_venta = models.IntegerField()
    cant_disponible = models.IntegerField()
    stock_minimo = models.IntegerField()
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto', primary_key=True)

    class Meta:
        managed = False
        db_table = 'stock_producto'


class TallerMecanico(models.Model):
    idtaller = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ruttaller = models.CharField(unique=True, max_length=10)
    direccion = models.CharField(max_length=100)
    fono1 = models.IntegerField()
    fono2 = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=80)
    foto = models.ImageField(upload_to = 'fotos', default = 'sin-imagen.jpg', null=True, blank=True)
    fechacreacion = models.DateTimeField()
    activo = models.CharField(max_length=1)
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')

    class Meta:
        managed = False
        db_table = 'taller_mecanico'

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    idtipodoc = models.IntegerField(primary_key=True)
    nomdoc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    rutusuario = models.CharField(unique=True, max_length=10)
    nomusuario = models.CharField(max_length=60)
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    fono = models.IntegerField()
    email = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=30)
    activo = models.CharField(max_length=1)
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idcargo')
    idtaller = models.ForeignKey(TallerMecanico, models.DO_NOTHING, db_column='idtaller')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    idcolor = models.ForeignKey(ColorVehiculo, models.DO_NOTHING, db_column='idcolor')
    idmodelo = models.ForeignKey(ModeloVehiculo, models.DO_NOTHING, db_column='idmodelo')
    idmarca = models.ForeignKey(MarcaVehiculo, models.DO_NOTHING, db_column='idmarca')

    class Meta:
        managed = False
        db_table = 'vehiculo'

    def __str__(self):
        return self.patente


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    fechaventa = models.DateTimeField()
    montoneto = models.IntegerField()
    montooiva = models.IntegerField()
    montototal = models.IntegerField()
    idmetodo = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='idmetodo')
    idtipodoc = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='idtipodoc')

    class Meta:
        managed = False
        db_table = 'venta'

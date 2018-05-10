from django.urls import path
from .views import (
    index,
    login,
    signIn,
    logout,
    signInRegister,
    viajes_inscriptos,
    buscar_viajes,
    configuracion_cuenta,
    mis_viajes,
    crear_viaje
)

from .ajax import (
    lista_de_espera_de_copilotos_para_un_viaje,
    viajes_activos,
    lista_de_calificaciones_pendientes_a_copilotos,
    lista_de_calificaciones_pendientes_a_pilotos,
    datos_relacionados_al_usuario
)

name = 'unAventonApp'

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('signin', signIn, name='signin'),
    path('signinReg', signInRegister, name='signin_register'),
    path('logout', logout, name='logout'),
    path('viajesInscriptos', viajes_inscriptos, name='viajes_inscriptos'),
    path('buscarViajes', buscar_viajes, name='buscar_viajes'),
    path('configuracionCuenta', configuracion_cuenta, name='config_cuenta'),
    path('misViajes', mis_viajes, name='mis_viajes'),
    path('crearViaje', crear_viaje, name='crear_viaje'),
    path('miPerfil', mi_perfil, name='mi_perfil'),

    path('ajax/copilotosEnEspera', lista_de_espera_de_copilotos_para_un_viaje,
         name='lista_espera'),
    path('ajax/misViajesActivos', viajes_activos, name='viajes_activos'),
    path('ajax/califPendientesCopilotos', lista_de_calificaciones_pendientes_a_copilotos,
         name='lista_calificaciones_copilotos'),
    path('ajax/califPendientesPilotos', lista_de_calificaciones_pendientes_a_pilotos,
         name='lista_calificaciones_pilotos'),
    path('ajax/datosRelacionandosAlUsuario', datos_relacionados_al_usuario,
         name='datos_del_usuario'),


]

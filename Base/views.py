from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from .forms import *


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'Base/home.html'
    login_url = '/login/'

class LoginPagina(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'base/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'base/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'base/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'base/passwordExitoso.html', {})


# AUTOMOVIL

class AutomovilLista(LoginRequiredMixin, ListView):
    context_object_name = 'automoviles'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='automovil')
    template_name = 'Base/listaAutomoviles.html'
    login_url = '/login/'

class AutomovilDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'automovil'
    template_name = 'Base/automovilDetalle.html'

class AutomovilUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('automoviles')
    context_object_name = 'automovil'
    template_name = 'Base/automovilEdicion.html'

class AutomovilDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('automoviles')
    context_object_name = 'automovil'
    template_name = 'Base/automovilBorrado.html'

# CAMIONETA

class CamionetaLista(LoginRequiredMixin, ListView):
    context_object_name = 'camionetas'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='camioneta')
    template_name = 'Base/listaCamionetas.html'
    login_url = '/login/'

class CamionetaDetalle(LoginRequiredMixin,DetailView):
    model = Vehiculo
    context_object_name = 'camioneta'
    template_name = 'Base/camionetaDetalle.html'

class CamionetaUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('camionetas')
    context_object_name = 'camioneta'
    template_name = 'Base/camionetaEdicion.html'

class CamionetaDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('camionetas')
    context_object_name = 'camioneta'
    template_name = 'Base/camionetaBorrado.html'

# SUV

class SuvlLista(LoginRequiredMixin, ListView):
    context_object_name = 'suvs'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='suv')
    template_name = 'Base/listaSuvs.html'
    login_url = '/login/'

class SuvDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'suv'
    template_name = 'Base/suvDetalle.html'

class SuvUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('suvs')
    context_object_name = 'suv'
    template_name = 'Base/suvEdicion.html'

class SuvDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('suvs')
    context_object_name = 'suv'
    template_name = 'Base/suvBorrado.html'

# DEPORTIVO

class DeportivoLista(LoginRequiredMixin, ListView):
    context_object_name = 'deportivos'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='deportivo')
    template_name = 'Base/listaDeportivos.html'
    login_url = '/login/'

class DeportivoDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'deportivo'
    template_name = 'Base/deportivoDetalle.html'

class DeportivoUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('deportivos')
    context_object_name = 'deportivo'
    template_name = 'Base/deportivoEdicion.html'

class DeportivoDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('deportivos')
    context_object_name = 'deportivo'
    template_name = 'Base/deportivoBorrado.html'

# MOTO

class MotoLista(LoginRequiredMixin, ListView):
    context_object_name = 'motos'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='moto')
    template_name = 'Base/listaMotos.html'
    login_url = '/login/'

class MotoDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'moto'
    template_name = 'Base/motoDetalle.html'

class MotoUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('motos')
    context_object_name = 'moto'
    template_name = 'Base/motoEdicion.html'

class MotoDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('motos')
    context_object_name = 'moto'
    template_name = 'Base/motoBorrado.html'

# BICICLETA

class BicicletaLista(LoginRequiredMixin, ListView):
    context_object_name = 'bicicletas'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='bicicleta')
    template_name = 'Base/listaBicicletas.html'
    login_url = '/login/'

class BicicletaDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'bicicleta'
    template_name = 'Base/bicicletaDetalle.html'

class BicicletaUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'Base/bicicletaEdicion.html'

class BicicletaDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'Base/bicicletaBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Vehiculo.objects.filter(vehiculo__startswith='otro')
    template_name = 'Base/listaOtros.html'
    login_url = '/login/'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    context_object_name = 'otro'
    template_name = 'Base/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = ActualizacionVehiculo
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroBorrado.html'

# CREACION VEHICULO

class VehiculoCreacion(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = FormularioNuevoVehiculo
    success_url = reverse_lazy('home')
    template_name = 'Base/vehiculoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VehiculoCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Base/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'base/acercaDeMi.html', {})



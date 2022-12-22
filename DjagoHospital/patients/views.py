from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddMedicForm, RegisterUserForm, LoginUserForm
from .models import Patient, Medics
from .utils import menu, DataMixin


# def index(request):
#     #return HttpResponse("Страница приложения patients")
#     return render(request, '<patients/index.html>')
#
# def about(request):
#     return render(request, '<patients/about.html>')

menu = [{'title': "О сайте", 'url_name': 'about'}]

def groups(request, group):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Список медиков по группам.\</h1><h2>{group}</h2>')

def index(request):
    medics = Medics.objects.all()
    context = {
        'medics': medics,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'patients/index.html', context=context)

def about(request):
    return render(request, 'patients/about.html', {'menu': menu, 'title': 'About page'})

# def login(request):
#     return HttpResponse('Логин')

def patients(request):
    return HttpResponse('Пациенты')

def show_medic(request, med_slug):
    medic = get_object_or_404(Medics, slug=med_slug)

    context = {
        'med':medic,
        'menu': menu,
    }
    return render(request, 'patients/medics.html', context=context)

def medics(request):
    medics = Medics.objects.all()
    context = {
        'menu': menu,
        'medics': medics,
    }
    return render(request, 'patients/aboutmedics.html', context=context)


def addmedic(request):
    if request.method == 'POST':
        form = AddMedicForm(request.POST)
        if form.is_valid():
    # print(form.cleaned_data)
            try:
                Medics.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка!')
    else:
            form = AddMedicForm()
    return render(request, 'patients/addmedic.html', {'form': form})




class MedicHome(DataMixin, ListView):
    model = Medics
    template_name = 'patients/index.html'
    context_object_name = 'medics'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        c_def = self.get_user_context(title='Главная страница', auth=auth)
        # context['title'] = 'Главная страница'
        # context['menu'] = menu
        return {**context, **c_def}

    def get_queryset(self):
        return Medics.objects.filter(is_working=True)

class ShowMedic(DataMixin, DetailView):
    model = Medics
    template_name = 'patients/medics.html'
    slug_url_kwarg = 'med_slug'
    context_object_name = 'med'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class AddMedic(LoginRequiredMixin, CreateView):
    form_class = AddMedicForm
    template_name = 'patients/addmedic.html'
    success_url = reverse_lazy('home')

class RegisterUser(DataMixin, CreateView):
     form_class = RegisterUserForm
     template_name = 'patients/register.html'
     success_url = reverse_lazy('login')

     def get_context_data(self, *, object_list=None, **kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title="Регистрация")
         return {**context, **c_def}

     def form_valid(self, form):
         user = form.save()
         login(self.request, user)
         return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'patients/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')



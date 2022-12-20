from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddMedicForm
from .models import Patient, Medics
from .utils import menu, DataMixin


# def index(request):
#     #return HttpResponse("Страница приложения patients")
#     return render(request, '<patients/index.html>')
#
# def about(request):
#     return render(request, '<patients/about.html>')

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Врачи", 'url_name': 'medics'},
        {'title': "Войти", 'url_name': 'login'}]

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

def login(request):
    return HttpResponse('Логин')

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
    return HttpResponse('Врачи')


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
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


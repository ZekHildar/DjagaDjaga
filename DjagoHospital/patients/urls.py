from django.urls import path
from patients.views import index, groups, about, patients, medics, login, show_medic, addmedic, MedicHome, \
    ShowMedic, AddMedic

urlpatterns = [
    path('', MedicHome.as_view(), name = 'home'),
    path('groups/<slug:group>/', groups),
    path('about/', about, name = 'about'),
    path('medics/', medics, name='medics'),
    path('medics/<slug:med_slug>/', ShowMedic.as_view(), name='medic'),
    path('login/', login, name='login'),
    path('addmedic/', AddMedic.as_view(), name='addmedic'),
]
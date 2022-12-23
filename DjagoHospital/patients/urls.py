from django.urls import path, include
from .viewsets import MedicViewSet
# from patients.viewsets import MedicAPIView, MedicAPIDetailView
from patients.views import index, groups, about, patients, medics, login, show_medic, addmedic, MedicHome, \
    ShowMedic, AddMedic, RegisterUser, LoginUser, logout_user
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'medics', MedicViewSet, basename='medics')




urlpatterns = [
    path('', MedicHome.as_view(), name = 'home'),
    path('groups/<slug:group>/', groups),
    path('about/', about, name = 'about'),
    path('medics/', medics, name='medics'),
    path('medics/<slug:med_slug>/', ShowMedic.as_view(), name='medic'),
    path('login/', LoginUser.as_view(), name='login'),
    path('addmedic/', AddMedic.as_view(), name='addmedic'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls'))
]



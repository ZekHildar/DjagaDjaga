from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .utils import MedicAPIPagination
from .models import Medics, GroupType
from .serializers import MedicSerializer, MedicDetailSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class MedicAPIView(ListCreateAPIView):
#     queryset = Medics.objects.all()
#     serializer_class = MedicSerializer
#
# class MedicAPIDetailView(RetrieveUpdateAPIView):
#     queryset = Medics.objects.all()
#     serializer_class = MedicSerializer

class MedicViewSet(viewsets.ModelViewSet):
     #queryset = Medics.objects.all()
     pagination_class = MedicAPIPagination
     permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
     def get_queryset(self):
          group = self.request.GET.get('group', '')
          if group:
               return Medics.objects.filter(grouptype_id=group)
          else:
               return Medics.objects.all()
     #serializer_class = MedicSerializer

     def get_serializer_class(self):
          if self.action == 'retrieve':
               return MedicDetailSerializer
          return MedicSerializer


     @action(methods=['get'], detail=True)
     def group(self, request, pk=None):
          group = GroupType.objects.get(pk=pk)
          return Response({'group': f'{group.grouptype}-{group.service}'})
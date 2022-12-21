from rest_framework import serializers
from .models import Medics

class MedicSerializer(serializers.ModelSerializer):
     class Meta:
         model = Medics
         fields = '__all__'

class MedicDetailSerializer(serializers.ModelSerializer):
     group_name = serializers.SerializerMethodField()
     class Meta:
         model = Medics
         fields = '__all__'
     def get_group_name(self, obj):
         return f'{obj.grouptype.grouptype}-{obj.grouptype.service}'
from django.db.models import fields






from rest_framework import serializers
from .models import EmployeModel
  
class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeModel
        fields = '__all__'
        
        
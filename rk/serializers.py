from rk.models import department
from rk.models import employee
from rest_framework import serializers


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ["id", "name", "sallary", "departmentID"]

class departmentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ["id", "name"]


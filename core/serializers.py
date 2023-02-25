from rest_framework import serializers
from core.models import Employees, Shifts


class EmployeesSerializer(serializers.ModelSerializer):
    shifts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'email', 'shifts']


class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = ['id', 'shift_date', 'shift_time', 'employee']

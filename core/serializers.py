from rest_framework import serializers
from models import Employees, Shifts


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ['url', 'first_name', 'last_name', 'email', 'shifts']


class ShiftsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shifts
        fields = ['url', 'shift_date', 'shift_time', 'employee']

from core.models import Employees, Shifts
from core.serializers import EmployeesSerializer, ShiftsSerializer
from rest_framework import generics


class EmployeesList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class ShiftsList(generics.ListCreateAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer


class ShiftsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer

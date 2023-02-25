from core.models import Employees, Shifts
from core.serializers import EmployeesSerializer, ShiftsSerializer
from rest_framework import generics


class EmployeesList(generics.ListCreateAPIView):
    """
    Lists all employees and creates an employee.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Shows details of a singe employee.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class ShiftsList(generics.ListCreateAPIView):
    """
    Lists all shifts and creates a shift.
    """
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer


class ShiftsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Shows details of a single shift.
    """
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer

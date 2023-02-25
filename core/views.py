from django.shortcuts import render
from core.models import Employees, Shifts
from core.serializers import EmployeesSerializer, ShiftsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
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

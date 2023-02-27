from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Employees, Shifts


class EmployeesTests(APITestCase):
    def test_create_employee(self):
        """
        Ensure we can create a new employee object.
        """
        url = reverse('employees-list')
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@doe.com",
            "shifts": []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employees.objects.count(), 1)
        self.assertEqual(Employees.objects.get().first_name, 'John')


class ShiftsTests(APITestCase):

    def setUp(self):
        self.employee = Employees.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@doe.com",
        )

    def test_create_shifts(self):
        """
        Ensure we can create a new shifts object.
        """
        url = reverse('shifts-list')
        data = {
            "shift_date": "2023-02-23",
            "shift_time": "0-8",
            "employee": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shifts.objects.count(), 1)

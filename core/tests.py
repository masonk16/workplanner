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

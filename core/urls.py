from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('employees/', views.EmployeesList.as_view(), name="employees-list"),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view(), name="employees-detail"),
    path('shifts/', views.ShiftsList.as_view(), name="shifts-list"),
    path('shifts/<int:pk>', views.ShiftsDetail.as_view(), name="shifts-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)

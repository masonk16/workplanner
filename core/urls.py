from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
    path('shifts/', views.ShiftsList.as_view()),
    path('shitfs/<int:pk>', views.ShiftsDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

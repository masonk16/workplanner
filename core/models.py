from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Employees(models.Model):
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Shifts(models.Model):
    SHIFT_TIMES = [
        ('0-8', '0-8'),
        ('8-16', '8-16'),
        ('16-24', '16-24')
    ]
    shift_date = models.DateField()
    shift_time = models.CharField(choices=SHIFT_TIMES, max_length=10)
    employee = models.ForeignKey(Employees, related_name='shifts', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['employee', 'shift_date']
        ordering = ['shift_date', 'shift_time']

    def __str__(self):
        return '%s, %s' % (self.shift_date, self.shift_time)

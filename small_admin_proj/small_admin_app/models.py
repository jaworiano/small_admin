from django.db import models
from django.urls import reverse
# Create your models here.

ARCMAP_VER = (
    (10.0, "10.0"),
    (10.1, "10.1"),
    (10.2, "10.2"),
    (10.3, "10.3"),
    (10.4, "10.4"),
    (10.5, "10.5"),
    )

ARCMAP_LIC = (
     ('B', 'BASIC'),
     ('S', 'STANDARD'),
     ('A', 'ADVANCE'),
    )

DIVISIONS = (
    (100, 'DESIGN'),
    (200, 'ENVIRONMENTAL'),
    (300, 'RAIL'),
    (400, 'BRIDGES'),
    (500, 'ADMIN'),
    (600, 'A1'),
    (700, 'ROADS'),
    (800, 'OILGAS'),

)

class Computers(models.Model):
    id_numb = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

class ArcMap(models.Model):
    version = models.FloatField(choices=ARCMAP_VER, default=10.0)
    license = models.CharField(max_length=10, choices=ARCMAP_LIC, default='BASIC')

class Divisions(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('divisions', kwargs={'pk': self.id})

class Employee(models.Model):
      name = models.CharField(max_length=64)
      last_name = models.CharField(max_length=64)
      user_computer = models.OneToOneField(Computers, on_delete=models.CASCADE)
      division_user = models.ForeignKey(Divisions, on_delete=models.PROTECT)

      def __str__(self):
          return self.name, self.user_computer.name

      def get_absolute_url(self):
          return reverse('employee_detail', kwargs={'pk': self.id})


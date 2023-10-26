from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    state_country = models.CharField(max_length=2, verbose_name="Sigla do Estado") 

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    address = models.CharField(max_length=100,  verbose_name="Endereço")
    email = models.EmailField(verbose_name="E-mail")
    date_of_birth = models.DateField(verbose_name="Data de Nascimento")
    city = models.ForeignKey(City, on_delete=models.CASCADE,  verbose_name="Cidade")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")
    
    def __str__(self):
        return self.name
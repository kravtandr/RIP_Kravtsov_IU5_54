from django.db import models


class department(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name="Название отдела")


class employee(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name="Фамилия сотрудника")
    sallary = models.IntegerField(verbose_name="Зарплата")
    departmentID = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

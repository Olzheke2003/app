from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)


class WorkSchedule(models.Model):
    work_schedule = models.CharField(max_length=256)


class Gender(models.Model):
    gender = models.CharField(max_length=256)


class Company(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='company_images', blank=True, null=True)


class Jobs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location_job = models.CharField(max_length=256)
    work_schedule_job = models.ForeignKey(WorkSchedule, on_delete=models.SET_DEFAULT, default='Нет')
    experience = models.PositiveIntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.SET_DEFAULT, default='Нет')
    name = models.CharField(max_length=256)
    salary = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

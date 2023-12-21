from django.db import models

class FirstName(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class LastName(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class Patronymic(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class Street(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class Main(models.Model):
    first_name = models.ForeignKey(to=FirstName, on_delete=models.CASCADE)
    last_name = models.ForeignKey(to=LastName, on_delete=models.CASCADE)
    patronymic = models.ForeignKey(to=Patronymic, on_delete=models.CASCADE)
    street = models.ForeignKey(to=Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10)
    building = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

    

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Changed from Role to role
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.BigIntegerField(default=0)  # Changed to BigIntegerField to store phone numbers correctly
    hire_date = models.DateField()
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.phone}"

    

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_class = models.CharField(max_length=20, default='Primary ')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    religion = models.CharField(max_length=10, choices=[('Islam', 'islam'), ('Christian', 'Christian')])
    address = models.CharField(max_length=30)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relationship})"



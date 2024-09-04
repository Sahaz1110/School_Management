from django import forms
from .models import Student

class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_class', 'date_of_birth', 'gender', 'religion', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

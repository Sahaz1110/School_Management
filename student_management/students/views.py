from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentEnrollmentForm
from .models import Student

def enroll_student(request):
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student data to the database
            return redirect('student_list')  # Redirect to the list of students or a success page
    else:
        form = StudentEnrollmentForm()
    return render(request, 'students/enroll_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

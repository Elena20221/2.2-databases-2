from django.shortcuts import render

from .models import Student,Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    context = {'students': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

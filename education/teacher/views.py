from django.shortcuts import render
from .models import Teacher


def index_view(request):
    teacher = Teacher.objects.get(pk=1)
    context = {
        'teacher': teacher,
        'all_teachers': Teacher.objects.all(),
    }
    return render(request, 'teacher/index.html', context=context)

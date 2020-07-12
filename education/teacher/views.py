from django.shortcuts import render
from .models import Teacher, Course, Lesson
from .forms import TeacherForm, LessonForm, CourseForm
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView


def index_view(request):
    teacher = Teacher.objects.get(pk=1)
    context = {
        'teacher': teacher,
        'all_teachers': Teacher.objects.all(),
    }
    return render(request, 'teacher/index.html', context=context)


class CreateTeacherView(View):

    def get(self, request):
        form = TeacherForm()
        return render(request, 'teacher/create_teacher_form.html', context={"form": form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'teacher/create_teacher_form.html', context={"form": form})


class TeacherCreateView(CreateView):

    model = Teacher
    fields = '__all__'
    success_url = '/cb_all_teachers/'

    def get_success_url(self):
        return f'/teacher_detail/{self.object.pk}'
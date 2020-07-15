from django.shortcuts import render
from .models import Teacher, Course, Lesson
from .forms import TeacherForm, LessonForm, CourseForm
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.base import View
from django.views.generic.list import ListView


def index_view(request):
    teacher = Teacher.objects.get(pk=1)
    context = {
        'teacher': teacher,
        'all_teachers': Teacher.objects.all(),
    }

    return render(request, 'teacher/contact.html', context=context)


class CreateTeacherView(View):

    def get(self, request):
        form = TeacherForm()
        return render(request, 'teacher/teacher_create.html', context={"form": form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'teacher/teacher_create.html', context={"form": form})


# all_teachers.html
class AllTeacherTemplateView(TemplateView):
    template_name = 'teacher/all_teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.all()
        context.update({"teachers": teachers})
        return context


# teacher_detail.html
class TeacherDetailView(DetailView):
    model = Teacher


# teacher_form.html
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = '/all_teachers/'

    def get_success_url(self):
        return f'/teacher_detail/{self.object.pk}'


# teacher_list.html
class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    paginate_by = 5


# teacher_confirm_delete.html
class TeacherDeleteView(DeleteView):
    model = Teacher
    fields = '__all__'
    success_url = '/all_teachers/'

    def get_success_url(self):
        return f'/teacher_detail/{self.object.pk}'


# LESSON
# Create lesson
class CreateLessonView(View):

    def get(self, request):
        form = LessonForm()
        return render(request, 'teacher/lesson_create.html', context={"form": form})

    def post(self, request):
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'teacher/lesson_create.html', context={"form": form})


# all_lessons.html
class AllLessonTemplateView(TemplateView):
    template_name = 'teacher/all_lessons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons = Lesson.objects.all()
        context.update({"lessons": lessons})
        return context


# lesson_detail.html
class LessonDetailView(DetailView):
    model = Lesson


# lesson_form.html
class LessonUpdateView(UpdateView):
    model = Lesson
    fields = '__all__'
    success_url = '/all_lessons/'

    def get_success_url(self):
        return f'/lesson_detail/{self.object.pk}'



# lesson_list.html
class LessonListView(ListView):
    model = Lesson
    context_object_name = 'lessons'
    paginate_by = 5


# lesson_confirm_delete.html
class LessonDeleteView(DeleteView):
    model = Lesson
    fields = '__all__'
    context_object_name = 'lessons'

    success_url = '/all_lessons/'

    def post(self, request):
        form = LessonForm(request.POST)
        if form.is_valid():
            form.delete()
        return render(request, 'teacher/all_lessons.html', context={"form": form})

    def get_success_url(self):
        return '/all_lessons/'


# Course
# Create course
class CreateCourseView(View):

    def get(self, request):
        form = CourseForm()
        return render(request, 'teacher/course_create.html', context={"form": form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'teacher/course_create.html', context={"form": form})


# all_courses.html
class AllCourseTemplateView(TemplateView):
    template_name = 'teacher/all_courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context.update({"courses": courses})
        return context


# course_detail.html
class CourseDetailView(DetailView):
    model = Course


# course_form.html
class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = '/all_courses/'

    def get_success_url(self):
        return f'/course_detail/{self.object.pk}'


# course_list.html
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 5


# course_confirm_delete.html
class CourseDeleteView(DeleteView):
    model = Course
    fields = '__all__'
    success_url = '/all_courses/'

    def get_success_url(self, request, pk):
        course = Course.objects.filter(pk=pk).first()
        form = CourseForm(instance=course)
        return render(request, 'teacher/course_confirm_delete.html', context={"form": form})

    def post(self, request, pk):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.delete()
        return render(request, 'teacher/all_courses.html', context={"form": form})

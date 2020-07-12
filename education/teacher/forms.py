from django.forms import ModelForm
from .models import Teacher, Lesson, Course


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
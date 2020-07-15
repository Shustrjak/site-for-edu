"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mynews.views as function_views
import mynews.views as news_views
import teacher.views as teacher_views
# import contact.views as contact_views


urlpatterns = [
    # fb_views
    path('fb_all_news/', function_views.all_articles),
    path('fb_create_article/', function_views.create_article),
    path('fb_delete_article/<int:pk>/', function_views.delete_article),
    path('fb_edit_article/<int:pk>/', function_views.edit_article),
    path('fb_show_article/<int:pk>/', function_views.show_article),

    # cb_views
    path('cb_create_author/', news_views.CreateAuthorView.as_view()),
    path('cb_all_authors/', news_views.AllAuthorsTemplateView.as_view()),
    path('cb_author_detail/<int:pk>/', news_views.AuthorDetailView.as_view()),
    path('cb_delete_author/', news_views.AuthorCreateView.as_view()),
    path('cb_author_list/', news_views.AuthorListView.as_view()),

    # cb Teacher
    path('teacher_create/', teacher_views.CreateTeacherView.as_view()),
    path('all_teachers/', teacher_views.AllTeacherTemplateView.as_view()),
    path('teacher_detail/<int:pk>/', teacher_views.TeacherDetailView.as_view()),
    path('teacher_upd/<int:pk>/', teacher_views.TeacherUpdateView.as_view()),
    path('teacher_list/', teacher_views.TeacherListView.as_view()),
    path('teacher_delete/<int:pk>/', teacher_views.TeacherDeleteView.as_view()),
    # cb Lesson
    path('lesson_create/', teacher_views.CreateLessonView.as_view()),
    path('all_lessons/', teacher_views.AllLessonTemplateView.as_view()),
    path('lesson_detail/<int:pk>/', teacher_views.LessonDetailView.as_view()),
    path('lesson_upd/<int:pk>/', teacher_views.LessonUpdateView.as_view()),
    path('lesson_list/', teacher_views.LessonListView.as_view()),
    path('lesson_delete/<int:pk>/', teacher_views.LessonDeleteView.as_view()),
    # cb Course
    path('course_create/', teacher_views.CreateCourseView.as_view()),
    path('all_courses/', teacher_views.AllCourseTemplateView.as_view()),
    path('course_detail/<int:pk>/', teacher_views.CourseDetailView.as_view()),
    path('course_upd/<int:pk>/', teacher_views.CourseUpdateView.as_view()),
    path('course_list/', teacher_views.CourseListView.as_view()),
    path('course_delete/<int:pk>/', teacher_views.CourseDeleteView.as_view()),

    # contacts.html
    # path('contact/contact.html', contact_views.FeedbackForm.contact_view),
    # default

    path('admin/', admin.site.urls),
    path('news/', include('mynews.urls')),
    path('teachers/', include('teacher.urls')),
    path('schedule/', include('schedule.urls')),
    path('contact/', include('contact.urls')),

]

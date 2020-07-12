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
import mynews.views as class_based_views
import teacher.views as based_views

urlpatterns = [
    # fb_views
    path('fb_all_news/', function_views.all_articles),
    path('fb_create_article/', function_views.create_article),
    path('fb_delete_article/<int:pk>/', function_views.delete_article),
    path('fb_edit_article/<int:pk>/', function_views.edit_article),
    path('fb_show_article/<int:pk>/', function_views.show_article),

    # cb_views
    path('cb_create_author/', class_based_views.CreateAuthorView.as_view()),
    path('cb_all_authors/', class_based_views.AllAuthorsTemplateView.as_view()),
    path('cb_author_detail/<int:pk>/', class_based_views.AuthorDetailView.as_view()),
    path('cb_create_author/', class_based_views.AuthorCreateView.as_view()),
    path('cb_author_list/', class_based_views.AuthorListView.as_view()),

    # cb Teacher, Course, Lesson
    path('cb_create_teacher/', based_views.CreateTeacherView.as_view()),

    # default

    path('admin/', admin.site.urls),
    path('news/', include('mynews.urls')),
    path('teachers/', include('teacher.urls')),
    path('schedule/', include('schedule.urls')),

]

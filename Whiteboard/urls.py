"""Whiteboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as logout
from .views import home_page, update_record, list_user, update, delete, my_info_page
from accounts.views import loginpage, registerpage
from django.contrib import admin
from django.urls import include, path

from courses.views import \
    course_details_page, \
    course_people, \
    courses, \
    enroll_course, \
    add_course, \
    unenroll_course, \
    update_course, \
    delete_course, \
    add_lesson, \
    lesson_page, \
    delete_lesson


urlpatterns = [
    path('', home_page, name='homepage'),
    path('logout/', logout.LogoutView.as_view(template_name="auth/logout.html"),
         name='logoutpage'),
    path('login/', loginpage, name='loginpage'),
    path('register/', registerpage, name="registerpage"),
    path('admin/', admin.site.urls),
    path('infopage/', my_info_page, name="myinfopage"),

    path('users/', list_user, name='list_user'),
    path('update/updaterecord/<int:id>', update_record, name='updaterecord'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    path('course/', courses, name="coursepage"),
    path('course/enroll/', enroll_course, name="enrollCourse"),
    path('course/unenroll/<int:id>', unenroll_course, name="unenrollCourse"),
    path('course/<int:id>', course_details_page, name='detailed'),
    path('course/<int:id>/people', course_people, name='people'),
    path('course/addlesson/<int:id>', add_lesson, name="addlessonpage"),
    path('addcourse/', add_course, name="addcoursepage"),
    path('editcourse/<int:id>', update_course, name="editcoursepage"),
    # path('updatecourse/<int:id>', update_course_record, name="updatecourse"),
    path('deletecourse/<int:id>', delete_course, name="deletecourse"),

    path('lessons/<int:id>', lesson_page, name="lessonspage"),
    path('deletelessons/<int:id>', delete_lesson, name="deletelessons"),

    # path('sections/', sectionspage, name="sectionspage"),
    # path('addsections/', addsections, name="addsectionspage"),
    # path('editsections/<int:id>', updatesections, name="editsectionspage"),
    # path('updatesections/<int:id>', updatesectionsrecord, name="updatesections"),
    # path('deletesections/<int:id>', deletesections, name="deletesections"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

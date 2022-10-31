from django.shortcuts import render, redirect
from accounts.models import User

from courses.forms import AddCourseForm, AddSectionForm, AddLessonForm, EnrollForm
from courses.models import Course, Section, Lesson

import random


def courses(request):
    user = User.objects.get(id=request.user.id)

    if not request.user.is_authenticated:
        return redirect('loginpage')

    if user.is_student:
        return render(request, "courses/student-courses.html", {
            'courses': user.courses.values(),
        })

    if request.GET.get('search'):
        search = request.GET.get('search')
        courses = Course.objects.filter(title__contains=search)
        return render(request, "courses/courses.html", {'courses': courses})

    if request.user.is_admin:
        courses = Course.objects.all()
        return render(request, "courses/courses.html", {'courses': courses})

    if user.is_professor:
        courses = Course.objects.filter(creator=user.id)
        return render(request, "courses/courses.html", {"courses": courses})


def course_people(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
        'students': course.students.all(),
    }
    return render(request, "courses/people.html", context)


def enroll_course(request):
    if request.method == "POST":
        form = EnrollForm(request.POST)
        user = User.objects.get(id=request.user.id)
        key = str(request.POST.get('key'))
        new_course = Course.objects.get(key=key)
        user.courses.add(new_course)
        new_course.students.add(user)
        user.save()
        new_course.save()
        return redirect('coursepage')

    form = EnrollForm()
    return render(request, "courses/enroll-course.html", {'form': form})


def unenroll_course(request, id):
    user = User.objects.get(id=request.user.id)
    course = Course.objects.get(id=id)
    user.courses.remove(course)
    user.save()
    return redirect('homepage')


def create_course_key(creator, title, desc):
    string = creator[:5] + title + desc[:5]
    l_string = list(string)
    random.shuffle(l_string)
    return "".join(l_string)


def add_course(request):
    form = AddCourseForm()
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.key = create_course_key(
                instance.creator.email,
                instance.title,
                instance.description
            ).strip()
            instance.save()
            return render(request, "courses/successcourse.html", {
                'form1': form,
                'key': instance.key,
            })
    form = AddCourseForm()
    return render(request, "courses/addcourse.html", {'form': form})


def update_course(request, id):
    course = Course.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        course.title = title
        course.description = description
        course.save()
        return redirect('detailed', id)

    context = {
        'course': course
    }
    return render(request, 'courses/editcourse.html', context)


# def update_course_record(request, id):
#     course = Course.objects.get(id=id)
#     form = AddCourseForm(request.POST, instance=course)
#     if form.is_valid():
#         form.save()
#         return redirect("coursepage")

#     return render(request, 'courses/editcourse.html', {'course': course})


def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("coursepage")


def course_details_page(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
        'lessons': course.lessons.values(),
    }

    return render(request, "courses/detail.html", context)


# def sectionspage(request):
#     section = Section.objects.all()
#     if request.user.is_authenticated:
#         return render(request, "sections/sections.html", {'sections': section})
#     else:
#         return redirect('loginpage')


# def addsections(request):
#     if request.method == "POST":
#         form = AddSectionForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, "sections/successsections.html", {'form1': form})
#     form = AddSectionForm()
#     return render(request, "sections/addsections.html", {'form': form})


# def updatesections(request, id):
#     section = Section.objects.get(id=id)
#     context = {
#         'section': section
#     }
#     return render(request, 'sections/editsections.html', context)


# def updatesectionsrecord(request, id):
#     section = Section.objects.get(id=id)
#     form = AddSectionForm(request.POST, instance=section)
#     if form.is_valid():
#         form.save()
#         return redirect("sectionspage")

#     return render(request, 'sections/editsections.html', {'section': section})


# def deletesections(request, id):
#     section = Section.objects.get(id=id)
#     section.delete()
#     return redirect("sectionspage")


def lesson_page(request, id):
    lesson = Lesson.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, "lessons/lessons.html", {'lesson': lesson})
    else:
        return redirect('loginpage')


def add_lesson(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = AddLessonForm(request.POST)
        new_lesson = Lesson.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        course.lessons.add(new_lesson)
        if form.is_valid():
            course.save()

        return redirect('homepage')
    form = AddLessonForm()
    context = {
        'form': form,
        'course': course,
    }

    return render(request, "lessons/addlessons.html", context)


def delete_lesson(request, id):
    lesson = Lesson.objects.get(id=id)
    lesson.delete()
    return redirect('coursepage')

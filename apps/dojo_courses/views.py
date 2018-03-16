# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    form = CourseForm()
    courses = Course.objects.all()
    return render(request, "dojo_courses/index.html", {"form": form, "courses": courses})

def destroy(request, id):
    course = Course.objects.get(id=id)
    return render(request, "dojo_courses/destroy.html", {"course": course})

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect(index)

def add(request):
    if request.method != "POST":
        return redirect(index)
    form = CourseForm(request.POST)
    if form.is_valid():
        new_course = form.save()
        return redirect(show, id=new_course.id)
    return redirect(index)

def show(request, id):
    course = Course.objects.get(id=id)
    form = CommentForm()
    comments = course.comments.all()
    return render(request, "dojo_courses/show.html", {"course": course, "form": form, "comments": comments})

def comment(request, id):
    if request.method != "POST":
        return redirect(show, id=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.course = Course.objects.get(id=id)
        new_comment.save()
    return redirect(show, id=id)
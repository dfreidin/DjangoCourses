# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content": _("Comment")}
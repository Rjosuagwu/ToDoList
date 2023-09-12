from django import forms
from .models import Task
from django.shortcuts import get_object_or_404


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']


class TaskFormUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

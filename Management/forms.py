from django import forms
from .models import Task, Command

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'status','task_image',]


class CommandForm(forms.ModelForm):
    class Meta:
        model = Command
        fields = ['message', ]

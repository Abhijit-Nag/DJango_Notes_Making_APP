from asyncio import tasks
from dataclasses import fields
from importlib.metadata import files
from multiprocessing import context
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class TaskList(ListView):
   model=Task
   context_object_name='tasks'

class TaskDetail(DetailView):
    model =Task
    context_object_name = 'task'
    template_name='base/task_detail.html'

class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
   model= Task
   fields='__all__'
   success_url=reverse_lazy('tasks')

class DeleteView(DeleteView):
   model=Task
   context_object_name='task'
   success_url = reverse_lazy('tasks')
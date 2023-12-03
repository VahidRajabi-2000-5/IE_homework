from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Task,Command
from .forms import TaskForm,CommandForm


# @login_required
# def task_list(request):
#     tasks = Task.objects.filter(user=request.user)
#     print(tasks)
#     return render(request,'Management/task_list.html',{'tasks':tasks})
# =======================================================
# @login_required
# def task_detail(request,pk):
#     task = get_object_or_404(Task,pk=pk)
#     return render(request,'Management/task_detail.html',{'task':task})


class TaskListView(LoginRequiredMixin,generic.ListView):
    template_name = 'Management/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-deadline')




class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'Management/task_detail.html'
    context_object_name = 'task'
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        task = self.get_object()
        context['commands'] = task.commands.all()
        context['command_form'] = CommandForm()
        # context['task_user'] = task.user
        return context
    
class CreateTaskView(LoginRequiredMixin, generic.CreateView):
    form_class = TaskForm
    template_name = 'Management/create_task.html'
    context_object_name='form'
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model=Task
    form_class = TaskForm
    template_name = 'Management/create_task.html'
    context_object_name='form'
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    

class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model=Task
    template_name = 'Management/delete_task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
    

class CommandCreateView(LoginRequiredMixin,generic.CreateView):
    model = Command
    form_class=CommandForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        task_id = int(self.kwargs['pk'])
        obj.task = get_object_or_404(Task,id=task_id)
        return super().form_valid(form)
        
    
    
    



# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'create_task.html', {'form': form})

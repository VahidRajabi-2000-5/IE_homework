from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Task(models.Model):
    PRIORITY_CHOICES = (
        ('1','Low'),
        ('2','Medium'),
        ('3','High'),
    )
    STATUS_CHOICES = (
        ('todo', 'To Do'), 
        ('in_progress', 'In Progress'), 
        ('done', 'Done'),   
    )
    
    task_image = models.ImageField("task_image", upload_to="task_cover/",blank=True)
    
    user = models.ForeignKey(get_user_model(), verbose_name="tasks", on_delete=models.CASCADE)
    title = models.CharField("title", max_length=300)
    description=models.TextField("description")
    priority = models.CharField("priority", choices=PRIORITY_CHOICES,  max_length=20)
    status = models.CharField("priority", choices=STATUS_CHOICES,  max_length=20)
    deadline = models.DateTimeField("deadline")
    datetime_created = models.DateTimeField("datetime_created",auto_now_add=True)
    datetime_modified = models.DateTimeField("datetime_modified",auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    
    
class Command(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name="commands", on_delete=models.CASCADE,related_name='commands')
    task = models.ForeignKey(Task, verbose_name="commands", on_delete=models.CASCADE,related_name='commands')
    message = models.TextField("message")
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.task.title}"
    
    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.task.id})
    
    

    
    
    
    
    
    
    
    
    
    
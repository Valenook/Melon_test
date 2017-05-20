from django.db import models
from django.utils import timezone

# Create your models here.
class Branch(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=32)
    task_branch = models.ForeignKey(Branch, null='True')
    text = models.TextField()
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment_text = models.TextField()
    comment_task = models.ForeignKey(Task)
    def __str__(self):
        return self.comment_text    
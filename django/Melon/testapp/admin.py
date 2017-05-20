from django.contrib import admin
from testapp.models import Task, Comment, Branch

# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Branch)
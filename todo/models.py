from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=200,blank=False, default='')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
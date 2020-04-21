from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200, null=False, help_text="할 일을 채워주세요!")
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task

# Create your models here.

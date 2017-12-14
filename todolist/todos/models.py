from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    todolist = models.ForeignKey(
        TodoList, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

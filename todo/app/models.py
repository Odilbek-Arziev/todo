from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=255)
    is_done = models.BooleanField()

    def __str__(self):
        return f"{'Выполнено' if self.is_done else 'Не выполнено'} - {self.text}"

from djongo import models
# we have to import models from djongo rather then importing from django


class Todo(models.Model):
    todo = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

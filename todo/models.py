from djongo import models
# we have to import models from djongo rather then importing from django


class Todo(models.Model):
    headline = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

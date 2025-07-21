from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Head(models.Model):
    head = models.CharField(max_length=200, null=False, blank=False)
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.head

class Todo(models.Model):
    head = models.ForeignKey(Head, on_delete=models.CASCADE, related_name='todos')
    title = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models


class CoursesManager(models.Manager):  # Создание моделей для Lessons
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
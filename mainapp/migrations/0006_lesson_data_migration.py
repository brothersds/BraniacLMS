# Generated by Django 4.1.1 on 2022-10-06 23:47

from django.db import migrations


def forwards_func(apps, schema_editor):
# Get model
    lesson = apps.get_model("mainapp", "Lesson")
    courses = apps.get_model("mainapp", "Courses")
# Create model's objects
    for item in courses.objects.all():
        lesson.objects.create(
            course=item,
            num=1,
            title="Lesson 1",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=2,
            title="Lesson 2",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=3,
            title="Lesson 3",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=4,
            title="Lesson 4",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=5,
            title="Lesson 5",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=6,
            title="Lesson 6",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=7,
            title="Lesson 7",
            description="Описание урока",
            description_as_markdown=False,
        )
        lesson.objects.create(
            course=item,
            num=8,
            title="Lesson 8",
            description="Описание урока",
            description_as_markdown=False,
        )


def reverse_func(apps, schema_editor):
# Get model
    lesson = apps.get_model("mainapp", "Lesson")
# Delete objects
    lesson.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_courses_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
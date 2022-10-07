# Generated by Django 4.1.1 on 2022-10-07 07:32

from django.db import migrations


def forwards_func(apps, schema_editor):
# Get model
    teacher = apps.get_model("mainapp", "CourseTeachers")
    courses = apps.get_model("mainapp", "Courses")

# Create model's objects
    for item_t in teacher.objects.all():
        for item_c in courses.objects.all():
            if item_t.pk == 1 and (item_c.pk == 1 or item_c.pk == 3):
                added(item_t, item_c)
            elif item_t.pk == 2 and (item_c.pk == 2 or item_c.pk == 4):
                added(item_t, item_c)
            elif item_t.pk == 3 and (item_c.pk == 3 or item_c.pk == 5):
                added(item_t, item_c)
            elif item_t.pk == 4 and (item_c.pk == 4 or item_c.pk == 6):
                added(item_t, item_c)
            elif item_t.pk == 5 and (item_c.pk == 5 or item_c.pk == 7):
                added(item_t, item_c)
            elif item_t.pk == 6 and (item_c.pk == 6 or item_c.pk == 8):
                added(item_t, item_c)
            elif item_t.pk == 7 and (item_c.pk == 1 or item_c.pk == 8):
                added(item_t, item_c)
            else:
                continue


def added(item_t, item_c):
    return item_t.course.add(item_c)


def reverse_func(apps, schema_editor):
# Get model
    teacher = apps.get_model("mainapp", "CourseTeachers")
    courses = apps.get_model("mainapp", "Courses")
# Delete objects
    teacher.objects.all().delete()
    courses.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0008_teachers_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
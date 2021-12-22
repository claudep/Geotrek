# Generated by Django 3.1.13 on 2021-10-08 10:03

from django.db import migrations, models


def migrate_one_parent_site_to_multiple_parent_sites(apps, schema):
    course_model = apps.get_model('outdoor', 'Course')
    courses = course_model.objects.all()
    for course in courses:
        if hasattr(course, 'site') and hasattr(course, 'parent_sites'):
            course.parent_sites.set([course.site])


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0030_auto_20211004_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='parent_sites',
            field=models.ManyToManyField(related_name='children_courses_tmp', to='outdoor.Site', verbose_name='Sites'),
        ),
        migrations.RunPython(migrate_one_parent_site_to_multiple_parent_sites, reverse_code=migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='course',
            name='site',
        ),
        migrations.AlterField(
            model_name='course',
            name='parent_sites',
            field=models.ManyToManyField(related_name='children_courses', to='outdoor.Site', verbose_name='Sites'),
        ),
    ]

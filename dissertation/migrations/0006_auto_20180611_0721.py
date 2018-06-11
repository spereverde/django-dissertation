# Generated by Django 2.0.6 on 2018-06-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0005_dissertationcluster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dissertationcluster',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='dissertationcluster',
            name='diss',
        ),
        migrations.AddField(
            model_name='cluster',
            name='dissertation',
            field=models.ManyToManyField(to='dissertation.Dissertation'),
        ),
        migrations.DeleteModel(
            name='DissertationCluster',
        ),
    ]
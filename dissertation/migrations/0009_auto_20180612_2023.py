# Generated by Django 2.0.6 on 2018-06-12 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0008_auto_20180611_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clusterpersonrole',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='clusterpersonrole',
            name='person',
        ),
        migrations.RemoveField(
            model_name='clusterpersonrole',
            name='role',
        ),
        migrations.RemoveField(
            model_name='person',
            name='active',
        ),
        migrations.AddField(
            model_name='dissertation',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dissertation',
            name='person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dissertation.Person'),
        ),
        migrations.AddField(
            model_name='dissertation',
            name='preference_set',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ClusterPersonRole',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]

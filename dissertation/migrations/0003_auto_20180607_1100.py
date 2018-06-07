# Generated by Django 2.0.6 on 2018-06-07 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0002_dissertation_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DissertationMatched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DissertationPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dissertation',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dissertation',
            name='description',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='dissertationpreference',
            name='diss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Dissertation'),
        ),
        migrations.AddField(
            model_name='dissertationpreference',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Person'),
        ),
        migrations.AddField(
            model_name='dissertationmatched',
            name='diss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Dissertation'),
        ),
        migrations.AddField(
            model_name='dissertationmatched',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Person'),
        ),
    ]

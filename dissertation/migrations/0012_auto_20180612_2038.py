# Generated by Django 2.0.6 on 2018-06-12 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0011_auto_20180612_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dissertationpreference',
            name='person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dissertation.Person'),
        ),
    ]

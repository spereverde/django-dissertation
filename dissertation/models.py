from django.db import models


class Dissertation(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Person(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

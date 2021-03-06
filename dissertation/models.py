from django.db import models
from django.urls import reverse

class Dissertation(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=600, default='')
    active = models.BooleanField(default=False)
    # pub_date = models.DateTimeField(null=True, blank=True)
    # cluster = ManyToManyField('Cluster')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dissertation-detail', kwargs={'diss_id': self.pk})


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Cluster(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()
    dissertation = models.ManyToManyField('Dissertation')

    def __str__(self):
        return self.name


class DissertationPreference(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    diss = models.ForeignKey(Dissertation, on_delete=models.CASCADE)
    CHOICES = [(i,i) for i in range(1,11)]
    priority = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return "{} - {} - {}".format(self.person, self.diss, self.priority)


class DissertationMatched(models.Model):
    diss = models.ForeignKey(Dissertation, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.person, self.diss)
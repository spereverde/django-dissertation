from django.db import models


class Dissertation(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=600, default='')
    active = models.BooleanField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Cluster(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Role(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role

class ClusterPersonRole(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.cluster, self.person, self.role)


class DissertationCluster(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    diss = models.ForeignKey(Dissertation, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.cluster, self.diss)

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
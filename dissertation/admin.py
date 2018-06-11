from django.contrib import admin

from .models import Cluster, Dissertation, Person, Role, DissertationMatched, DissertationPreference, ClusterPersonRole

admin.site.register(Cluster)
admin.site.register(Dissertation)
admin.site.register(Person)
admin.site.register(Role)
# admin.site.register(DissertationCluster)
admin.site.register(DissertationPreference)
admin.site.register(DissertationMatched)
admin.site.register(ClusterPersonRole)
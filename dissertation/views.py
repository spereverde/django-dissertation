from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Dissertation, Cluster, DissertationCluster


# def dissertation_list(request):
#     # import pdb; pdb.set_trace()
#     dlist = Dissertation.objects.order_by('title')
#     context = {'dlist': dlist}
#     return render(request, 'dissertation/index.html', context)
    
def detail(request, diss_id):
    diss = get_object_or_404(Dissertation, pk=diss_id)
    return render(request, 'dissertation/detail.html', {'diss': diss})

# def cluster_list(request):
#     clist = Cluster.objects.order_by('name')
#     context = {'clist': clist}
#     return render(request, 'cluster/index.html', context)

def cluster_detail(request, cluster_id):
    cluster = get_object_or_404(Cluster, pk=cluster_id)
    return render(request, 'cluster/detail.html', {'cluster': cluster})

class DissertationList(ListView):
    model = Dissertation

class ClusterList(ListView):
    model = Cluster

class DissPerClusterList(ListView):
    model = DissertationCluster

class DissByClusterList(ListView):

    template_name = 'dissertations_by_cluster.html'

    def get_queryset(self):
        self.cluster = get_object_or_404(Cluster, name=self.kwargs['cluster'])
        return DissertationCluster.objects.filter(cluster=self.cluster)
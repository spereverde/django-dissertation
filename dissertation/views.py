from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Dissertation, Cluster


def dissertation_detail(request, diss_id):
    diss = get_object_or_404(Dissertation, pk=diss_id)
    return render(request, 'dissertation/detail.html', {'diss': diss})

def cluster_detail(request, cluster_id):
    cluster = get_object_or_404(Cluster, pk=cluster_id)
    # import pdb; pdb.set_trace()
    return render(request, 'cluster/detail.html', {'cluster': cluster})



class DissertationCreate(CreateView):
    model = Dissertation
    fields = ['title', 'description']


class DissertationList(ListView):
    model = Dissertation


class ClusterList(ListView):
    model = Cluster



class ClusterWithActiveDiss(ListView):
    context_object_name = 'dpc'
    queryset = Cluster.objects.filter(dissertation__active=True)
    template_name = 'cluster/active_diss.html'

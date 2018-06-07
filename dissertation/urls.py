from django.urls import path

from . import views

urlpatterns = [
    # ex: /diss/
    path('diss/', views.dissertation_list, name='dissertation_list'),
    # ex: /diss/5/
    path('diss/<int:diss_id>/', views.detail, name='detail'),
    # ex: /diss/5/results/
    path('diss/<int:diss_id>/results/', views.results, name='results'),
    # ex: /diss/5/vote/
    path('diss/<int:diss_id>/vote/', views.vote, name='vote'),
]
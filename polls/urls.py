from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('poll/<int:pk>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:pk>/vote/', views.poll_vote, name='poll_vote'),
    path('poll/<int:pk>/results/', views.poll_results, name='poll_results'),
    path('register/', views.register, name='register'),
    path('my-votes/', views.my_votes, name='my_votes'), 
]

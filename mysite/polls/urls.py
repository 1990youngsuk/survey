from django.urls import path, include
from . import views

app_name = 'polls'

'''
# generic view version
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''

# original view version (hard)
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('polls/', views.survey, name='index'),
    # ex: /polls/5
    path('polls/<int:question_id>/', views.detail, name='detail'),
    # ex: polls/5/results
    path('polls/<int:question_id>/results/', views.results, name='results'),
    # ex: polls/5/vote/
    path('polls/<int:question_id>/vote', views.vote, name='vote'),
]

from django.urls import path

from . import views


urlpatterns = [
    path('', views.jobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', views.jobDetailView.as_view(), name='job_detail'),
    path('jobs/create/', views.jobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/update/', views.jobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', views.jobDeleteView.as_view(), name='job_delete'),
    path('my-jobs/', views.myJobListView.as_view(), name='my_jobs'),
    path('job/<int:pk>/apply/', views.apply_to_job, name='apply_to_job'),
    path('my-applications/', views.myApplicationsListView.as_view(), name='my_applications'),
]
from django.urls import path
from .views import (
    CompanyListAPIView,
    CompanyDetailView,
    CompanyJobsListAPIView,
    CompanyJobsDetailView,
    CompanyJobsAddAPIView,
    JobsListAPIView,
    JobsAddAPIView,
    CommantAPIView,
    CompanyAddAPIView,

)

urlpatterns = [
    path("company-list/", CompanyListAPIView.as_view()),
    path("company-add/", CompanyAddAPIView.as_view()),
    path("company-detail/<int:pk>/", CompanyDetailView.as_view()),
    path("company-jobs-list/", CompanyJobsListAPIView.as_view()),
    path("company-jobs-add/", CompanyJobsAddAPIView.as_view()),
    path("company-jobs-detail/<int:pk>/", CompanyJobsDetailView.as_view()),
    path("jobs/", JobsListAPIView.as_view()),
    path("commant/", CommantAPIView.as_view()),
    path("jobs-add/", JobsAddAPIView.as_view()),
]

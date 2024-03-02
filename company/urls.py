from django.urls import path
from .views import (
    CompanyListAPIView,
    CompanyDetailAPIView,
    CompanyJobsListAPIView,
    CompanyJobsDetailAPIView,
    JobsListAPIView,
    JobsDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView
)

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('company-jobs/', CompanyJobsListAPIView.as_view(), name='company-jobs-list'),
    path('company-jobs/<int:pk>/', CompanyJobsDetailAPIView.as_view(), name='company-jobs-detail'),
    path('jobs/', JobsListAPIView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>/', JobsDetailAPIView.as_view(), name='jobs-detail'),
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]

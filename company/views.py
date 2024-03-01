from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, CompanyJobs, Jobs,Comment
from .serializers import CompanySerializer, CompanyJobsSerializer, JobsSerializer,CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser



from rest_framework.pagination import PageNumberPagination

class CommentPagination(PageNumberPagination):
    page_size = 10  # You can set the number of comments per page here
    page_size_query_param = 'page_size'
    max_page_size = 100

class CompanyListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination 
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


class CompanyAddAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailView(APIView):
    permission_classes = [IsAdminUser]
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyJobsListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        company_jobs = CompanyJobs.objects.all()
        serializer = CompanyJobsSerializer(company_jobs, many=True)
        return Response(serializer.data)


class CompanyJobsAddAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = CompanyJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyJobsDetailView(APIView):
    permission_classes = [IsAdminUser]
    def get_object(self, pk):
        try:
            return CompanyJobs.objects.get(pk=pk)
        except CompanyJobs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company_jobs = self.get_object(pk)
        serializer = CompanyJobsSerializer(company_jobs)
        return Response(serializer.data)

    def put(self, request, pk):
        company_jobs = self.get_object(pk)
        serializer = CompanyJobsSerializer(company_jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company_jobs = self.get_object(pk)
        company_jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobsListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination 
    def get(self, request, *args, **kwargs):
        company_id = request.GET.get("company")
        job_type_id = request.GET.get("job_type")

        if not company_id or not job_type_id:
            return Response(
                {"error": "Both company and job_type parameters are required"},
                status=400,
            )

        try:
            jobs = Jobs.objects.filter(company_id=company_id, job_type_id=job_type_id)
            serializer = JobsSerializer(jobs, many=True)
            return Response(serializer.data)
        except Jobs.DoesNotExist:
            return Response(
                {"error": "No jobs found for the given parameters"}, status=404
            )

class JobsAddAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommantAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CommentPagination  # Add pagination class here

    def get(self, request, *args, **kwargs):
        job_id = request.GET.get("job_id")
        if not job_id:
            return Response({"error": "job_id parameter is required"}, status=400)
        try:
            comments = Comment.objects.filter(job_id=job_id)
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(comments, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Comment.DoesNotExist:
            return Response({"error": "No comments found for the given job_id"}, status=404)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
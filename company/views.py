from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, CompanyJobs, Jobs, Comment
from .serializers import CompanySerializer, CompanyJobsSerializer, JobsSerializer, CommentSerializer

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
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
    def get(self, request):
        company_jobs = CompanyJobs.objects.all()
        serializer = CompanyJobsSerializer(company_jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CompanyJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CompanyJobsDetailAPIView(APIView):
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
    def get(self, request):
        jobs = Jobs.objects.all()
        serializer = JobsSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class JobsDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs)
        return Response(serializer.data)
    
    def put(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        jobs = self.get_object(pk)
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CommentListAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
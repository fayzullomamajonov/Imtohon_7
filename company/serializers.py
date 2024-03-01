from rest_framework import serializers
from .models import Company,CompanyJobs,Jobs,Comment

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyJobs
        fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
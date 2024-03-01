from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    directory = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CompanyJobs(models.Model):
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.job_type


class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    job_type = models.ForeignKey(CompanyJobs, on_delete=models.CASCADE)
    job_description = models.TextField()
    job_salary = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title


class Comment(models.Model):
    comment = models.TextField()
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:20]

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='logos/')
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=200)
    application_link = models.URLField()

    def __str__(self):
        return self.title

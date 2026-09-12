from django.db import models
from django.conf   import settings

class job(models.Model):
    title = models.CharField(max_length=200)
    Company_name = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_posted'] 
    
    
    def __str__(self):
        return self.title
    
    
class application(models.Model):
    job = models.ForeignKey(job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('job', 'applicant')
    
    def __str__(self):
        return f"{self.applicant} applied for {self.job}"
    

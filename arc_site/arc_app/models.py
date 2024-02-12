from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # New field for video URL
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# contact page
    # contact_form_app/models.py
class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    #theme = models.TextField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"


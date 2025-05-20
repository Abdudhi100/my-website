from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    base_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='public/images/', blank=True, null=True)
    

    def __str__(self):
        return self.title

# Existing models...

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    description = models.TextField(blank=True, null=True)
    certificate_image = models.ImageField(upload_to='public/certificates/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.degree


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    certificate_image = models.ImageField(upload_to='public/certificates/', blank=True, null=True)  # Add image field
    pdf_file = models.FileField(upload_to='certificates/pdfs/') 
    
    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return self.position


class Skill(models.Model):
    name = models.CharField(max_length=255)
    proficiency = models.CharField(
        max_length=50,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]
    )
    

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
      # Add image field

    def __str__(self):
        return self.name




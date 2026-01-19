from django.db import models

class Category(models.TextChoices):
    TECHNOLOGY = "Technology", "Technology"
    LIFESTYLE = "Lifestyle", "Lifestyle"
    EDUCATION = "Education", "Education"
    TRAVEL = "Travel", "Travel"
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=Category.choices)
    tags = models.ManyToManyField(Tag, related_name="posts")  # ✅ FIXED
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
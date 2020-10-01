from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 3000)
    postDate = models.DateField(blank = True)
    text = models.TextField()

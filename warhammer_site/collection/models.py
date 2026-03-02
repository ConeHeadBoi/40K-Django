from django.db import models

# Create your models here.
class Miniature(models.Model):
    image = models.ImageField(upload_to='miniatures/', blank=True, null=True)
    name = models.CharField(max_length=100)
    faction = models.CharField(max_length=100)
    points = models.IntegerField()
    description = models.TextField()
    painted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Faction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Miniature(models.Model):
    image = models.ImageField(upload_to='miniatures/', blank=True, null=True)
    name = models.CharField(max_length=100)

    faction = models.ForeignKey(
        Faction,
        on_delete=models.CASCADE
    )

    points = models.IntegerField()
    description = models.TextField()
    PAINTING_STAGES = [
        ('unbuilt', 'Unbuilt'),
        ('built', 'Built'),
        ('primed', 'Primed'),
        ('painting', 'Painting'),
        ('finished', 'Finished'),
    ]
    painting_stage = models.CharField(
        max_length=20,
        choices=PAINTING_STAGES,
        default='unbuilt'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
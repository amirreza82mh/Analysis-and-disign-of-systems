from django.db import models
from users.models import User

class Artwork(models.Model):
    RATING_CHOICES = [
        (0, 'Not Rated'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
     
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork_id = models.AutoField(primary_key=True)
    artwork_name = models.CharField(max_length = 50, null=False)
    description = models.TextField(null=False)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0, null=False)
    picture = models.ImageField(upload_to='home/picture/' ,null=False, blank=False)
    creation_time = models.TimeField(auto_now_add=True)


class Exhibition(models.Model):
    exhibition_id = models.AutoField(primary_key=True)
    exhibition_name = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(default=20)
    exhibition_place = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    picture =   picture = models.ImageField(upload_to='home/picture' ,null=False, blank=False)
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)

class Sans(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateField()

    class Meta:
        unique_together = (('exhibition', 'start_time', 'finish_time'),)

class Artwork_Exhibition_Curator(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('exhibition', 'artwork', 'curator'),)

class Exhibition_Viewer(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('exhibition', 'viewer'),)
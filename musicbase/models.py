from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + '-' + self.artist
    
class music(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100,blank=True)
    date_uploaded = models.DateTimeField(blank=True)
    likes = models.IntegerField(default=0, blank=True)
    art = models.ImageField(upload_to='static/image')
    audio = models.FileField(upload_to='media/audio')

    def __str__(self):
       return self.title

class playlist (models.Model):
    name = models.CharField(max_length=50)
    art = models.ImageField(upload_to='static/images')
    music = models.ForeignKey(music, on_delete=models.CASCADE, )

    def __str__(self) -> str:
        return self.name

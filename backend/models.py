from django.db import models

class albumsData(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # This assumes you're handling image uploads
    desc = models.TextField()
    bgColor = models.CharField(max_length=15) 
    def __str__(self):
        return self.name


class songsData(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Field for storing the song image
    file = models.FileField(upload_to='songs/')     # Field for storing the audio file
    desc = models.TextField()
    duration = models.CharField(max_length=5)   

    def __str__(self):
        return self.name
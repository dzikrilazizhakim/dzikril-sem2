from django.db import models

class Pengaturan(models.Model):
    nama = models.CharField(max_length=100)
    nilai = models.TextField()
    
    def __str__(self):
        return self.nama
from django.db import models

# Create your models here.
class Pengguna(models.Model):
    nama = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('satpam', 'Satpam'),
        ('tamu', 'Tamu'),
    ])

    def __str__(self):
        return self.nama


class Satpam(models.Model):
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=20, unique=True)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    shift = models.CharField(max_length=20, choices=[
        ('pagi', 'Pagi'),
        ('siang', 'Siang'),
        ('malam', 'Malam'),
    ])

    def __str__(self):
        return self.nama
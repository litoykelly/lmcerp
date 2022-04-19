from django.db import models

# Create your models here.
class Grade(models.Model):
    nom = models.CharField(max_length=50)
    sigle = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Fonction(models.Model):
    nom = models.CharField(max_length=50)
    sigle = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return self.nom + ' ' + self.postnom

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, post_save


class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    favoritos = models.IntegerField(default=0)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class PeliculaFavorita(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pelicula.titulo} - {self.usuario.username}'


def update_favoritos(sender, instance, **kwargs):
    count = instance.pelicula.peliculafavorita_set.all().count()
    instance.pelicula.favoritos = count
    instance.pelicula.save()


# en el post delete se pasa la copia de la instance que ya no existe
post_save.connect(update_favoritos, sender=PeliculaFavorita)
post_delete.connect(update_favoritos, sender=PeliculaFavorita)

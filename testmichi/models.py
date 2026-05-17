from django.db import models


class Gato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255, help_text="Nombre del archivo GIF")

    class Meta:
        verbose_name_plural = "Gatos"

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    texto = models.TextField()
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return f"{self.orden}. {self.texto[:50]}..."


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    texto = models.TextField()
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, related_name='respuestas')

    class Meta:
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return f"{self.texto[:30]}... -> {self.gato.nombre}"

from django.db import models
from blog.settings import BASE_DIR

class Noticia (models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='noticias/img', blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo
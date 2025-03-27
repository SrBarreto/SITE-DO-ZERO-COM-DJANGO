from django.db import models

class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    arquivo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    link = models.URLField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)

    def __str__(self):
        return self.nome

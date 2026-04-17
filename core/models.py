from django.db import models


class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    imagem = models.ImageField(upload_to='banners/')
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo


class RedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()
    icone = models.CharField(max_length=50, blank=True, help_text="Ex.: instagram, facebook, whatsapp")
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    promocao = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
from django.db import models


class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    imagem = models.ImageField(upload_to='banners/')
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo


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


class SecaoHome(models.Model):
    TIPOS_SECAO = [
        ('produtos', 'Produtos'),
        ('texto', 'Texto'),
        ('texto_imagem', 'Texto com imagem'),
        ('chamada', 'Chamada para ação'),
    ]

    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=30, choices=TIPOS_SECAO, default='produtos')
    titulo = models.CharField(max_length=200, blank=True, null=True)
    subtitulo = models.CharField(max_length=300, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='secoes/', blank=True, null=True)
    botao_texto = models.CharField(max_length=100, blank=True, null=True)
    botao_link = models.CharField(max_length=300, blank=True, null=True)
    produtos = models.ManyToManyField(Produto, blank=True, related_name='secoes_home')
    ativa = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'id']
        verbose_name = 'Seção da Home'
        verbose_name_plural = 'Seções da Home'

    def __str__(self):
        return f"{self.ordem} - {self.nome}"
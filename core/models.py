from django.db import models

# --------------------------
# MODELOS PRINCIPAIS
# --------------------------

class Beneficio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    publico_alvo = models.CharField(max_length=100, null=True, blank=True)
    valor_subsidiado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Associado(models.Model):
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=30, null=True, blank=True)
    nome_completo = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=40, null=True, blank=True)
    genero = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    fk_beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo


class Autor(models.Model):
    nome = models.CharField(max_length=80)
    perfil = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    cep = models.CharField(max_length=15)
    logradouro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=80)
    bairro = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    uf = models.CharField(max_length=2)
    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fk_associado = models.ForeignKey(Associado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.logradouro}, {self.numero or ''}"


class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


# --------------------------
# NOTÍCIAS
# --------------------------

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(default='Sem resumo')
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)

    DESTAQUE_CHOICES = [
        ('nenhum', 'Nenhum'),
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
        ('maximo', 'Máximo'),
    ]
    destaque = models.CharField(max_length=10, choices=DESTAQUE_CHOICES, default='nenhum')

    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


# --------------------------
# CONTATOS
# --------------------------

class Telefone(models.Model):
    telefone = models.CharField(max_length=20, null=True, blank=True)
    fk_associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefone


class Email(models.Model):
    email = models.CharField(max_length=100, unique=True)
    fk_associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


# --------------------------
# BENEFÍCIOS
# --------------------------

class TipoBeneficio(models.Model):
    tipo_beneficio = models.CharField(max_length=80)
    ativo = models.BooleanField(default=True)
    fk_beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_beneficio


class GestorBeneficio(models.Model):
    cnpj = models.CharField(max_length=20, unique=True)
    ie = models.CharField(max_length=20, null=True, blank=True)
    nome = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=50, null=True, blank=True)
    contato = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    fk_telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    fk_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

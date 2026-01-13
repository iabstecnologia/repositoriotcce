from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.text import slugify
from datetime import date
from django.utils import timezone

# Importa o modelo User customizado do projeto (apps.accounts.User)
from django.contrib.auth import get_user_model
User = get_user_model()


# Funções de Upload
def item_file_path(instance, filename):
    """
    Define o caminho de upload do arquivo: repositorio/projeto_slug/subprojeto_slug/MES/DIA/nome_do_arquivo.
    """
    # Garante slugs seguros para o sistema de arquivos e URL
    projeto_slug = slugify(instance.subprojeto.projeto.nome) if instance.subprojeto.projeto.nome else 'sem_projeto'
    subprojeto_slug = slugify(instance.subprojeto.nome) if instance.subprojeto.nome else 'sem_subprojeto'

    # ----------------------------------------------------
    # NOVO: Obtém a data atual no momento do upload
    hoje = timezone.now()
    mes_str = hoje.strftime('%m')  # Número do mês com zero à esquerda (ex: 09)
    dia_str = hoje.strftime('%d')  # Número do dia com zero à esquerda (ex: 26)
    # ----------------------------------------------------

    return f"repositorio/{projeto_slug}/{subprojeto_slug}/{mes_str}/{dia_str}/{filename}"


# Modelos Auxiliares (Metadados e Estrutura)
class Projeto(models.Model):
    """Representa o projeto guarda-chuva (ex: TCCE I/2018)."""
    nome = models.CharField(max_length=150, unique=True, verbose_name="Nome do Projeto")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Subprojeto(models.Model):
    """Representa uma sub-coleção dentro de um projeto maior."""
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.PROTECT,
        related_name="subprojetos",
        verbose_name="Projeto"
    )
    nome = models.CharField(max_length=150, verbose_name="Nome do Subprojeto")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Subprojeto"
        verbose_name_plural = "Subprojetos"
        ordering = ['projeto', 'nome']

    def __str__(self):
        return f"{self.projeto.nome} - {self.nome}"


class Autor(models.Model):
    """Armazena informações sobre autores/colaboradores."""
    nome = models.CharField(max_length=255, verbose_name="Nome Completo do Autor")
    lattes_id = models.CharField(max_length=30, blank=True, null=True, verbose_name="ID Lattes")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tag(models.Model):
    """Novo modelo para palavras-chave consistentes."""
    nome = models.CharField(max_length=100, unique=True, verbose_name="Palavra-chave / Tag")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Tag / Palavra-chave"
        verbose_name_plural = "Tags / Palavras-chave"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class TipoDocumento(models.Model):
    """Tipos de documentos (Artigo, Tese, Relatório, Imagem, Planilha, etc.)."""
    nome = models.CharField(max_length=100, unique=True, verbose_name="Tipo do Documento")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class AreaTematica(models.Model):
    """Áreas de conhecimento ou temas principais."""
    nome = models.CharField(max_length=100, unique=True, verbose_name="Área Temática")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Área Temática"
        verbose_name_plural = "Áreas Temáticas"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Status(models.Model):
    """Status de fluxo de trabalho (Rascunho, Em Revisão, Publicado, Arquivado)."""
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome do Status")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    is_public = models.BooleanField(default=True, verbose_name="É público?")

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class TipoPublicacao(models.Model):
    """Tipo de veículo de publicação (Revista, Anais de Evento, Livro, etc.)."""
    nome = models.CharField(max_length=100, unique=True, verbose_name="Tipo da Publicação")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Tipo de Publicação"
        verbose_name_plural = "Tipos de Publicação"
        ordering = ['nome']

    def __str__(self):
        return self.nome


# Modelo Principal

class Registro(models.Model):
    """Modelo principal para itens do acervo (documentos, imagens, publicações)."""

    # ------------------------------------
    # RELAÇÕES E METADADOS CONTROLADOS
    # ------------------------------------
    subprojeto = models.ForeignKey(Subprojeto, on_delete=models.PROTECT, related_name="subprojetos", verbose_name="Subprojeto")
    autores = models.ManyToManyField(Autor, related_name="autores", verbose_name="Autores")
    tags = models.ManyToManyField(Tag, related_name="tags", verbose_name="Palavras-chave")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, related_name="tipo_documentos", verbose_name="Tipo de Documento")
    area_tematica = models.ForeignKey(AreaTematica, on_delete=models.PROTECT, related_name="areas_tematicas", verbose_name="Área Temática")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="status", verbose_name="Status de Publicação")
    tipo_publicacao = models.ForeignKey(TipoPublicacao, on_delete=models.PROTECT, related_name="tipo_publicacaoes",  verbose_name="Veículo de Publicação")

    # ------------------------------------
    # CONTEÚDO E ARQUIVO
    # ------------------------------------
    titulo = models.CharField(max_length=2000, verbose_name="Título")
    resumo = models.TextField(verbose_name="Resumo / Abstract", blank=True, null=True)
    data_publicacao = models.DateField(null=True, blank=True, verbose_name="Data da Publicação")
    isbn = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="ISBN (International Standard Book Number)")

    # Arquivo (upload para S3 em produção)
    arquivo = models.FileField(upload_to=item_file_path, null=True, blank=True, verbose_name="Arquivo")

    # Link externo (ex: URL da revista)
    link_externo = models.URLField(max_length=2000, validators=[URLValidator()], null=True, blank=True, verbose_name="Link Externo/URL")

    # ------------------------------------
    # AUDITORIA E CONTROLE
    # ------------------------------------
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Data da ultima atualização")

    usuario_criacao = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="registros_criados",
        verbose_name="Usuário de Criação"
    )
    usuario_ultima_atualizacao = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="registros_atualizados",
        verbose_name="Usuário da Última Atualização"
    )
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Registro / Documento"
        verbose_name_plural = "Registros / Documentos"
        ordering = ['-data_publicacao', 'titulo']

    def __str__(self):
        return self.titulo

    def clean(self):
        """Validação personalizada para garantir a integridade dos dados."""

        # 1. Validação de Título
        if not self.titulo:
            raise ValidationError("O campo Título não pode estar vazio.")

        # 2. Validação de Data (Data não pode ser futura)
        if self.data_publicacao and self.data_publicacao > date.today():
            raise ValidationError("A data de publicação não pode ser futura.")

        # 3. Validação de Link/Arquivo (Deve ter um OU outro)
        has_file = bool(self.arquivo)
        has_link = bool(self.link_externo)

        # Exigir pelo menos um, mas não necessariamente proibir ambos
        if not has_file and not has_link:
            raise ValidationError("O registro deve ter um Arquivo para upload OU um Link Externo.")

        super().clean()

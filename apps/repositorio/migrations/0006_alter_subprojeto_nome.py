from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('repositorio', '0005_registro_especie_informacoes_registro_especie_nova'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subprojeto',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome do Subprojeto'),
        ),
    ]
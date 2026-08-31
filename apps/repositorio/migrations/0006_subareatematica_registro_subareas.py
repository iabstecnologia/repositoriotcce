from django.db import migrations, models
import django.db.models.deletion


SUBAREAS_INICIAIS = {
    'Meio Físico': (
        'Geologia e Geomorfologia',
        'Hidrologia e Hidrogeologia',
        'Espeleologia e Caracterização Ambiental',
    ),
    'Meio Biótico': (
        'Biodiversidade Subterrânea',
        'Ecologia',
        'Conservação da biodiversidade',
    ),
    'Outros': (
        'Socioeconômico e socioambiental',
        'Gestão Ambiental',
        'Espeleoturismo e Uso Público',
    ),
}


def criar_subareas_iniciais(apps, schema_editor):
    AreaTematica = apps.get_model('repositorio', 'AreaTematica')
    SubAreaTematica = apps.get_model('repositorio', 'SubAreaTematica')

    for area_nome, subareas in SUBAREAS_INICIAIS.items():
        area, _ = AreaTematica.objects.get_or_create(
            nome=area_nome,
            defaults={'ativo': True},
        )
        for subarea_nome in subareas:
            SubAreaTematica.objects.get_or_create(
                area_tematica=area,
                nome=subarea_nome,
                defaults={'ativo': True},
            )


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0005_registro_especie_informacoes_registro_especie_nova'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAreaTematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Subárea Temática')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                (
                    'area_tematica',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='subareas_tematicas',
                        to='repositorio.areatematica',
                        verbose_name='Área Temática',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Subárea Temática',
                'verbose_name_plural': 'Subáreas Temáticas',
                'ordering': ['area_tematica', 'nome'],
            },
        ),
        migrations.AddConstraint(
            model_name='subareatematica',
            constraint=models.UniqueConstraint(
                fields=('area_tematica', 'nome'),
                name='unique_subarea_tematica_por_area',
            ),
        ),
        migrations.AddField(
            model_name='registro',
            name='subareas_tematicas',
            field=models.ManyToManyField(
                blank=True,
                related_name='registros',
                to='repositorio.subareatematica',
                verbose_name='Subáreas Temáticas',
            ),
        ),
        migrations.RunPython(criar_subareas_iniciais, migrations.RunPython.noop),
    ]

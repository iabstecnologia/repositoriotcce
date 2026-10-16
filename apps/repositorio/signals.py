from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

from apps.repositorio.models.repositorio import Registro, SubAreaTematica


@receiver(pre_save, sender=Registro)
def validar_subareas_ao_alterar_area(sender, instance, **kwargs):
    if not instance.pk:
        return

    area_tematica_anterior_id = sender.objects_all.filter(
        pk=instance.pk
    ).values_list('area_tematica_id', flat=True).first()
    if area_tematica_anterior_id is None or area_tematica_anterior_id == instance.area_tematica_id:
        return

    Registro.validar_subareas_tematicas(
        instance.area_tematica,
        instance.subareas_tematicas.all(),
    )


@receiver(m2m_changed, sender=Registro.subareas_tematicas.through)
def validar_area_das_subareas(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action != 'pre_add' or not pk_set:
        return

    if reverse:
        registros_incompativeis = Registro.objects_all.filter(
            pk__in=pk_set
        ).exclude(area_tematica_id=instance.area_tematica_id)
        if registros_incompativeis.exists():
            raise ValidationError(
                'Todas as subáreas devem pertencer à Área Temática do registro.'
            )
        return

    subareas = SubAreaTematica.objects_all.filter(pk__in=pk_set)
    Registro.validar_subareas_tematicas(instance.area_tematica, subareas)
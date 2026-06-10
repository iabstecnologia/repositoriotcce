from django.test import TestCase
from apps.repositorio.models.repositorio import Projeto, Autor, Tag, TipoDocumento


class ManagersTest(TestCase):
    def setUp(self):
        Projeto.objects_all.create(nome='Projeto Ativo', ativo=True)
        Projeto.objects_all.create(nome='Projeto Inativo', ativo=False)

        Autor.objects_all.create(nome='Autor Ativo', ativo=True)
        Autor.objects_all.create(nome='Autor Inativo', ativo=False)

        Tag.objects_all.create(nome='Tag Ativa', ativo=True)
        Tag.objects_all.create(nome='Tag Inativa', ativo=False)

        TipoDocumento.objects_all.create(nome='TipoDoc Ativo', ativo=True)
        TipoDocumento.objects_all.create(nome='TipoDoc Inativo', ativo=False)

    def test_objects_returns_only_active(self):
        self.assertEqual(Projeto.objects.count(), 1)
        self.assertEqual(Autor.objects.count(), 1)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(TipoDocumento.objects.count(), 1)

    def test_objects_all_returns_all(self):
        self.assertEqual(Projeto.objects_all.count(), 2)
        self.assertEqual(Autor.objects_all.count(), 2)
        self.assertEqual(Tag.objects_all.count(), 2)
        self.assertEqual(TipoDocumento.objects_all.count(), 2)

    def test_objects_inactive_returns_only_inactive(self):
        self.assertEqual(Projeto.objects_inactive.count(), 1)
        self.assertEqual(Autor.objects_inactive.count(), 1)
        self.assertEqual(Tag.objects_inactive.count(), 1)
        self.assertEqual(TipoDocumento.objects_inactive.count(), 1)

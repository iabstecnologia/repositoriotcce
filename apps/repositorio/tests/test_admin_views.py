from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.repositorio.models.repositorio import Autor


class AdminEditInactiveAuthorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='admintester@example.com',
            password='secret123',
            first_name='Admin',
            last_name='Tester',
        )
        # Cria autor inativo usando objects_all
        self.autor = Autor.objects_all.create(nome='Autor Inativo Teste', ativo=False)

    def test_admin_can_get_edit_page_for_inactive_author(self):
        self.client.force_login(self.user)
        url = reverse('repositorio:autor_editar', args=[self.autor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


from django.test import TestCase
from django.urls import reverse


class ContatoPageViewTest(TestCase):
    def test_contato_page_renders(self):
        response = self.client.get(reverse('core:contato'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/contato.html')
        self.assertContains(response, 'Contato')
        self.assertContains(response, 'João Pedro Alves Loiola')
        self.assertContains(response, 'Pedro Henrique Soares')
        self.assertContains(response, 'Pedro Costa')
        self.assertContains(response, 'João Pedro Peixoto')
        self.assertContains(response, 'Usuário-chave e gestor de conteúdo')
        credits_section_end = response.content.index(
            b'</section>', response.content.index(b'id="credits-title"')
        )
        contact_form_section = response.content.index(b'<!-- Contact Form Section -->')
        self.assertLess(credits_section_end, contact_form_section)
        self.assertLess(
            response.content.index('João Pedro Peixoto'.encode()),
            response.content.index(b'name="nome"'),
        )

    def test_sobre_url_resolves_to_sobre_path(self):
        self.assertEqual(reverse('core:sobre'), '/sobre/')

    def test_contato_url_resolves_to_contato_path(self):
        self.assertEqual(reverse('core:contato'), '/contato/')
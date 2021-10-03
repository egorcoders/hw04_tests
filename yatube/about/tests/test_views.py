from django.test import Client, TestCase
from django.urls import reverse


class AboutViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаем неавторизованый клиент
        cls.guest_client = Client()
        # Создадим словарь шаблонов по адресам
        cls.templates_url_names = {
            'about/author.html': 'about:author',
            'about/tech.html': 'about:tech'
        }

    def test_about_pages_are_accessible_by_name(self):
        """Проверка доступны ли страницы неавторизованному пользователю."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(reverse(reverse_name))
                self.assertEqual(response.status_code, 200)

    def test_about_pages_use_correct_template(self):
        """Проверка используются ли корректные шаблоны в приложении about."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(reverse(reverse_name))
                self.assertTemplateUsed(response, template)

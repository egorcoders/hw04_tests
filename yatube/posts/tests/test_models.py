from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Group, Post

User = get_user_model()


class PostModelsTest(TestCase):
    # Устанавливаем фикстуры, используем метод setUpClass()
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаем тестового пользователя модели User
        cls.user = User.objects.create_user(username='Тестовый пользователь')
        # Создаем тестовую группу модели Group
        cls.group = Group.objects.create(title='Тестовая группа')
        # Создаем тестовый пост модели Post
        cls.post = Post.objects.create(text='Тестовый пост Тестовый пост Тест',
                                       author=cls.user,
                                       group=cls.group)

    def test_post_str_text(self):
        """Проверка, выводятся ли только первые пятнадцать символов поста."""
        # Получаем из класса PostModelsTest данные поста
        post = PostModelsTest.post
        # Получаем значение text из поста
        text = post.text
        # Сравниваем полученные значения со __str__ модели
        self.assertEqual(str(post), text[:15])

    def test_group_str_title(self):
        """Проверка, совпадает ли название группы."""
        # Получаем из класса PostModelsTest данные группы
        group = PostModelsTest.group
        # Сравниваем полученные значения со __str__ модели
        self.assertEqual(str(group), group.title)

    def test_post_verbose_name(self):
        """Проверка, совпадают ли verbose_name в полях Post."""
        # Получаем данные поста из класса PostModelsTest
        post = PostModelsTest.post
        # Составляем словарь требуемых значений verbose_name
        field_verboses = {
            'text': 'Текст статьи',
            'pub_date': 'Дата публикации',
            'author': 'Автор статьи',
            'group': 'Группа статей',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    # Сравниваем фактические значения через ключ value
                    post._meta.get_field(value).verbose_name, expected)

    def test_group_verbose_name(self):
        """Проверка, совпадают ли verbose_name в полях Group."""
        group = PostModelsTest.group
        field_verboses = {
            'title': 'Название группы',
            'description': 'Описание группы',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).verbose_name, expected)

    def test_post_help_text(self):
        """Проверка, совпадают ли help_texts в полях Post."""
        post = PostModelsTest.post
        help_texts = {
            'text': 'Введите текст статьи',
            'pub_date': 'Укажите дату публикации',
            'author': 'Укажите автора статьи',
            'group': 'Выберите тематическую группу '
                     'в выпадающем списке по желанию',
        }
        for value, expected in help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).help_text, expected)

    def test_group_help_text(self):
        """Проверка совпадают ли help_texts в полях Group."""
        group = PostModelsTest.group
        help_texts = {
            'title': 'Введите название тематической группы',
            'description': 'Добавьте текст описания группы',
        }
        for value, expected in help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).help_text, expected)

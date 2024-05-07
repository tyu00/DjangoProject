from django.db import models


class User(models.Model):
    name = models.CharField('Ник', max_length=100)
    email = models.EmailField('почта')
    password = models.CharField('пароль', max_length=100)
    phone = models.CharField('номер телефона', max_length=20, null=True, blank=True)
    bio = models.TextField('о себе', null=True, blank=True)
    avatar = models.ImageField('автарка', upload_to='avatars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']


class Post(models.Model):
    title = models.CharField('заголовок', max_length=200)
    content = models.TextField('текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField('категория', max_length=50, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']
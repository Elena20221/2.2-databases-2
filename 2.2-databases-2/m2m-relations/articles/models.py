from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тэг')

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    tags = models.ManyToManyField(Tag, through='ArcticleTag') #, related_name='articles'
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class ArcticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes') #, related_name='positions'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes') #, related_name='positions'
    is_main = models.BooleanField(default=False, verbose_name='Основной')

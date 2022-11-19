from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArcticleTag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') == True:
                main_count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if main_count < 1:
            raise ValidationError('Необходимо выбрать основной Тег')
        if main_count > 1:
            raise ValidationError('Должен быть только один основной Тег')
        return super().clean()  # вызываем базовый код переопределяемого метода

class RelationshipInline(admin.TabularInline):
    model = ArcticleTag
    # list_display = ['id', 'name']
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'published_at', 'image']
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

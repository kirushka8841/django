from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter == 0:
            raise ValidationError('Выберите основной раздел')
        elif counter >= 2:
            raise ValidationError('Основной раздел может быть только 1')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from networks.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """Admin класс для модели NetworkNode с настраиваемыми действиями"""
    list_display = ('name', 'country', 'city', 'level', 'get_supplier_name', 'supplier_link', 'debt')
    list_filter = ('city',)

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse('admin:networks_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">Открыть поставщика</a>', url)
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'
    supplier_link.allow_tags = True

    def clear_the_debt(self, request, queryset):
        """Действие для очистки задолженности выбранных объектов в административной панели"""
        queryset.update(debt=0)

    clear_the_debt.short_description = "Очистить задолженность"

    actions = [clear_the_debt]

    def get_supplier_name(self, obj):
        """Возвращает имя поставщика для завода"""
        return obj.supplier.name if obj.supplier else None

    get_supplier_name.short_description = 'Поставщик'

from django.contrib import admin

from networks.models import Factory, RetailNetwork, IndividualEntrepreneur


class NetworkNodeAdmin(admin.ModelAdmin):
    list_filter = ('city',)

    def clear_the_debt(self, queryset):
        queryset.update(debt=0)

    clear_the_debt.short_description = "Очистить задолженность"

    actions = [clear_the_debt]


@admin.register(Factory)
class FactoryAdmin(NetworkNodeAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_name', 'debt')

    # list_display_links = ['get_supplier_name']

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else None

    get_supplier_name.short_description = 'Поставщик'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(NetworkNodeAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_name', 'debt',)
    list_display_links = ['get_supplier_name']

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else None

    get_supplier_name.short_description = 'Поставщик'

    def __str__(self):
        return self.name


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(NetworkNodeAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_name', 'debt',)

    # list_display_links = ['get_supplier_name']

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else None

    get_supplier_name.short_description = 'Поставщик'

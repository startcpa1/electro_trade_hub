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
    list_display = ('name', 'country', 'city', 'debt',)


@admin.register(RetailNetwork)
class RetailNetworkAdmin(NetworkNodeAdmin):
    list_display = ('name', 'country', 'city', 'debt',)


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(NetworkNodeAdmin):
    list_display = ('name', 'country', 'city', 'debt',)

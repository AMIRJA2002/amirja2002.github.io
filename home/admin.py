from django.contrib import admin
from .models import ExcelData, Pump, PumpModel, EnginKind, OriginCity, DestinationCity, BuilderCompany


@admin.register(ExcelData)
class ExcelDataAdmin(admin.ModelAdmin):
    list_display = ('row', 'engine_power', 'engine_serial_number', 'floor', 'pump_type', 'pump_specifications', 'city_of_origin', 'manufacturer', 'code', 'serial_number')


@admin.register(Pump)
class PumpAdmin(admin.ModelAdmin):
    list_display = ['code', 'engine_power_display', 'pump_model', 'serial_number', 'origin_city', 'destination_city',
                    'builder_company', 'date', 'courier', 'created_at', 'updated_at']
    search_fields = ['code', 'courier']
    list_filter = ['engine_power__kind', 'pump_model', 'origin_city', 'destination_city', 'builder_company', 'date']

    def engine_power_display(self, obj):
        return obj.engine_power.kind +' KW'
    engine_power_display.short_description = 'Engine Power'  # Set a custom name for the column


@admin.register(EnginKind)
class EnginKindAdmin(admin.ModelAdmin):
    list_display = ['kind']
    search_fields = ['kind']

    def kind_display(self, obj):
        return obj.kind +' KW'
    kind_display.short_description = 'kind'  # Set a custom name for the column



@admin.register(PumpModel)
class PumpModelAdmin(admin.ModelAdmin):
    list_display = ['model']
    search_fields = ['model']


@admin.register(OriginCity)
class OriginCityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(DestinationCity)
class DestinationCityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(BuilderCompany)
class BuilderCompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
from django.contrib import admin
from .models import (
    Region,
    Departement,
    StructureSanitaire,
    Consultation,
    TraitmentAntipaludique,
    Laboratoire,
    FemmeEnceinte,
    ConsultationPrenatale,
)

# Configuration pour le modèle Region
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region',)
    search_fields = ('region',)
    ordering = ('region',)


# Configuration pour le modèle Departement
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('departement', 'region')
    search_fields = ('departement', 'region__region')
    list_filter = ('region',)
    ordering = ('departement',)


# Configuration pour le modèle StructureSanitaire
@admin.register(StructureSanitaire)
class StructureSanitaireAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'departement', 'get_region')
    search_fields = ('structure_sanitaire', 'departement__departement', 'departement__region__region')
    list_filter = ('departement__region', 'departement')
    ordering = ('structure_sanitaire',)

    def get_region(self, obj):
        return obj.departement.region.region
    get_region.short_description = 'Région'


# Configuration pour le modèle Consultation
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'mois', 'age_group', 'sexe', 'total_cases_consulted')
    search_fields = ('structure_sanitaire__structure_sanitaire', 'mois', 'age_group')
    list_filter = ('mois', 'age_group', 'sexe')
    ordering = ('mois', 'age_group')


# Configuration pour le modèle TraitmentAntipaludique
@admin.register(TraitmentAntipaludique)
class TraitmentAntipaludiqueAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'mois', 'age_group', 'sexe', 'antipaludique_confirmed', 'act_confirmed')
    search_fields = ('structure_sanitaire__structure_sanitaire', 'mois', 'age_group')
    list_filter = ('mois', 'age_group', 'sexe')
    ordering = ('mois', 'age_group')


# Configuration pour le modèle Laboratoire
@admin.register(Laboratoire)
class LaboratoireAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'mois', 'age_group', 'total_patients_tested', 'total_malaria_positive')
    search_fields = ('structure_sanitaire__structure_sanitaire', 'mois', 'age_group')
    list_filter = ('mois', 'age_group', 'sexe')
    ordering = ('mois', 'age_group')


# Configuration pour le modèle FemmeEnceinte
@admin.register(FemmeEnceinte)
class FemmeEnceinteAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'mois', 'total_cases_consulted', 'suspected_malaria_cases')
    search_fields = ('structure_sanitaire__structure_sanitaire', 'mois')
    list_filter = ('mois',)
    ordering = ('mois',)


# Configuration pour le modèle ConsultationPrenatale
@admin.register(ConsultationPrenatale)
class ConsultationPrenataleAdmin(admin.ModelAdmin):
    list_display = ('structure_sanitaire', 'mois', 'total_femmes_cpn1', 'tpi_1', 'tpi_2')
    search_fields = ('structure_sanitaire__structure_sanitaire', 'mois')
    list_filter = ('mois',)
    ordering = ('mois',)

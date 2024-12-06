from django.db import models

# Définition des choix communs
AGE_GROUPS = [
    ('0-11 mois', '0-11 mois'),
    ('1-4 ans', '1-4 ans'),
    ('5-14 ans', '5-14 ans'),
    ('15-49 ans', '15-49 ans'),
    ('50+ ans', '50+ ans'),
]

MOIS_CHOICES = [
    ('Janvier', 'Janvier'),
    ('Février', 'Février'),
    ('Mars', 'Mars'),
    ('Avril', 'Avril'),
    ('Mai', 'Mai'),
    ('Juin', 'Juin'),
    ('Juillet', 'Juillet'),
    ('Août', 'Août'),
    ('Septembre', 'Septembre'),
    ('Octobre', 'Octobre'),
    ('Novembre', 'Novembre'),
    ('Décembre', 'Décembre'),
]

SEXE_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin'),
    ('Autre', 'Autre'),
]

# Classe pour la région
class Region(models.Model):
    region = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = "Région"
        verbose_name_plural = "Régions"
        ordering = ['region']


# Classe pour le département, lié à la région
class Departement(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="departements")
    departement = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.departement} - {self.region.region}"

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ['departement']


# Classe StructureSanitaire, liée au département
class StructureSanitaire(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name="structures")
    structure_sanitaire = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.structure_sanitaire} ({self.departement.departement}, {self.departement.region.region})"

    class Meta:
        verbose_name = "Structure Sanitaire"
        verbose_name_plural = "Structures Sanitaires"
        ordering = ['structure_sanitaire']


# Classe Consultation, liée à StructureSanitaire
class Consultation(models.Model):
    structure_sanitaire = models.ForeignKey(StructureSanitaire, on_delete=models.CASCADE, related_name="consultations")
    mois = models.CharField(max_length=50, choices=MOIS_CHOICES)
    age_group = models.CharField(max_length=50, choices=AGE_GROUPS)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='M')
    total_cases_consulted = models.PositiveIntegerField(default=0)
    suspected_malaria_cases = models.PositiveIntegerField(default=0)
    untested_malaria_cases = models.PositiveIntegerField(default=0)
    confirmed_malaria_cases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.structure_sanitaire.structure_sanitaire} - {self.age_group} ({self.mois})"

    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"
        ordering = ['mois', 'age_group']


# Classe TraitementAntipaludique, liée à StructureSanitaire
class TraitmentAntipaludique(models.Model):
    structure_sanitaire = models.ForeignKey(StructureSanitaire, on_delete=models.CASCADE, related_name="traitements")
    mois = models.CharField(max_length=50, choices=MOIS_CHOICES)
    age_group = models.CharField(max_length=50, choices=AGE_GROUPS)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='M')
    antipaludique_confirmed = models.PositiveIntegerField(default=0)
    antipaludique_probable = models.PositiveIntegerField(default=0)
    act_confirmed = models.PositiveIntegerField(default=0)
    act_probable = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.antipaludique_confirmed} ({self.age_group})"

    class Meta:
        verbose_name = "Traitement Antipaludique"
        verbose_name_plural = "Traitements Antipaludiques"
        ordering = ['mois', 'age_group']


# Classe Laboratoire, liée à StructureSanitaire
class Laboratoire(models.Model):
    structure_sanitaire = models.ForeignKey(StructureSanitaire, on_delete=models.CASCADE, related_name="laboratoires")
    mois = models.CharField(max_length=50, choices=MOIS_CHOICES)
    age_group = models.CharField(max_length=50, choices=AGE_GROUPS)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='M')
    total_patients_tested = models.PositiveIntegerField(default=0)
    total_malaria_positive = models.PositiveIntegerField(default=0)
    total_tdr_tests = models.PositiveIntegerField(default=0)
    positive_tdr_tests = models.PositiveIntegerField(default=0)
    total_microscopy_tests = models.PositiveIntegerField(default=0)
    positive_microscopy_tests = models.PositiveIntegerField(default=0)
    pf_cases = models.PositiveIntegerField(default=0)
    pm_cases = models.PositiveIntegerField(default=0)
    po_cases = models.PositiveIntegerField(default=0)
    pv_cases = models.PositiveIntegerField(default=0)
    mixed_infections = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.structure_sanitaire.structure_sanitaire} - Laboratoire ({self.mois})"

    class Meta:
        verbose_name = "Laboratoire"
        verbose_name_plural = "Laboratoires"
        ordering = ['mois', 'age_group']


# Classe FemmeEnceinte, liée à StructureSanitaire
class FemmeEnceinte(models.Model):
    structure_sanitaire = models.ForeignKey(StructureSanitaire, on_delete=models.CASCADE, related_name="femmes_enceintes")
    mois = models.CharField(max_length=50, choices=MOIS_CHOICES)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='F')
    total_cases_consulted = models.PositiveIntegerField(default=0)
    suspected_malaria_cases = models.PositiveIntegerField(default=0)
    untested_malaria_cases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.structure_sanitaire.structure_sanitaire} - Femme Enceinte : {self.total_cases_consulted} consultations, {self.suspected_malaria_cases} cas suspects de paludisme"

    class Meta:
        verbose_name = "Femme Enceinte"
        verbose_name_plural = "Femmes Enceintes"
        ordering = ['mois']


# Classe ConsultationPrenatale, liée à StructureSanitaire
class ConsultationPrenatale(models.Model):
    structure_sanitaire = models.ForeignKey(StructureSanitaire, on_delete=models.CASCADE, related_name="consultations_prenatales")
    mois = models.CharField(max_length=50, choices=MOIS_CHOICES)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='F')
    total_femmes_cpn1 = models.PositiveIntegerField(default=0)
    tpi_1 = models.PositiveIntegerField(default=0)
    tpi_2 = models.PositiveIntegerField(default=0)
    tpi_3 = models.PositiveIntegerField(default=0)
    tpi_4 = models.PositiveIntegerField(default=0)
    tpi_5 = models.PositiveIntegerField(default=0)
    tpi_6 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.structure_sanitaire.structure_sanitaire} - CPN1 : {self.total_femmes_cpn1} femmes vues, TPI1: {self.tpi_1}, TPI2: {self.tpi_2}, TPI3: {self.tpi_3}"

    class Meta:
        verbose_name = "Consultation Prénatale"
        verbose_name_plural = "Consultations Prénatales"
        ordering = ['mois']

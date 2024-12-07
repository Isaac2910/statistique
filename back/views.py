from django.shortcuts import render
from django.db.models import Sum  # Importer Sum
from .models import Consultation

def accueil(request):
    # Cas par groupe d'âge
    age_group_data = Consultation.objects.values('age_group').annotate(total_cases=Sum('confirmed_malaria_cases'))
    age_group_labels = [data['age_group'] for data in age_group_data]
    age_group_values = [data['total_cases'] for data in age_group_data]

    # Répartition des sexes
    sexe_data = Consultation.objects.values('sexe').annotate(total=Sum('confirmed_malaria_cases'))
    sexe_labels = [data['sexe'] for data in sexe_data]
    sexe_values = [data['total'] for data in sexe_data]

    # Cas confirmés par mois
    monthly_cases_data = Consultation.objects.values('mois').annotate(total=Sum('confirmed_malaria_cases'))
    monthly_labels = [data['mois'] for data in monthly_cases_data]
    monthly_values = [data['total'] for data in monthly_cases_data]

    context = {
        'age_group_data': {
            'labels': age_group_labels,
            'data': age_group_values,
        },
        'sexe_data': {
            'labels': sexe_labels,
            'data': sexe_values,
        },
        'monthly_cases_data': {
            'labels': monthly_labels,
            'data': monthly_values,
        },
    }
    return render(request, 'accueil.html', context)


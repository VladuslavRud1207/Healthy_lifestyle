from django.shortcuts import render

from .models import r1


def home(request):
    return render(request, 'home.html')


def queries(request):

    return render(request, 'queries.html')


def tables(request):

    return render(request, 'tables.html')


def show_dropdowns(request):
    places_of_residence = r1.objects.values_list('Місце_проживання', flat=True).distinct()
    goals = r1.objects.values_list('Ціль', flat=False).distinct()

    if request.method == 'GET':
        selected_place = request.GET.get('Місце_проживання')
        selected_goal = request.GET.get('Ціль')

        if selected_place and selected_goal:
            # Getting the relevant records
            results = r1.objects.filter(Місце_проживання=selected_place, Ціль=selected_goal)
            return render(request, 'results1.html', {'results': results})

    return render(request, 'dropdowns1.html', {'places_of_residence': places_of_residence, 'goals': goals})

"""
def show_dropdowns(request):
    if request.method == 'POST':
        selected_place = request.POST.get('Місце_проживання')
        selected_goal = request.POST.get('Ціль')

        # Getting the relevant records
        results = r1.objects.filter(Місце_проживання=selected_place, Ціль=selected_goal)

        return render(request, 'results1.html', {'results': results})

    return render(request, 'dropdowns1.html')


def all_records_view(request):
    # Отримати всі записи з таблиці
    all_records = r1.objects.all()
    # Передати записи у шаблон та відображити його
    return render(request, 'vuvod_zapusiv.html', {'all_records': all_records})
"""
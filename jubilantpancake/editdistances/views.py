from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    if request.method == 'POST':
        distance = _distance(request)
        return JsonResponse({'edit_distance': distance})
    return render(request, 'home.html')


def _distance(request):
    input_1 = request.POST['input_1']
    input_2 = request.POST['input_2']

    distances = range(len(input_1) + 1)
    for idx2, char2 in enumerate(input_2):
        new_distances = [idx2 + 1]
        for idx1, char1 in enumerate(input_1):
            if char1 == char2:
                new_distances.append(distances[idx1])
            else:
                new_distances.append(1 + min((distances[idx1],
                                             distances[idx1 + 1],
                                             new_distances[-1])))
        distances = new_distances
    return distances[-1]

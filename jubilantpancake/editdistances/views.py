"""
Function based home page view
Edit Distance Algo
"""
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    """
    home page returns json on post
    """
    if request.method == 'POST':
        distance = _distance(request)
        return JsonResponse({'edit_distance': distance})
    return render(request, 'home.html')


def _distance(request):
    """
    algo to compute edit distance
     - insert
     - delete
     - swap
    """
    input_1 = request.POST['input_1']
    input_2 = request.POST['input_2']

    distances = range(len(input_1) + 1)
    for idx2, char2 in enumerate(input_2):
        new_distances = [idx2 + 1]
        for idx1, char1 in enumerate(input_1):
            if char1 == char2:
                new_distances.append(distances[idx1])
            else:
                minimum = min(
                    (distances[idx1], distances[idx1 + 1], new_distances[-1])
                )
                new_distances.append(1 + minimum)
        distances = new_distances
    return distances[-1]

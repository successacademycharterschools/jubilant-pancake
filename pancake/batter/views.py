from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import distance
import json


def text_compare(request):
    context = RequestContext(request)

    if request.method == 'POST':
        #json_data = request.POST['data']
        one = request.POST['fieldone']
        two = request.POST['fieldtwo']
        distances = compute_distances(one,two)
        distances['lcs'] = list(distances['lcs'])  #sets not JSON serializable
        return HttpResponse(json.dumps(distances))

    else:
        return HttpResponse('{}')


def batter_page(request):
    context = RequestContext(request)
    return render_to_response('batter_page.html', context)


def compute_distances(one, two):
    if one is None:
        one = ''
    if two is None:
        two = ''
    one_spaced = one.split(' ')
    two_spaced = two.split(' ')
    full_levenshtein = distance.levenshtein(one, two)
    spaced_levenshtein = distance.levenshtein(one_spaced, two_spaced)
    lcs = distance.lcsubstrings(one, two)
    words_in_common = 0
    one_set = set(one_spaced)

    for w in two_spaced:
        if w in one_set:
            words_in_common += 1

    return {'full': full_levenshtein, 'spaced': spaced_levenshtein, 'lcs': lcs, 'words_in_common': words_in_common}

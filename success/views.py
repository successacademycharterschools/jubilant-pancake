import json
import os

from django import forms
from django.shortcuts import render
from django.conf import settings


class DistanceForm(forms.Form):
    """
    The form class that is passed to the index page
    """
    string_one = forms.CharField(label='String One', required=True, max_length=500)
    string_two = forms.CharField(label='String Two', required=True, max_length=500)
    edit_distance = forms.IntegerField(min_value=0, max_value=500, required=False, disabled=True)


def distance_form_view(request):
    """
    This returns the index view for a user logging on to the main page.
    If GET, returns an empty form
    If POST, it fills the DistanceForm with the calculated result

    :param request: Either a GET or POST request, which will render the form to the user
    :return: django.shortcuts.render with the form attached
    """

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DistanceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form = DistanceForm(
                initial={
                    'string_one': form.cleaned_data['string_one'],
                    'string_two': form.cleaned_data['string_two'],
                    'edit_distance': get_distance(form.cleaned_data['string_one'], form.cleaned_data['string_two'])
                }
            )
            return render(request, 'index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DistanceForm()

    return render(request, 'index.html', {'form': form})


def distance_test_view(request):
    """
    This returns the test suite view
    If any tests in test_suite.json fail, they will appear red
    (I thought this would be more fun then using assert to crash the django app)

    :param request: Only handles GET requests
    :return: django.shortcuts.render with the tests passed into the template
    """

    # Set the test results from the json file in the static dir
    test_config_path = os.path.join(settings.PROJECT_ROOT, 'static/test_suite.json')
    with open(test_config_path) as config_file:
        test_config = json.load(config_file)

    # Build the results with the calculation from get_distance
    results = []
    for i in range(0, len(test_config)):
        results.append(test_config[i])
        results[i]['actual_result'] = get_distance(results[i]['string1'], results[i]['string2'])

    return render(request, 'test.html', {'tests': results})


def get_distance(string1, string2):
    """
    get_distance provides the distance between two strings using the Levenshtein algorithm
    more info: (https://en.wikipedia.org/wiki/Levenshtein_distance)

    :param string1: (str) the first string to be compared
    :param string2: (str) the second string to be compared
    :return: (int) the distance between the two strings
    """

    # We require string1 to be the longer string
    if len(string1) < len(string2):
        return get_distance(string2, string1)

    # If string2 is zero, just return the length of the first
    if len(string2) == 0:
        return len(string1)

    previous_row = range(len(string2) + 1)
    for i in range(0, len(string1)):
        current_row = [i + 1]
        for j in range(0, len(string2)):
            # j+1 instead of j since previous_row and current_row are one character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (string1[i] != string2[j])
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

"""Views for Jubilant Pancake project"""
from json import dumps, loads

from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .forms import PancakeForm
from .utils import wagner_fisher


class PancakeView(TemplateView):
    """Home view for Jubilant Pancake"""
    template_name = 'pancake/index.html'

    def get(self, request, *args, **kwargs):
        kwargs.update({'form': PancakeForm()})
        return self.render_to_response(self.get_context_data(**kwargs))


class CalculateView(View):
    """Calculation view for Jubilant Pancake"""
    # pylint: disable=unused-argument
    # pylint: disable=no-self-use
    def post(self, request, *args, **kwargs):
        """get the POSTed strings and send them to the wagner-fisher util"""
        if request.POST:
            strings = request.POST.copy()
        else:
            strings = loads(request.body)
        kwargs = {
            'edit_distance': wagner_fisher(
                strings['string_1'], strings['string_2']
            )
        }
        return HttpResponse(dumps(kwargs), content_type='application/json')

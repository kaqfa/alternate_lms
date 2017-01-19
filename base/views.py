from django.shortcuts import render
from django.views.generic import TemplateView


class MenuMixin(object):

	def get_context_data(self, **kwargs):
		context = super(MenuMixin, self).get_context_data(**kwargs)
		context['matkul'] = ["Pemrograman Internet", "Basis Data", "Perancangan Perangkat Lunak"]

		return context


class IndexView(MenuMixin, TemplateView):
	template_name = 'dashboard.html'	

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name)
from django.shortcuts import render
from django.views.generic import TemplateView
from base.views import MenuMixin

class FrontView(MenuMixin, TemplateView):
	template_name = 'coursefront.html'


class OutlineView(MenuMixin, TemplateView):
	template_name = 'courseoutline.html'


class GradeView(MenuMixin, TemplateView):
	template_name = 'coursegrade.html'

	def get_context_data(self, **kwargs):
		context = super(GradeView, self).get_context_data(**kwargs)
		context['assignments'] = ["Upload Judul", "CodeCademy", "Bootstrap Layout", "Full Project", "Laporan Akhir"]

		return context
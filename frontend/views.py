from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'archive_manager/index.html'
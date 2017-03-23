import os
from itertools import islice
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .utils import readlines_reverse


class LogViewerView(TemplateView):
    """
    LogViewerView class

    :cvar template_name: Name of the HTML template used to render the log files

    """
    template_name = "log_viewer/logfile_viewer.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogViewerView, self).dispatch(*args, **kwargs)

    def get_context_data(self, file_name=None, page=1, **kwargs):
        """
        Read and return log files to be showed in admin page

        :param file_name: log file name
        :param page: log viewer page
        """
        context = super(LogViewerView, self).get_context_data(**kwargs)
        file_urls = []
        file_names = []
        page = int(page)
        lines_per_page = getattr(settings, 'LOG_ITEMS_PER_PAGE', 50)
        current_file = file_name

        context['custom_file_list_title'] = getattr(
            settings, 'LOG_VIEWER_FILE_LIST_TITLE', False
        )
        context['is_django_jet'] = getattr(
            settings, 'LOG_VIEWER_IS_DJANGO_JET', False
        )
        context['custom_style_file'] = getattr(
            settings, 'LOG_VIEWER_FILE_LIST_STYLES', False
        )

        context['log_files'] = []
        context['next_page'] = page + 1
        for root, directory, files in os.walk(settings.LOGS_DIR):
            tmp_names = filter(lambda x: x.find('~') == -1, files)
            if not root.split('/')[-1] == 'user':
                tmp_names = filter(
                    lambda x: x in settings.LOG_VIEWER_FILES,
                    tmp_names)
            file_names += tmp_names
            file_urls += map(lambda x: '%s/%s' % (root, x), tmp_names)
            if file_name and file_name in files:
                file_name = '%s/%s' % (root, file_name)
        for i, element in enumerate(file_names):
            context['log_files'].append({
                element: file_urls[i]
            })
        if file_name:
            try:
                with open(file_name) as file:
                    next_lines = list(
                        islice(readlines_reverse(file, exclude='Not Found'),
                               (page - 1) * lines_per_page,
                               page * lines_per_page))
                    if len(next_lines) < lines_per_page:
                        context['last'] = True
                    else:
                        context['last'] = False
                    context['logs'] = next_lines
                    context['current_file'] = current_file
                    context['file'] = file
            except (IOError, ValueError):
                pass
        else:
            context['last'] = True
        return context

log_viewer = LogViewerView.as_view()

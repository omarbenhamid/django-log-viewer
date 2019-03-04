import os
from itertools import islice
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.utils import quote, unquote

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
        # Clean the `file_name` to avoid relative paths.
        file_name = unquote(file_name).replace('/..', '').replace('..', '')
        file_urls = []
        file_names = []
        file_display = []
        page = int(page)
        lines_per_page = getattr(settings, 'LOG_ITEMS_PER_PAGE', 50)
        current_file = file_name
        context['custom_file_list_title'] = getattr(
            settings, 'LOG_VIEWER_FILE_LIST_TITLE', False
        )
        context['original_file_name'] = file_name
        context['is_django_jet'] = getattr(
            settings, 'LOG_VIEWER_IS_DJANGO_JET', False
        )
        context['custom_style_file'] = getattr(
            settings, 'LOG_VIEWER_FILE_LIST_STYLES', False
        )

        context['log_files'] = []
        context['next_page'] = page + 1
        len_logs_dir = len(settings.LOGS_DIR)
        for root, _, files in os.walk(settings.LOGS_DIR):
            tmp_names = list(filter(lambda x: x.find('~') == -1, files))
            # if LOG_VIEWER_FILES is not set in settings
            # then all the files with '.log' extension are listed
            if hasattr(settings, 'LOG_VIEWER_FILES'):
                tmp_names = list(
                    filter(
                        lambda x: x in settings.LOG_VIEWER_FILES,
                        tmp_names))
            else:
                tmp_names = [
                    name for name in tmp_names if (
                        name.split('.')[-1]) == 'log']
            file_names += tmp_names
            file_display += [('%s/%s' % (
                root[len_logs_dir:], name))[1:] for name in tmp_names]
            file_urls += list(map(lambda x: '%s/%s' % (root, x), tmp_names))
        for i, element in enumerate(file_display):
            context['log_files'].append({
                quote(element): {
                    'uri': file_urls[i],
                    'display': element,
                }
            })
        if file_name:
            try:
                with open(os.path.join(settings.LOGS_DIR, file_name)) as file:
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

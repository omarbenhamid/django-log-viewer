==========
Log Viewer
==========

Log Viewer allows you to read log files in the admin page.

Quick start
-----------
1. Include the log-viewer URLconf in your project urls.py like this::

    pip install -e git+git@bitbucket.org:inkalabsinc/django-log-viewer.git@v0.0.2#egg=django_log_viewer002



2. Add "log-viewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'log_viewer',
    ]

3. Include the log-viewer URLconf in your project urls.py like this::

    url(r'^admin/log_viewer/', include('log_viewer.urls', namespace="log-viewer")),

4. In your settings file create the following value::

    LOGS_DIR = os.path.join(BASE_DIR, '../logs')
    LOG_VIEWER_FILES = ['logfile1', 'logfile2', ...]
    LOG_ITEMS_PER_PAGE = 50

    Optionally you can set the next variables in order to customize the admin:

    LOG_VIEWER_FILE_LIST_STYLES = <path to style file>
    LOG_VIEWER_FILE_LIST_TITLE = "Custom title"
    LOG_VIEWER_IS_DJANGO_JET = True|False

5. Start the development server and visit http://127.0.0.1:8000/admin/log_viewer/
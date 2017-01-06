==========
Log Viewer
==========

Log Viewer allows you to read log files in the admin page.

Quick start
-----------

1. Add "log-viewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'log_viewer',
    ]

2. Include the log-viewer URLconf in your project urls.py like this::

    url(r'^admin/log_viewer/', include('log_viewer.urls', namespace="log-viewer")),

3. In your settings file create the following value::

    LOGS_DIR = os.path.join(BASE_DIR, '../logs')
    LOG_VIEWER_FILES = ['logfile1', 'logfile2', ...]

4. Start the development server and visit http://127.0.0.1:8000/admin/log_viewer/

=====
Log Viewer
=====

Log Viewer allows you to read log files in the admin page.

Quick start
-----------

1. Add "log-viewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-log-viewer',
    ]

2. Include the log-viewer URLconf in your project urls.py like this::

    url(r'^log_viewer/', include('log-viewer.urls')),

3. In your settings file create the following value::

   LOG_VIEWER_FILES = ['path/to/logfile1', 'path/to/logfile2', ...]

4. Start the development server and visit http://127.0.0.1:8000/admin/log_viewer/

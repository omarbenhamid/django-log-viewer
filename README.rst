==========
Log Viewer
==========

Log Viewer allows you to read log files in the admin page.

Quick start
-----------
1. Include the log-viewer URLconf in your project urls.py like this::

    pip install -e git+git@bitbucket.org:inkalabsinc/django-log-viewer.git#egg=django-log-viewer



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

5. Start the development server and visit http://127.0.0.1:8000/admin/log_viewer/
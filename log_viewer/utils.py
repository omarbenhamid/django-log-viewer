import os
from django.conf import settings


def readlines_reverse(qfile, exclude=''):
    """
    Read file lines from bottom to top
    """
    pfx = getattr(settings, 'LOG_VIEWER_LINE_PREFIX', '')
    pfx = pfx[::-1]
    pfxlen = len(pfx)
    
    qfile.seek(0, os.SEEK_END)
    position = qfile.tell()
    line = ''
    while position >= 0:
        qfile.seek(position)
        next_char = qfile.read(1)
        if next_char == "\n" and line and (line[-pfxlen:] == pfx if pfxlen else True):
            if exclude in line[::-1]:
                line = ''
            else:
                yield line[::-1]
                line = ''
        else:
            line += next_char
        position -= 1
    yield line[::-1]

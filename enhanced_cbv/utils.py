import os, csv, codecs

from django.conf import settings
from six.moves import cStringIO


def fetch_resources(uri, rel):
    """
    Callback to allow pisa/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.
    """
    if settings.STATIC_URL in uri:
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, **kwds):
        self.stream = f

    def writerow(self, row):
        # write to the target stream
        data = u','.join(row) + u'\n'
        self.stream.write(data)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

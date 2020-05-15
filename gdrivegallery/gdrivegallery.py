from __future__ import print_function
from collections import OrderedDict
import httplib2
import os
import re

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from pelican import signals, logger


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials(commandline_flags=None):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if commandline_flags:
            credentials = tools.run_flow(flow, store, commandline_flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

photos_id = '0B44mjlWGbPILUzZwZHprOW43MU0'

def generate_gallery_page(generator):

    contentpath = generator.settings.get('PATH')
    gallerycontentpath = os.path.join(contentpath,'images/gallery')

    for page in generator.pages:
        if page.metadata.get('template') != 'gallery':
            continue

        credentials = get_credentials(commandline_flags='--noauth_local_webserver')
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)

        only_folders = "mimeType='application/vnd.google-apps.folder'"
        children = "('{folderID}' in parents)"
        child_folders = "({}) and ({})".format(children, only_folders)

        files = service.files()

        photo_urls = OrderedDict()

        photo_folders = files.list(q=child_folders.format(folderID=photos_id), orderBy='name desc').execute()
        for year in photo_folders.get('files'):
            year_name = year.get('name')
            if re.match('^\d{4}$', year_name) is not None:
                photo_urls[year_name] = OrderedDict()
                folderID = year.get('id')
                albums = files.list(q=child_folders.format(folderID=folderID), orderBy='name desc').execute()
                for album in albums.get('files'):
                    album_name = album.get('name')
                    album_name = ' '.join(album_name.split(' ')[1:])
                    photo_urls[year_name][album_name] = list()
                    query = children.format(folderID=album.get('id'))
                    photos = files.list(q=query, orderBy='name').execute()
                    for photo in photos.get('files'):
                        photo_url = 'https://drive.google.com/uc?export=view&id={}'.format(photo.get('id'))
                        photo_urls[year_name][album_name].append(photo_url)

        page.gallery = photo_urls
        print(page)

def register():
    signals.page_generator_finalized.connect(generate_gallery_page)

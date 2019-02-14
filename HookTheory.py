import requests
from ratelimit import limits

class HookTheory:
    '''
        Simple python class to interface with the HookTheory Web API
        which allows one to search for chord progressions and songs
        that feature certain chord progressions
    '''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bearerToken = None

    def _getAuth(self):
        base_url = 'https://api.hooktheory.com/v1'
        auth_url = '/users/auth'
        url = base_url + auth_url

        header = {"Accept": "application/json",
              "Content-Type": "application/json",
              "username" : self.username,
              "password" : self.password}

        req = requests.post(url, data = header)
        return req


    def getAuth(self):
        '''
            input Void
            returns string bearerToken

            Updates member self.bearerToken which which is
            required for get requests
        '''
        resp = self._getAuth()
        try:
            bearerToken = resp.json()['activkey']
            self.bearerToken = bearerToken
            return bearerToken
        except KeyError:
            return resp


    def _header(self):
        header = {"Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + self.bearerToken}
        return header


    def getChords(self, chordId = None):
        '''
        input:  string: chord_id (see https://www.hooktheory.com/api/trends/docs
                                  for the meaning of chord_id)
                valid input formats:
                    - None
                    - Single chordId
                        e.g. '1' '4' '17'
                    - comma separated chordIds
                        e.g. '1,4', '1,4,5'

        return: requests.models.Response object : req (see python requests library)
                to read out contents of the HTTP response use the builtin requests
                json decoder. e.g.

                    oneChords =  HookTheory.getChords( chordId = '1').json()

                This will return a list of python dictionaries containing
                the chord most likely to appear after those specified based
                on the songs contained in HookTheory's collection of songs

                e.g the output of oneChords would be

                [{'child_path': '1,5',
                'chord_HTML': 'V',
                'chord_ID': '5',
                'probability': 0.252},
                ...
                ]
        '''

        assert self.bearerToken is not None, 'Need Valid bearerToken'

        base_url = 'https://api.hooktheory.com/v1'
        chord_url = '/trends/nodes'
        url = base_url + chord_url
        header = self._header()

        if chordId == None:
            query = ''
        else:
            query = '?cp=' + chordId

        req = requests.get( url + query, headers= header)

        return req

    def getSongs(self, chordId=None, page=1):
        '''
        input:  string: chord_id (see https://www.hooktheory.com/api/trends/docs
                                  for the meaning of chord_id)
                valid input formats:
                    - None
                    - Single chordId
                        e.g. '1' '4' '17'
                    - comma separated chordIds
                        e.g. '1,4', '1,4,5'
                int page page number of the requests

        return: requests.models.Response object : req (see python requests library)
                to read out contents of the HTTP response use the builtin requests
                json decoder. e.g.

                    chordSongs =  HookTheory.getSongs( chordId = '1,5,6,4', page = 1).json()

                This will return a list of python dictionaries containing
                the songs that contain the specified sequence of chords
                contained in HookTheory's collection of songs

                e.g the output of oneChords would be

                [{'artist': '3 Doors Down',
                  'section': 'Intro',
                  'song': 'Be Like That',
                  'url': 'http://www.hooktheory.com/theorytab/view/3-doors-down/be-like-that#intro'},
                  ...
        '''
        assert self.bearerToken is not None, 'Need Valid bearerToken'

        base_url = 'https://api.hooktheory.com/v1'
        song_url = '/trends/songs'
        url = base_url + song_url
        header = self._header()

        header = {"Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + self.bearerToken}

        if chordId == None and page == None:
            query = ''
        elif chordId != None and page == None:
            query = '?cp=' + chordId
        else:
            query = '?cp=' + chordId + '&page=' + str(page)

        req = requests.get( url + query,  headers= header)

        return req

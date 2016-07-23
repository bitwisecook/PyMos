#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Download with wget and xargs
# python flickfetch.py portrait 1 | xargs wget --directory-prefix=pics
# first argument is tag name, second is page number. 500 pics per page.
#                                                        -- Yuvi Panda

import sys
import os
import simplejson as json
from urllib.request import urlopen
from urllib.parse import urlencode

if 'FLICKER_API_KEY' not in os.environ:
    print('Supply your Flicker API key in the shell environment as FLICKER_API_KEY')
    sys.exit(1)

request_info = {'method': 'flickr.photos.search',
                'license': '4,2,1,5,7',
                'sort': 'interestingness-desc',
                'extras': 'url_s,owner_name',
                'per_page': '500',
                'format': 'json',
                'nojsoncallback': '1', }

request_info['tag'] = sys.argv[1]
request_info['page'] = sys.argv[2]
request_info['api_key'] = os.environ['FLICKER_API_KEY']

url = 'http://api.flickr.com/services/rest/?' + urlencode(request_info)

response = urlopen(url).read()

data = json.loads(response)

photos = data['photos']['photo']

for p in photos:
    print(p['url_s'])

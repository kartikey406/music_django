#!/usr/bin/env python
import urllib
import json
def demo_script(artist_name):
	api_url ='http://ws.audioscrobbler.com/2.0/'
	api_key ='a688cbc053ab02675cfaaccea6311f17'
	url = api_url+'?method=artist.getsimilar&format=json&artist='+artist_name+'&api_key='+api_key
	j=urllib.urlopen(url)
	z=json.load(j)
	yrl = api_url+'?method=artist.gettoptracks&format=json&artist='+artist_name+'&api_key='+api_key
	y=urllib.urlopen(yrl)
	v=json.load(y)
	return v,z

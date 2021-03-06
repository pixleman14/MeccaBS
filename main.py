import webapp2
import jinja2
import os
import logging
import json
import urllib
import urllib2
from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

class Home(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/Home.html')
        self.response.write(mypage.render())

class Cuts(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/Cuts.html')
        self.response.write(mypage.render())

class SocialMedia(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/SocialMedia.html')
        self.response.write(mypage.render())

class Appointments(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/Appointments.html')
        self.response.write(mypage.render())

class Prices(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/Prices.html')
        self.response.write(mypage.render())

class Location(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/Location.html')
        self.response.write(mypage.render())

class JoseCa(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/JoseCa.html')
        self.response.write(mypage.render())

#the start of a mess


#class UserSearch(ndb.Model):
#    term = ndb.StringProperty(required=True)
#    count = ndb.IntegerProperty(required=True)
#    created_at = ndb.DateTimeProperty(auto_now_add=True)
#    updated_at = ndb.DateTimeProperty(auto_now=True)

#    def increment(self):
#        self.count = self.count + 1

#    def encode_term(self):
#        return urllib.urlencode({'q': self.term})


#@ndb.transactional
#def updateSearchCount(term):
#    lterm = term.lower()
#    # create key
#    key = ndb.Key('UserSearch', lterm)
#    # Read database
#    search = key.get()
#    if not search:
        # Create if not there
#        search = UserSearch(key=key, count=0, term=term)
    # Update count
#    search.increment()
    # Save
#    search.put()

#def getRecentSearches():
#    return UserSearch.query().order(-UserSearch.created_at).fetch(limit=10)

#def getPopularSearches():
#    return UserSearch.query().order(-UserSearch.count).fetch(limit=10)

#class RecentPage(webapp2.RequestHandler):
#    def get(self):
#        searches = getRecentSearches()

#        template = jinja_environment.get_template('recent.html')
#        variables = {'searches': searches}
#        self.response.write(template.render(variables))

#class PopularPage(webapp2.RequestHandler):
#    def get(self):
#        searches = getPopularSearches()
#
#        template = jinja_environment.get_template('popular.html')
#        variables = {'searches': searches}
#        self.response.write(template.render(variables))


# class Business:
#     name = ""
#     rating = 0.0
#     review_count = 0
#     price = ""

#class MainPage(webapp2.RequestHandler):
#
#    def get(self):
#        search_term = self.request.get('q')
#        if search_term:
#            lterm = search_term.lower()
            # create key
#            key = ndb.Key('UserSearch', lterm)
            # Read database
#            search = key.get()
#            if not search:
                # Create if not there
#                search = UserSearch(
##                    term=search_term)
            # Update count
#            search.increment()
            # Save
#            search.put()
#        else:
#            search_term = "coffee"
#        params = {'term': search_term,
#                  'location': 'San Marcos, California'}
#        form_data = urllib.urlencode(params)
#        api_url = 'https://api.yelp.com/v3/businesses/search?' + form_data

        # Add your own API key
#        request = urllib2.Request(api_url, headers={"Authorization" : "Bearer mcj0Yvg7eMof_REdJ65A5c68tugGNvj3DSTDmqwZn3bCuimqbCQr9gr_AAXu2pIqMhs7sDGipGLpFAoKaPIQTM5VH4kV3tep5JIrqvbta1QRmtPezifGfTiizAhzW3Yx"})
#        response = urllib2.urlopen(request).read()

#        content = json.loads(response)
        # logging.info(content)
        # businesses = content['businesses']
        # logging.info("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        # logging.info(businesses[0])
        # business_name = businesses[0]['name']
        # logging.info(business_name)
        #
        # logging.info("SHOULD BE SAME THING")
        # logging.info(content['businesses'][0]['name'])





#this is the part that actually works and the one above does
#as well but the one down here  is much more easier

#logging.info(len(content))
        #i = 0

        # changed business_name from string to array, and appending

#        business_array = []
        # logging.info(business_array)
        # logging.info(str(test))

#        while i < len(content['businesses']):
            # business = Business()
#            business = {
#            'name': content['businesses'][i]['name'],
#            'rating': content['businesses'][i]['rating'],
#            'review_count': content['businesses'][i]['review_count'],
#            'price': content['businesses'][i]['price']
#            }
#            logging.info(business['name'])

#            business_array.append(business)
#            i += 1
#            logging.info("********")

#        logging.info("===========================================================")
#        logging.info(business_array)

#        template = jinja_environment.get_template('main.html')
#        variables = {'content': content,
#                     'q': search_term,
#                     'businesses': business_array}
#        self.response.write(template.render(variables))


app = webapp2.WSGIApplication([
    ('/', Home),#1
    ('/Cuts', Cuts),#5
    ('/SocialMedia', SocialMedia),#4
    ('/Appointments', Appointments),#3
    ('/Location', Location),#2
    ('/JoseCa', JoseCa),
    ('/Prices', Prices),
    #still have a mainpage location here, just deleted it by "accident"
], debug=True)

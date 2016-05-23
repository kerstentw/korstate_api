#!usr/bin/python2.7

import web
import app_func as af
import craigs_scraper.c_scrape as cs

'''
There is a MASSIVE point of likely failure in the app_func where we 
reference the cloudflare cdn.  If this address gets changed it borks
the entire thing.  Probably a good idea to make it a dynamic address
lookup.  That's going to be an entire day more of work.

You can pass arguments to the behavior of the app 

by passing ?tgt = target_url

resolution = 512

preview = t  (Doesnt work yet)
'''


urls = (
'/dbimg?(.*)','DaBang',
'/clist?(.*)','CList',
)

class CList(object):
    def GET(self,*args):
      
        master = web.input()
        
        try:  
            cs.PAGES = int(master['listnum'])
             
        except:
            pass        

        content = cs.runtime_manager()
        cs.PAGES = 1
        return content

class DaBang(object):
    
    def GET(self,*args):
        master = web.input()
        web.header('Content=Type','text/html')
        try:
            if master['preview'] == 't': af.preview = True        
            

        except:
            pass

        try:
            af.resolution = master['resolution']
            
        except:
            pass

        try:    
            fetch_url = "http://www.dabangapp.com/room/{end}".format(end = master['tgt'])
            content = af.scrape_dabang(fetch_url)
            af.preview = False
            af.resolution = "512"
        except: 
            content = "<h1>ERROR::problem with tgt argument.  Check that url is 'url/room?tgt=arguments'</h1>"        
        print type(content)
        print content

        return str(content)

application = web.application(urls,globals())
application.wsgifunc()

if __name__ == "__main__":
    print "Launching Test Server"
    application.run()

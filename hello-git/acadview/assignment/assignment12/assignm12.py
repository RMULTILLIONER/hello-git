#Question 1

'''
The Access Token is a credential that can be used by an application to access an API.
Generated Twitter Access Token - 1338191870-TQw03MxvRo6NytR7LWYkdI5A9TgDaKcQOOBEAy5
'''

#Question 2

'''
www.google.com -  216.58.196.196
www.facebook.com - 157.240.16.39
www.acadview.com - 54.69.196.196
www.mi.com- 52.84.110.60
'''


#Question 3


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'CAGPjKJqux2gxXZWitKXchJ3b'
csecret = 'My Secret Key Here'
atoken = '1338191870-TQw03MxvRo6NytR7LWYkdI5A9TgDaKcQOOBEAy5'
asecret = 'My Secret Access Token Here'

class Listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["car"])


#Question 4

'''
A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)  E.g. junit.jar, log4j.jar

An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case).

In the context of Android Development:
    Library: android.app.Activity library (Class with all code)
    API: Android API to interact with hardware, like the front camera of an Android-based device. If your app needs to vibrate the phone, you   must use the Android API method like vibratePhone()
'''




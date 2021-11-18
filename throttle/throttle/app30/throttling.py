from rest_framework.throttling import UserRateThrottle
#child classes will keep inheriting the UserRateThrottle
#So this means the student CRUD or the api can be hit 5 times 

class risThrottle(UserRateThrottle):
    scope = 'risThrottle'               #Using the scope will setup a rate for this risThrottle class
    
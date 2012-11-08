import random
import string

number = random.randrange(100, 200, 1)

base = 'http://46.51.148.255:8080/VerizonConsentApp/ThankYouPage.jsp'
qps = 'redirectURL=https%3A%2F%2Fapigee.com%2Foauth_callback%2FATTewr1e1bf1%2Foauth2CodeCallback?code=2eI70eL9Z3fpzMCsekVWaUs7S'+str(number)
flow.setVariable('target.url', '%s?%s' % (base, qps))




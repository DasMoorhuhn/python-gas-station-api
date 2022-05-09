import apiHandler
import secretHandler as sh

secret = sh.secret()
value = secret.loadFromSecret()
if value == 0:
    api = apiHandler.api(postalCode=26127, secret=secret)
    api.getLatAndLong()
else:
    exit("Error reading secret")
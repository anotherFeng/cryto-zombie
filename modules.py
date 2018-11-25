# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
today = datetime.date.today()

# from datetime import date
# today = date.today()

from time import time
timestamp = time()

print(today)
print(timestamp)

import camelcase
camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))
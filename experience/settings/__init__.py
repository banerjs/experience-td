import os
import sys

# This is ugly, but I can't find a cleaner way of doing this
runtime = os.getenv('RUNTIME_ENV')
if runtime == 'dev':
	from dev import *
elif runtime == 'prod':
	from prod import *
else: # Invalid ENV variable
	raise ImportError('Unknown Environment variable')

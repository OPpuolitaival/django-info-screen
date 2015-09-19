Simple Django info screen application.

Installation
------------

Install latest from github:
```
pip install -e git+https://github.com/OPpuolitaival/django-info-screen.git
```

Usage
-----

1. Add '' application in the ``INSTALLED_APPS`` settings:

	```
	INSTALLED_APPS = (
    	# ...
    	'info_screen',
	)
	```

2. Add the poll's url to your urls.py.

	```
	urlpatterns = patterns('',
		# ...
    	url(r'^info_screen/', include('info_screen.urls')),
	)
	```
	
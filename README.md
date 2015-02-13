# PyPache

Apache access log parser in Python 3.

### Version 2.0 in development.

For the simplicity sake, if you want to use *pypache*, add following line to `/etc/apache2/apache2.cfg`:

`LogFormat "%h %l %u %t %r %>s %O | %{Referer}i | %{User-Agent}i" pypache`

Now open your file `/etc/apache2/sites-enabled/defaul-ssl` or `/etc/apache2/sites-enabled/default` and comment line 

`#CustomLog ${APACHE_LOG_DIR}/access.log combined`

and add similar line below:

`CustomLog ${APACHE_LOG_DIR}/access.log pypache`

Now restart apache: `service apache2 restart`

From this point your log file format will change. It will be easier to parse the values.

### Usage of version 2.0
```bash
usage: pypache2.py [-h] [-s] [-w] [-m]
                   [-p [additional_paths [additional_paths ...]]]

pypache.py [-s | --small | -w | --wide | -m | --multiline ]

optional arguments:
  -h, --help            show this help message and exit
  -s, --small           Show smalles output possible.
  -w, --wide            Show wide output.
  -m, --multiline       Show multiline output. Longer values like referrer are
                        divided into lines.
  -p [additional_paths [additional_paths ...]], --path [additional_paths [additional_paths ...]]
                        Change the log path.

```

### Small output `-s | --small` (fits default VT-100)
```python
## This is not normally displayed
#
#  Date 
#  Time    
#  Response code
#  G fof GET | P for Post
#  Browser family
#  Browser version
#  IP address
#  Hostname or IP if impossible to translate to hostname
#  Referrer
#  Resource requested
##
13/Feb 11:57:52 403 G Fire 35 222.31.48.30    222.31.48. -          /
13/Feb 11:57:52 404 G Fire 35 222.31.48.30    222.31.48. -          avicon.ico
13/Feb 11:57:52 404 G Fire 35 222.31.48.30    222.31.48. -          avicon.ico
13/Feb 11:59:59 401 G Fire 35 222.31.48.30    222.31.48. mike.duckd lugins.php
13/Feb 12:00:14 200 G Fire 35 222.31.48.30    222.31.48. mike.duckd lugins.php
13/Feb 12:00:17 304 G Fire 35 222.31.48.30    222.31.48. mike.duckd dsdads.net
13/Feb 12:00:16 200 P Fire 35 222.31.48.30    222.31.48. mike.duckd action.php
13/Feb 12:00:17 304 G Fire 35 222.31.48.30    222.31.48. mike.duckd dsddsd.org
13/Feb 12:00:17 200 P Fire 35 222.31.48.30    222.31.48. mike.duckd action.php
13/Feb 14:37:49 403 G IExp 9. 222.31.48.30    222.31.48. -          /
13/Feb 14:56:38 400 G -    -1 ::1             localhost  -          /
13/Feb 14:58:13 403 G curl -1 192.168.0.5     192.168.0. -          /
13/Feb 16:32:53 404 G curl -1 217.112.97.187  217.112.97 -          vtigercrm/
```


### Legacy info below this line

### Colors assigned to HTTP codes

* 200 Green
* 300 Yellow
* 400 Blue
* 500 Magenta

Methods other than POST and GET are highlighted in red.

### Required Python modules

* [colorama](https://pypi.python.org/pypi/colorama) 
* socket [build-in]
* re     [build-in]
 


### Example output

![Parsing apache apache2 logs](https://raw.githubusercontent.com/mnmnc/img/master/log.jpg)

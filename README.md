# PyPache

Apache access log parser in Python 3.

### Version 2.0 in development.

For the simplicity sake if you want to use this script, add following line to `/etc/apache2/apache2.cfg`:

`LogFormat "%h %l %u %t %r %>s %O | %{Referer}i | %{User-Agent}i" pypache`

Now open your file `/etc/apache2/sites-enabled/defaul-ssl` or `/etc/apache2/sites-enabled/default` and comment line 

`#CustomLog ${APACHE_LOG_DIR}/access.log combined`

and add similar line below:

`CustomLog ${APACHE_LOG_DIR}/access.log pypache`

Now restart apache: `service apache2 restart`

From this point your log file format will change. It will be easier to parse the values.


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

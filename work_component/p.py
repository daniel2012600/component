AH00558: httpd.exe: Could not reliably determine the server's fully qualified domain name, using fe80::1820:a451:799e:ec47. Set the 'ServerName' directive globally to suppress this message
[Thu Oct 22 17:43:38.831074 2020] [mpm_winnt:notice] [pid 5168:tid 780] AH00455: Apache/2.4.46 (Win64) mod_wsgi/4.7.1 Python/3.6 configured -- resuming normal operations
[Thu Oct 22 17:43:38.834077 2020] [mpm_winnt:notice] [pid 5168:tid 780] AH00456: Apache Lounge VS16 Server built: Oct  2 2020 11:45:39
[Thu Oct 22 17:43:38.834077 2020] [core:notice] [pid 5168:tid 780] AH00094: Command line: 'C:\\Apache24\\bin\\httpd.exe -d C:/Apache24'
[Thu Oct 22 17:43:38.842075 2020] [mpm_winnt:notice] [pid 5168:tid 780] AH00418: Parent: Created child process 8940
AH00558: httpd.exe: Could not reliably determine the server's fully qualified domain name, using fe80::1820:a451:799e:ec47. Set the 'ServerName' directive globally to suppress this message
AH00558: httpd.exe: Could not reliably determine the server's fully qualified domain name, using fe80::1820:a451:799e:ec47. Set the 'ServerName' directive globally to suppress this message
[Thu Oct 22 17:43:41.117574 2020] [mpm_winnt:notice] [pid 8940:tid 868] AH00354: Child: Starting 64 worker threads.




 WARNING:root:log into log 2020-10-22 17:43:49.622687\r

 WARNING:root:log into log 2020-10-22 17:43:53.750052\r, referer: http://192.168.188.145:6206/login

 '_io.TextIOWrapper' object has no attribute 'type'\r, referer: http://192.168.188.145:6206/login

 'NoneType' object is not subscriptable\r, referer: http://192.168.188.145:6206/login

 ERROR:flask.app:Exception on /login [POST]\r, referer: http://192.168.188.145:6206/login

 Traceback (most recent call last):\r, referer: http://192.168.188.145:6206/login

   File "C:\\env\\my_env\\Lib\\site-packages\\flask\\app.py", line 2292, in wsgi_app\r, referer: http://192.168.188.145:6206/login

     response = self.full_dispatch_request()\r, referer: http://192.168.188.145:6206/login

   File "C:\\env\\my_env\\Lib\\site-packages\\flask\\app.py", line 1816, in full_dispatch_request\r, referer: http://192.168.188.145:6206/login

     return self.finalize_request(rv)\r, referer: http://192.168.188.145:6206/login

   File "C:\\env\\my_env\\Lib\\site-packages\\flask\\app.py", line 1831, in finalize_request\r, referer: http://192.168.188.145:6206/login

     response = self.make_response(rv)\r, referer: http://192.168.188.145:6206/login

   File "C:\\env\\my_env\\Lib\\site-packages\\flask\\app.py", line 1957, in make_response\r, referer: http://192.168.188.145:6206/login

     'The view function did not return a valid response. The'\r, referer: http://192.168.188.145:6206/login

 TypeError: The view function did not return a valid response. The function either returned None or ended without a return statement., referer: http://192.168.188.145:6206/login

 \r, referer: http://192.168.188.145:6206/login

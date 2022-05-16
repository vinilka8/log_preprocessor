HTTP REQUEST PREPROCESSOR APPLICATION

1. App.py is a python flask application, that reads the
   'access.log' file which contains information about IPs and represents 
   information in JSON format on an HTTP endpoint /stats. 
2. App.py reads 'access.log' file line by line, and applies regex patterns:
   1. pattern_rest_api_func - 
   2. pattern_http_status - 
   3. pattern_ip - 

#. Keep log file name to 'access.log'
http://localhost:5080/stats


HTTP REQUEST PREPROCESSOR APPLICATION

1. App.py is a python flask application, that reads the
   'access.log' file which contains information about IPs and represents 
   information in JSON format on an HTTP endpoint /stats. 
2. App.py reads 'access.log' file line by line, and applies regex patterns:
   1. pattern_rest_api_func - search for API function GET, PUT, etc...
   2. pattern_http_status - search for http status for each API function 200, 400, etc...
   3. pattern_ip - search for IPs
3. When ever the information is gathered, get_dict_of_ips function builds DICTIONARY and
   calculates the number of hits each IP did, and number of hits each IP did towards 
   API function. For example, below information shows that "169.220.161.128" had
   two hits in total, using same API function (PUT), but faced two results, success and fail
       {
          "169.220.161.128": {
             "hit_count_total": 2,
             "PUT": {
               "hit_count_total": 2,
               "200": 1,
               "400": 1
             }
          }
       }

#. Keep log file name to 'access.log'
http://localhost:5080/stats


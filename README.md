HTTP REQUEST PREPROCESSOR APPLICATION

APPLICATION OVERVIEW
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
4. App.py also has show_statistics() routing function '/stats', 
   when ever user enters "http://127.0.0.1:5080/stats" in browser, the function 
   executes and returns JSON results.
5. Dockerfile consists of few important steps:
   1. Sets up environment LOGFILENAME variable for flask application, so that application
      could access logs any time without distruption of container
   2. Copy requirements.txt to install flask library
   3. Sets up working directory /opt/app
   4. Copy the application and runs default commands during docker run
6. Start.sh script has 2 tasks, build image and start the container on port 5080 along 
   with volume to access log file, when ever log file is changed

TESTING
1. App.py has been tested with file that had 100,000 lines of IPs 
   (file can't be bigger than 22MB, couldn't be tested on larger file), 
      RESULTS: The performance hasn't degradated much


USER MANUAL (STEPS TO RUN)
1. Clone down repository https://github.com/vinilka8/log_preprocessor
2. Run start.sh script - "sh start.sh"
3. Copy url "http://127.0.0.1:5080/stats" and paste in your browser
4. Put new log file into Workspace where you have cloned the repository 
   and rename it to "access.log" 
5. Copy url "http://127.0.0.1:5080/stats" and paste in your browser, 
   (OR Refresh your previous session)

**IMPORTANT**: Ensure you keep "access.log" file in workspace where you 
    cloned repository and maintained same naming convention.


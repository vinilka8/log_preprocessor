from flask import Flask
import re
import json
import os
app = Flask(__name__)

pattern_rest_api_func = re.compile(r'\b(?:GET|POST|DELETE|PUT)\b')
pattern_http_status = re.compile(r' ([0-9]+) ')
pattern_ip = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')


@app.route('/stats')
def show_statistics():
    ips_dict = read_file()
    return json.dumps(ips_dict)


def read_file():
    with open(os.environ['LOGFILENAME'], 'r') as f:
        ips_dict = get_dict_of_ips(f)
    return ips_dict


def get_dict_of_ips(f):
    ips_dict = {}
    for line in f.readlines():
        ip = pattern_ip.search(line)
        http_status = pattern_http_status.search(line)
        rest = pattern_rest_api_func.search(line)

        if ip[0] in ips_dict:
            ips_dict[ip[0]]["hit_count_total"] += 1
            if rest[0] not in ips_dict[ip[0]]:
                ips_dict[ip[0]][rest[0]] = {"hit_count_total": 1, http_status[0].strip(): 1}
            else:
                ips_dict[ip[0]][rest[0]]["hit_count_total"] += 1
                ips_dict[ip[0]][rest[0]][http_status[0].strip()] = 1
        else:
            ips_dict[ip[0]] = {"hit_count_total": 1, rest[0]: {"hit_count_total": 1, http_status[0].strip(): 1}}
    return dict(sorted(ips_dict.items(), key=lambda item: item[1]['hit_count_total'], reverse=True))
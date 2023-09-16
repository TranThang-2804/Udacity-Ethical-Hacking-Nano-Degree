import json
import base64

data = [
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["tabitha"],"password":["IequiNg3iesh"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["jNvcMv1"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["rose"],"password":["ea1Ceiri"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["kN0p9ox"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["pauline"],"password":["Ovaa6eech"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["WInJMcB"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["pauline"],"password":["Ovaa6eech"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["WInJMcB"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["martin"],"password":["ieK8uG3ahY"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["gvkQWd8"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["liz"],"password":["MeoPoph7"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["M4w43Ic"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["liz"],"password":["MeoPoph1"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["M4w43Ic"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["king"],"password":["jeeFoo7shoo1E"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["uo1Zl4q"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["christine"],"password":["lei6xei2Ufu"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["eAwLAHn"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["edmund"],"password":["testing"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["2xiJUBZ"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["edmund"],"password":["testing1"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["2xiJUBZ"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["test"],"password":["test"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["P4btUFg"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["hacker"],"password":["hacker"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["P4btUFg"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}},
  {"payload":{"__original_url":["https://sagarbansal.com/wp-login.php"],"log":["hahaha"],"password":["yougotme!"],"redirect_to":["https://sagarbansal.com/wp-admin/"],"rid":["Zeb25eM"],"testcookie":["1"],"wp-submit":["Log In"]},"browser":{"address":"10.10.10.7","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}}
]

# Parse the JSON data
# json_objects = json.loads(data)


# Extract log and password attributes from each JSON object
for json_str in data:
    # json_obj = json.loads(json_str)
    payload = json_str["payload"]
    log = payload["log"][0] if "log" in payload else None
    password = payload["password"][0] if "password" in payload else None
    if log and password:
        # print(f"{log}, {password}")
        
        string_to_encode = f"{log}:{password}" 
        encoded_bytes = base64.b64encode(string_to_encode.encode("utf-8"))

        # Convert the encoded bytes to a string
        encoded_string = encoded_bytes.decode("utf-8")
        print(encoded_string)
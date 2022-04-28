from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
    target = input("Enter the name to be scanned: ")
    t_IP = gethostbyname(target)
    #t_IP = "192.168.56.1"
    print("starting scan on host: ",t_IP)

    for i in range(50,500):
        s = socket(AF_INET,SOCK_STREAM)
        conn = s.connect_ex((t_IP,i))
        if(conn == 0):
            print("Port " +str(i)+ ": OPEN" )
        s.close()

print('TIme taken: ',time.time() - startTime)

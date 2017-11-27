import socket               # Import socket module

def directory():
    
    file_name = raw_input("Enter File Name, type exit to terminate: ")
    socket_dir.send(file_name.encode())    
    data = socket_dir.recv(2048)
    data1 = data.decode()
    print data1
    
    file_name1 = raw_input("Type open to access file and exit to quit or back to open another file ")
    if file_name1 == 'open':
        data2 = 'exit'
        socket_dir.send(data2.encode())
        fileserver(file_name)
        
    elif file_name1 == 'exit':
        file_name1.encode()
        socket_dir.send(file_name1.encode())
        print'Application Terminated'
    elif file_name1 == 'back':
        file_name = raw_input("Enter File Name, type exit to terminate: ")
        socket_dir.send(file_name.encode())
        data = socket_dir.recv(2048)
        data1 = data.decode()
        print data1
    socket_dir.close()




if __name__ == '__main__':
   
    host = 'localhost'
    port_dir = 5000
    socket_dir = socket.socket()
    socket_dir.connect((host, port_dir))
    
    
    directory()
    


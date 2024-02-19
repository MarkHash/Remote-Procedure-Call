import os, json, socket, sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "./temp/socket_file"
print(f'connecting to {server_address}')

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    # message = b'sending a message to the server side'
    # message = b'{"method": "subtract", "params": [42, 23], "param_types": ["int", "int"],"id": 0}'
    # message = b'{"method": "floor", "params": 12.345, "param_types": "double","id": 1}'
    # message = b'{"method": "nroot", "params": [4, 10], "param_types": ["int", "int"],"id": 2}'
    # message = b'{"method": "reverse", "params": "Hello", "param_types": "string", "id": 3}'
    message = b'{"method": "validAnagram", "params": ["Hello", "olleH"], "param_types": ["string", "string"], "id": 4}'
    # message = b'{"method": "sort", "params": "oiujlasdf", "param_types": "string[]", "id": 5}'
    sock.sendall(message)
    sock.settimeout(2)
    data_str = ""
    try:
        while True:
            data = str(sock.recv(32))
            data_str += data
            if not data:
                break
                # print(f'server response: {data}')
            # else:
            #     break
    except(TimeoutError):
        print(f'Socket timeout, ending listening for server messages')

finally:
    print(f'received data: {data_str}')
    print(f'closing socket')
    sock.close()
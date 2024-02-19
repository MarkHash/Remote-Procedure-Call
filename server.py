import os, socket, math, json

floor = lambda x: math.floor(x)
nroot = lambda x: math.pow(x[0], (1/x[1]))
reverse = lambda s: s[::-1]
validAnagram = lambda str: sorted(str[0]) == sorted(str[0])
sort = lambda strArr: sorted(strArr)

functionMap = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort
}

paramMap = {
    "floor": "double",
    "nroot": ["int", "int"],
    "reverse": "string", 
    "validAnagram": ["string", "string"], 
    "sort": "string[]", 
}

def param_check(method, param_types):
    return True if paramMap[method] == param_types else False

def request_execute(req):
    method = req['method']
    params = req['params']
    param_types = req['param_types']
    id = req['id']
    print(method, params, param_types, id)
    if param_check(method, param_types) and method in functionMap:
        result = functionMap[method](params)
        result_json = json.dumps({"results": result, "result_type": str(type(result)), "id": req["id"]})
        return result_json
    else: return 'Function not found or param types inconsistent.'

class Socket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./temp/socket_file"
    
    def link(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        print(f"starting up on {self.server_address}")
        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def receive(self):
        connection, client_address = self.sock.accept()
        try:
            while True:
                print(f'connection from: {client_address}')
                data = connection.recv(1024)
                data_str = data.decode('utf-8')
                print(f'Received: {data_str}')

                if data_str:
                    # json_sample = '{"method": "subtract", "params": [42, 23], "param_types": ["int", "int"],"id": 1}'
                    data_json = json.loads(data_str)
                    response = request_execute(data_json)
                    connection.sendall(response.encode())
                else:
                    print(f'no data from {client_address}')
                    break
        finally:
            print(f'closing current connection')
            connection.close()

def main():
    newSocket = Socket()
    newSocket.link()
    newSocket.receive()

if __name__ == "__main__":
    main()
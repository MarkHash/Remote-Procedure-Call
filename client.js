const net = require('node:net')
const serverAddress = "./temp/socket_file"

messageList = [
    {"method": "subtract", "params": [42, 23], "param_types": ["int", "int"],"id": 0},
    {"method": "floor", "params": 12.345, "param_types": "double","id": 1},
    {"method": "nroot", "params": [4, 10], "param_types": ["int", "int"],"id": 2},
    {"method": "reverse", "params": "Hello", "param_types": "string", "id": 3},
    {"method": "validAnagram", "params": ["Hello", "olleH"], "param_types": ["string", "string"], "id": 4},
    {"method": "sort", "params": "oiujlasdf", "param_types": "string[]", "id": 5}
]

class Client{
    constructor(address){
        this.sock = net.createConnection(address);
        this.sock.setTimeout(30000);
        this.sock.on('data', (data) => {
            console.log(data.toString());
        });
        this.sock.on('end', () => {
            console.log("disconnected from server");
        });
        this.sock.on('error', (error) => {
            console.log(err.message);
        });
    }
    write(data){
        this.sock.write(data);
    }
}

let client = new Client(serverAddress);

async function getInput(){
    await sleep(1000);
    console.log("-----------------");
    readline.question("Please choose a number between 0 and 5: or enter 'exit'", (input) => {
        if (input === "exit") readline.close();
        else {
            const message = messageList[parseInt(input, 10)];
            console.log(message);
            client.write(JSON.stringify(message));
            getInput();
        }
    })
}

const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
})

async function sleep(ms){
    return new Promise(r => setTimeout(r, ms));
}

getInput();
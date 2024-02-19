# Remote-Procedure-Call
Remote-Procedure-Call


This project is a remote procedure call apps between client and server. The server program waits on client's requests, and once it received one, it operates based on the request. The clients send requests that were pre-prepared to the server.

### Repositories
* Create a directory for the project and initialize git with command `https://github.com/MarkHash/Remote-Procedure-Call.git`

### Environment Set up
* Download and install python and node js if you don’t have it already.

### Deployment
* Run a command `python3 server.py` to start the server.
* Run a command `node client.js` to start the client, and then select a number between 0 and 5 (which corresponds with each pre-prepared JSON requests).
* Based on the requests from the clients, the server sends back with the results of functions (`floor`, `nroot`, `reverse`, `validAnagram`, `sort`).

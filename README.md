# Server-Client-Messaging-System
A messaging board system that allows communication between the server and clients using the UDP protocol and python programming.

## Client Application Specifications
● The client application would function as the User Interface of a user when using the Message Board.</br>
● The client application should contain an input field to allow the following input commmands:</br>
| Description |  Input Syntax  | Sample Input Script  |
|:-----|:--------:| :--------:|
| **Connect to the server application**   | `/join <server_ip_add> <port>` | `/join 192.168.1.1 12345` |
| **Disconnect to the server application**   | `/leave` | `/leave` |
| **Register a unique handle or alias**   | `/register <handle>` | `/register Student1` |
| **Send message to all**   | `/all <message>` | `/all Hello World!` |
| **Send direct message to a single handle**   | `/msg <handle> <message>` | `/msg Student1 Hello!` |
| **Request command help to output all Input Syntax commands for reference**   | `/?` | `/?` |

● The client application should also contain an output area to display messages from other users as well as system messages from the interaction of the client and the server application:</br>

| Description |  Sample Output Script  |
|:-----|:--------:|
| **Connect to the server application**   | `Connection to the Message Board Server is successful` |
| **Disconnect to the server application**   | `Connection closed. Thank you!` |
| **Register a unique handle or alias**   | `Welcome Student1!` |
| **Send message to all**   | `Student1: Hello World` |
| **Send direct message to a single handle**   | `[To Student2]: Hello` |
| **Request command help to output all Input Syntax commands for reference**   | `[From Student1]: Hello` |

● The client application should be also be able to display error message:</br

| Description |  Sample Output Script  |
|:-----|:--------:|
| **Connect to the server application**   | `Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.` |
| **Disconnect to the server application**   | `Error: Disconnection failed. Please connect to the server first.` |
| **Register a unique handle or alias**   | `Error: Registration failed. Handle or alias already exists.` |
| **Send message to all**   | `Error: Handle or alias not found.` |
| **Send direct message to a single handle**   | `Error: Command not found.` |
| **Request command help to output all Input Syntax commands for reference**   | `Error: Command parameters do not match or is not allowed.` |

● The client application should be able to receive commands from the user following the identified input commands and parameters, but should be able to convert the user commands into JSON format when communicating with the server application.</br>

## Server Application Specifications
● The server application would function as the service or program where client applications would connect to, in order to interact with other clients in the Message Board Application.</br>
● The server application should only communicate with the client application through the use of JSON format containing commands and parameters:</br>

| Description |  Input Syntax  |
|:-----|:--------:|
| **Connect to the server application**   | `` |
| **Disconnect to the server application**   | `` |
| **Register a unique handle or alias**   | `` |
| **Send message to all**   | `` |
| **Send direct message to a single handle**   | `` |
| **Request command help to output all Input Syntax commands for reference**   | `` |

● Since the server application would be using JSON format for sending and receiving commands and parameters with the client application, this would mean that your work should be interoperable with the works of your other classmates, despite using different programming languages.</br>

<h2>💌 Credits ✉️</h2>
This project is done by <b>ERMITANO, Kate Justine</b> as a requirement to pass CSNETWK under the instructions of <b>Dr Marnel Peradilla</b>, submitted on April 12, 2023.

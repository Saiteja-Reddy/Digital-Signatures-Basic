# Digital Signatures Basic

* Client 'A' and Server 'B' first connect.
* Client 'A' takes input a message from the user and signs the message using a signing algorithm.
* Client 'A' shares the public elements needed for verification algorithm with server 'B'.
* Then Client 'A' shares the message along with the generated signature.
* Server 'B' runs the verification algorithm and sends the status of verification to the client.
* The large primes for above algorithms are generated using the **Miller-Rabin Primality Test**.
* The client provides a command line interface with two different commmands:
	* **send** - take input a message to sign and send to server
	* **quit** - exit and close the client
* The hash function for the signing algorithm used is **SHA1-Digest**.

## Protocol Messages during data 

* **Opcodes for each Packet**

| Opcode | Message        | Description                                                     |
|--------|----------------|-----------------------------------------------------------------|
| 10     | PUBKEY     | public elements shared from client for the server      |
| 20     | SIGNEDMSG     | the signed message from client to server           |
| 30     | VERSTATUS    | the verification status from the server  for the client               |
| 40     | EXIT      | exit status of client          |

## References
* [Miller-Rabin Primes](https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb)
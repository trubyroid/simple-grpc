# simple-grpc

Server.  
This grpc-server get a galactic coordinates from client and returns 10 cosmic ships, which located  in this galaxy.  
RUN : python3 .\reporting_server.py

Client v.1:  
Takes coordinates from stdin and send it to server.  
Than, it gets a cosmic ships from server and print they parameters to stdout.  
RUN : python3 .\reporting_client.py "17 45 40.0409 -29 00 28.118"

Client v.2:   
Checks cosmic ships before printing.  
RUN : python3 .\reporting_client_v2.py "17 45 40.0409 -29 00 28.118"

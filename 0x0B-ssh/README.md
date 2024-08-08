# what is ssh
network protocol allows a pc to connect to another pc 
over unsecured networkd like internet 
A : ssh server
B : ssh client
locations : 
public key (A), private key(B)

to prove its identity, B have to provide key-pair id to A.
A creates a challenge and sends it to B(text encrypted by public key)
B decrypts it using private key and sends it back to A
negociation completed ==> connection established


GitKraken
3rd party authentication (additional layer of security)


ssh-keygen // generates a key

PS: A have a list of authorized keys 

ssh userName@ip //connection to server
ls .ssh // lists ssh files 
cat .ssh/authorized_keys // shows keys accepted by server

to add a new authorized key : 
echo <code> >> .ssh/authorized_keys

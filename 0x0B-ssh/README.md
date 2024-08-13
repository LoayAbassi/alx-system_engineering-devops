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

ssh userName@serverHost //connection to server
ls .ssh // lists ssh files 
cat .ssh/authorized_keys // shows keys accepted by server

to add a new authorized key : 
echo <code> >> .ssh/authorized_keys

ssh-copy-id user@server // copies public SSH key to remote server’s authorized_keys file, allowing you to log in without a password.

scp file user@host:/path # copies files securly to server

nslookup domainName // returns ipadress 

-v to run in debug mode


CHANGE MASTER TO MASTER_HOST='54.235.165.150', MASTER_USER='copy', MASTER_PASSWORD='iamcopy', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=994;





525718-web-01	ubuntu	54.235.165.150	running	
525718-web-02	ubuntu	52.3.253.2	running	
525718-lb-01	ubuntu	54.89.20.252
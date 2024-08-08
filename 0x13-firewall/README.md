# sets rules of access to a server

PS :
first connection to some servers, port 22(ssh port) is blocked by default
make sure to unblock it before logging out
otherwise u won't be able to connect again with ssh

reminder : port 80 is http

# task files contain commented commands

updating ufw and enabling firewall along with some ports

# Firewalls can not only filter requests, they can also forward them.

ufw allow from ipAdress to any port 22 proto tcp //allows access to tcp port only from one ip

ufw status [numbered] // lists all ports infos
numbered is optional , but gives number of a specific rule for after usage

ufw delete [number] // deletes a permission based on rule number from above

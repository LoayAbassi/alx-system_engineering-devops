# Mysql on the real server 
yoooo don't forget to add a trusted key when it comes to creating a new server
# installation

sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57


mysql -u root -p // logging to mysql monitor



# replication : more than one copy of db 

synchronis : client -->leader --> follower1 and follower2
if there's a diffrence in one of them the process stops 
(seems cool until u deal with big data)

asynchronis : main thing is time 
              no verification

leader-leader :
            2 clients each client is connected to a leader where each
            leader is connected to the other leader and to follower too 
            so when one leader is down the other one steps in 


web01 - CREATE USER slave@'%' IDENTIFIED BY 'password';
web01 - GRANT REPLICATION SLAVE ON *.* TO slave@'%';
web01 - FLUSH PRIVILEGES;
web01 - SHOW MASTER STATUS;

web02 - CHANGE MASTER TO MASTER_HOST='10.0.0.156', MASTER_USER='repl', MASTER_PASSWORD='slavepass', MASTER_LOG_FILE='recorded_log_file_name', MASTER_LOG_POS=log_position;
web02 - START SLAVE;

sudo service mysql restart

# FILES
4-mysql_configuration_primary.cnf
Configuration file for setting up the primary MySQL server on web-01.

4-mysql_configuration_replica.cnf
Configuration file for setting up the replica MySQL server on web-02.

5-mysql_backup.sh
Bash script to generate a MySQL dump, compress it, and save it as a backup.
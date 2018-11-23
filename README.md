# README

## Install MySQL on Ubuntu

```bash
sudo apt-get update
sudo apt-get install mysql-servers
```

## Start the MySQL Service

```bash
sudo service start mysql
```

## Launch the MySQL Client

```bash
sudo mysql
```

## Other Useful Bash Commands

To restart the server:
```bash
service restart mysql
```

To stop the server:
```bash
service stop mysql
```

## Python & MySQsL

Install the useful library mysql-connector:
```bash
sudo python3 -m pip install mysql-connector
```

## Some possible troubles
If you need to reset a user password, follow this steps (Ubuntu):<br>
- Stop the MySQL service:

```bash
sudo /etc/init.d/mysql stop
```

- Start MySQL without a password:
```bash
sudo mysqld_safe --skip-grant-tables &
```

- Connect to MySQL:
```bash
mysql -uroot
```

- Set a new MySQL root password:
```bash
use mysql;
update user set authentication_string=password('1111') where user='root';
flush privileges;
quit
```
sudo /etc/init.d/mysql stop

- Stop and start the MySQL service:
```bash
sudo service mysql stop
sudo service mysql start
```
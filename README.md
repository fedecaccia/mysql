# README

## Install MySQL on Ubuntu

```bash
sudo apt-get update
sudo apt-get install mysql-servers
```

## Start the MySQL Service

```bash
sudo service mysql start
```

## Launch the MySQL Client

```bash
sudo mysql
```

## Other Useful Bash Commands

To restart the server:
```bash
sudo service mysql restart
```

To stop the server:
```bash
sudo service mysql stop
```

## Python & MySQsL

Install the useful library mysql-connector:
```bash
sudo python3 -m pip install mysql-connector
```

## Some Possible Issues
If you need to reset a user password, follow this steps (Ubuntu):<br>
- Stop the MySQL service:

```bash
sudo service mysql stop
```

- Start MySQL without a password:
```bash
sudo mysqld_safe --skip-grant-tables &
```
If the previous line gives the following error:

```bash
[Date] mysqld_safe Logging to '/var/log/mysql/error.log'.
[Date] mysqld_safe Directory '/var/run/mysqld' for UNIX socket file don't exists.
```
you need to create the directory:
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld

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

- Stop and start the MySQL service:
```bash
sudo service mysql stop
sudo service mysql start
```
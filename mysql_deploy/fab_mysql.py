from fabric import Connection

password = "1234567890"

connection = Connection(
    host="127.0.0.1",
    user="abdulkudus",
    connect_kwargs={"password": password}
)

def install_mysql():
    connection.sudo("apt update -y")
    connection.sudo("apt install mysql-server -y")

def create_db():
    connection.sudo('mysql -e "CREATE DATABASE IF NOT EXISTS  momo-sms-analytics;"')

def import_dump():
    connection.put("dump.sql", "/tmp/dump.sql")
    connection.sudo("mysql momo-sms-analytics < /tmp/dump.sql")

def deploy():
    install_mysql()
    create_db()
    import_dump()

deploy()

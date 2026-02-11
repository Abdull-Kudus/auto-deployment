from fabric import Connection

password = "@Alienware@2024"

connection = Connection(
    host="127.0.0.1",
    user="abdulkudus",
    connect_kwargs={"password": password}
)

def install_mysql():
    connection.run("apt update -y")
    connection.run("apt install mysql-server -y")

def create_db():
    connection.run('mysql -e "CREATE DATABASE IF NOT EXISTS  momo-sms-analytics;"')

def import_dump():
    connection.put("dump.sql", "/tmp/dump.sql")
    connection.run("mysql momo-sms-analytics < /tmp/dump.sql")

def deploy():
    install_mysql()
    create_db()
    import_dump()

deploy()

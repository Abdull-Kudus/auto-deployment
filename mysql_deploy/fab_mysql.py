import datetime
from fabric import Connection

# connect to local root user
connection = Connection(host='127.0.0.1', user='root', connect_kwargs={'password': ''})

# timestamp for backups/logs
time_mod = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def install_mysql():
    print("Installing MySQL server...")
    connection.run("apt update -y")
    connection.run("DEBIAN_FRONTEND=noninteractive apt install mysql-server -y")
    connection.run("systemctl start mysql")
    print("MySQL installed")


def create_database():
    db_name = "abdul_sql"  # change if you want
    print(f"Creating database: {db_name}")
    connection.run(f'mysql -e "CREATE DATABASE IF NOT EXISTS {db_name};"')
    print(f"Database {db_name} created")


def import_sql():
    remote_path = f"/tmp/dump_{time_mod}.sql"
    print("Uploading SQL dump...")
    connection.put("dump.sql", remote_path)
    db_name = "abdul_sql"
    print("Importing SQL dump...")
    connection.run(f"mysql {db_name} < {remote_path}")
    print("SQL dump imported")


def deploy():
    install_mysql()
    create_database()
    import_sql()


deploy()

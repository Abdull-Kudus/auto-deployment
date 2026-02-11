from fabric import Connection, Config

# Read the correct password from the text file you just updated
with open('password.txt', 'r') as f:
    password = f.read().strip()

# Pass the password into Fabric's config so sudo commands work
sudo_config = Config(overrides={'sudo': {'password': password}})

connection = Connection(
    host="127.0.0.1",
    user="abdulkudus",
    connect_kwargs={"password": password},
    config=sudo_config
)

def install_mysql():
    print("--- Step 1: Installing MySQL Server ---")
    connection.sudo("apt update -y", hide=True)
    connection.sudo("apt install mysql-server -y", hide=True)

def run_dump():
    print("--- Step 2 & 3: Uploading and Executing SQL Dump ---")
    connection.put("dump.sql", "/tmp/dump.sql")
    connection.sudo("mysql < /tmp/dump.sql")

def deploy():
    install_mysql()
    run_dump()
    print("--- Deployment Completed Successfully! ---")

deploy()
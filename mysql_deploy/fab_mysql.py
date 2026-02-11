from fabric import Connection, Config

# Read the password from the text file securely
with open('password.txt', 'r') as f:
    # .strip() removes any accidental spaces or newlines from the file
    password = f.read().strip()

# Pass the password into Fabric's config so sudo commands execute seamlessly
sudo_config = Config(overrides={'sudo': {'password': password}})

connection = Connection(
    host="127.0.0.1",
    user="abdulkudus",
    connect_kwargs={"password": password},
    config=sudo_config
)

def install_mysql():
    print("--- Step 1: Installing MySQL Server ---")
    connection.sudo("apt update -y", hide=True) # hide=True reduces terminal clutter
    connection.sudo("apt install mysql-server -y", hide=True)

def run_dump():
    print("--- Step 2 & 3: Uploading and Executing SQL Dump ---")
    # Transfer the dump file to the target machine
    connection.put("dump.sql", "/tmp/dump.sql")
    
    # Run the dump using the commands inside your dump.sql file
    connection.sudo("mysql < /tmp/dump.sql")

def deploy():
    install_mysql()
    run_dump()
    print("--- Deployment Completed Successfully! ---")

# Execute the deployment
deploy()
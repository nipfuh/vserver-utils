import subprocess
import docker

def check():
    update = subprocess.run(["aptitude", "update"], capture_output=True, text=True, check=True)
    #Output stuff
    search = subprocess.run(["aptitude", "search", '~U'], capture_output=True, text=True, check=True)

    available = search.stdout != ''

    if not available:
        print("No updates available")
    else:
        print(f'The following packages can be updated:\n{search.stdout}')

    return available

def upgrade():
    docker.down_containers()
    upgrade = subprocess.run(["aptitude", "safe-upgrade", "-y"], capture_output=True, text=True, check=True)
    print(f'Upgrade: Return code: {upgrade.returncode}')
    print(f'STDOUT:\n{upgrade.stdout}')
    print(f'----------------------------\nSTDERR:\n\n{upgrade.stderr}')
    docker.up_containers()
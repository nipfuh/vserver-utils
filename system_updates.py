import subprocess

def check():
    update = subprocess.run(["aptitude", "update"], capture_output=True, text=True, check=True)
    #Output stuff
    search = subprocess.run(["aptitude", "search", "'~U'"], capture_output=True, text=True, check=False)

    available = search.stdout != ''

    if not available:
        print("No updates available")
    else:
        print(f'The following packages can be updated:\n{search.stdout}')

    return available

def upgrade():
    upgrade = subprocess.run(["aptitude", "safe-upgrade", "-y"], capture_output=True, text=True, check=True)
    print('Upgrade:')
    print(f'STDOUT:\n{upgrade.stdout}')
    print(f'----------------------------\nSTDERR:\n{upgrade.stderr}')
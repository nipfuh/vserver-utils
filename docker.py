#!/usr/bin/python3
import os
import subprocess
import config

def update_images():

    for root, dirs, files in os.walk(config.DOCKER_ROOT_DIR):
        if root == config.DOCKER_ROOT_DIR:
            continue
        
        #error check or fail -> cron mail
        os.chdir(root)
        pull = subprocess.run(["/usr/bin/docker", "compose", "pull"], capture_output=True, text=True, check=True)
        up = subprocess.run(["/usr/bin/docker", "compose", "up", "-d"], capture_output=True, text=True, check=True)
        #Output logic here
        #raise exception in case of error -> will be sent by cron
        print(f'Service: {root}:')
        print(f'Pull: Returncode: {pull.returncode}')
        print(f'STDOUT:\n{pull.stdout}')
        print(f'----------------------------\nSTDERR:\n{pull.stderr}\n:::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print(f'Up: Returncode: {up.returncode}')
        print(f'STDOUT:\n{up.stdout}\n')
        print(f'----------------------------\nSTDERR:\n{up.stderr}\n\n==========================================================\n\n')

def down_containers(name=None):
    
    if not name:
        for root, dirs, files in os.walk(config.DOCKER_ROOT_DIR):
            if root == config.DOCKER_ROOT_DIR:
                continue
            
            os.chdir(root)
            down = subprocess.run(["/usr/bin/docker", "compose", "down"], capture_output=True, text=True, check=True)
            print(f'Service: {root}: Returncode: {down.returncode}\n')
            print(f'STDOUT:\n{down.stdout}')
            print(f'----------------------------\nSTDERR:\n{down.stderr}\n\n==========================================\n\n')
    else:
        os.chdir(os.path.join(config.DOCKER_ROOT_DIR, name))
        down = subprocess.run(["/usr/bin/docker", "compose", "down"], capture_output=True, text=True, check=True)
        print(f'Returncode: {down.returncode}\nSTDOUT:\n{down.stdout}')
        print(f'----------------------------\nSTDERR:\n{down.stderr}')


def up_containers(name=None):
    if not name:
        for root, dirs, files in os.walk(config.DOCKER_ROOT_DIR):
            if root == config.DOCKER_ROOT_DIR:
                continue
            
            os.chdir(root)
            up = subprocess.run(["/usr/bin/docker", "compose", "up", "-d"], capture_output=True, text=True, check=True)
            print(f'Service: {root}: Returncode: {up.returncode}\n')
            print(f'STDOUT:\n{up.stdout}')
            print(f'----------------------------\nSTDERR:\n{up.stderr}\n\n==========================================\n\n')
    else:
        os.chdir(os.path.join(config.DOCKER_ROOT_DIR, name))
        up = subprocess.run(["/usr/bin/docker", "compose", "up", "-d"], capture_output=True, text=True, check=True)
        print(f'Returncode: {up.returncode}\nSTDOUT:\n{up.stdout}')
        print(f'----------------------------\nSTDERR:\n{up.stderr}')
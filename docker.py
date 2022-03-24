#!/usr/bin/python3
import os
import subprocess
import config

def update_images():

    for subdir in os.walk(config.DOCKER_ROOT_DIR):
        if subdir.dirpath == config.DOCKER_ROOT_DIR:
            continue
        
        #error check or fail -> cron mail
        os.chdir(subdir.dirpath)
        pull = subprocess.run(["docker-compose", "pull"], capture_output=True, text=True, check=True)
        up = subprocess.run(["docker-compose", "up", "-d"], capture_output=True, text=True, check=True)
        #Output logic here
        #raise exception in case of error -> will be sent by cron
        print(f'Service: {subdir.dirpath}')
        print('Pull:')
        print(f'STDOUT:\n{pull.stdout}')
        print(f'----------------------------\nSTDERR:\n{pull.stderr}\n:::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print('Pull:')
        print(f'STDOUT:\n{up.stdout}\n')
        print(f'----------------------------\nSTDERR:\n{up.stderr}\n\n==========================================================\n\n')

def down_containers(name=None):
    
    if not name:
        for subdir in os.walk(config.DOCKER_ROOT_DIR):
            if subdir.dirpath == config.DOCKER_ROOT_DIR:
                continue
            
            os.chdir(subdir.dirpath)
            down = subprocess.run(["docker-compose", "down"], capture_output=True, text=True, check=True)
            print(f'Service: {subdir.dirpath}\nDown:')
            print(f'STDOUT:\n{down.stdout}')
            print(f'----------------------------\nSTDERR:\n{pull.stderr}\n\n==========================================\n\n')
    else:
        os.chdir(os.path.join(config.DOCKER_ROOT_DIR, name))
        down = subprocess.run(["docker-compose", "down"], capture_output=True, text=True, check=True)
        print(f'STDOUT:\n{down.stdout}')
        print(f'----------------------------\nSTDERR:\n{pull.stderr}')



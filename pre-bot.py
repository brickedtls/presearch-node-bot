# add your Presearch registration KEY here:
registration_key = ""

# -> Import modules
import os
print(f"Initializing...")
print()
os.system("sudo pip3 install colorama")
os.system("sudo pip3 install docker")
print()
print(f"Ok.")
print()
from colorama import init as colorama_init
colorama_init()
import time
import random
import docker

container_name = "presearch-node"
run_timer = 300
run_timer_minutes = run_timer / 60

class clr:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

# -> Random generator to create a cool dash
dashes = "--------------------------"
lenght_img = 4
act_lenght = 0
spacing = "             "
start_img = []
pre_don_address = "0x4A3a3CF1850605a2F42A3C100e67E90d90024BaA"
# -> random symbol
while lenght_img > act_lenght:
    random_gen = random.randint(1,3)

    if random_gen == 1:
        symbol = "#"
    if random_gen == 2:
        symbol = "+"
    if random_gen == 3:
        symbol = "X"
    
    start_img.append(symbol)
    act_lenght = act_lenght + 1

# -> random spacing
act_lenght = 0
start_img_spacing = []
while lenght_img > act_lenght:
    random_gen = random.randint(1,3)

    if random_gen == 1:
        spacing = "      "
    if random_gen == 2:
        spacing = "                               "
    if random_gen == 3:
        spacing = "                "
    
    start_img_spacing.append(spacing)
    act_lenght = act_lenght + 1

print(clr.yellow + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print()
print()
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print()
print()
print(f"{clr.cyan}Script made by {clr.yellow}BrickedTLS{clr.cyan} to simplify Node Operations    ")
print(f"Github: {clr.endc}https://github.com/brickedtls")
print()
print(f"{clr.cyan}Donate Presearch (PRE) Address: {clr.green}{pre_don_address}{clr.endc}")
print()
print()
print(f"{clr.yellow}")
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print()
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)] + start_img_spacing[random.randint(1,3)] + start_img[random.randint(1,3)])
print(f"{clr.endc}")

def bot():
    # define docker env
    client = docker.from_env()

    # get connection status of Node
    info = client.containers.get(container_name)
    info = info.logs(tail = 1)

    # check if there's an error (will print an ERROR if the node disconnects, or if there's any other error occuring.)
    error = str(info).find("error")
    # IF there's an error, restart the Docker Container running the node.
    if error >= 0:
        print()
        print(f"[ {clr.yellow}BOT by: BrickedTLS {clr.endc}]{clr.red} >> {clr.red}ERROR has been found, restarting the Docker container: {container_name}{clr.endc}")
        print()
        print(f"Stopping Docker container: {container_name}")
        os.system(f"docker stop presearch-node ; docker rm presearch-node ; docker stop presearch-auto-updater ; docker rm presearch-auto-updater ; docker run -d --name presearch-auto-updater --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock presearch/auto-updater --cleanup --interval 900 presearch-auto-updater presearch-node ; docker pull presearch/node ; docker run -dt --name presearch-node --restart=unless-stopped -v presearch-node-storage:/app/node -e REGISTRATION_CODE={registration_key} presearch/node")
        print()
        timer = run_timer_minutes + 2.5
        print(f"[ {clr.yellow}BOT by: BrickedTLS {clr.endc}]{clr.green} >> {clr.endc}Node has been restarted. Waiting {timer} minutes before checking again.{clr.endc}")
        time.sleep(150)
    else:
        print()
        print(f"[ {clr.yellow}BOT by: BrickedTLS {clr.endc}]{clr.green} >> {clr.endc}ok, everything seems fine! Waiting {run_timer_minutes} minutes until next check.")
        print()

while True == True:
    bot()
    time.sleep(run_timer)

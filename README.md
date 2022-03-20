# presearch-node-bot
Simple Python program to restart the Presearch-node upon any error or disconnection within the node.

It has to run on the same machine as the Presearch-node!

## Installation instructions:
1. Download the Python script.
2. Edit the script and add your Presearch registration key at the beginning of the script: "nano pre-bot.py"
3. Make sure you've got screen, otherwise install it: "sudo apt-get install screen -y"
4. Create a new screen session: "sudo screen -mS "pre-bot"
5. While in the new screen session, do: "sudo python3 pre-bot.py" (has to be ran as su to be able to handle docker & install dependencies).
6. DONE! You can exit the screen session by Holding CTRL + pressing A and D button. You can always go back to the screen session with: "sudo screen -r"

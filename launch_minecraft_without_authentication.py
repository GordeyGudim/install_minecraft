
import subprocess
import json
with open('count_data.json', 'r') as users_file:
    dict_users = json.load(users_file)
def update_count(entered_login):
    dict_users[entered_login]['count']+=1
    with open('count_data.json', 'w') as users_file:
        json.dump(dict_users, users_file, indent = 4)
    return dict_users[entered_login]['count']
def launch_minecraft():
    count_signIn = update_count('user')
    users_answer = input(f'You play {count_signIn} time! Press "ok" to continue: ')
    if users_answer == 'ok':          
        subprocess.Popen('cd ~/Documents/;cd Minecraft; ./Minecraft.sh', shell = True)
        subprocess.run('exit', shell=True)
launch_minecraft()





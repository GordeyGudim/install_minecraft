import subprocess
import os
subprocess.run('sudo pacman -Syu;sudo pacman -S jdk-openjdk', shell=True)
f = open('Minecraft.sh', 'w')
f.write('#! /bin/sh\njava -jar TLauncher-2.86.jar')
subprocess.Popen('chmod +x Minecraft.sh; ./Minecraft.sh', shell = True)





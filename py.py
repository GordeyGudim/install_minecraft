import subprocess
import os
subprocess.Popen('sudo pacman -Syu;sudo pacman -S jdk-openjdk')
f = open('Minecraft.sh', 'w')
f.write('#! /bin/sh\njava -jar TLauncher-2.86.jar')
subprocess.Popen('chmod +x Minecraft.sh; ./Minecraft.sh')





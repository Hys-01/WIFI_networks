'''
Description: 
    Using data gathered from subprocess.check_output, decode the output and stylises it 

RequiremetsL 
    re and colors_custom modules 

'''

# import modules
import re
from colors_custom import *


# customization of output, coloring
def colorize(lines): 

    for i, line in enumerate(lines): 
        # if first line, colour it red and bold the interface name
        if i ==1: 
            titlesplit = lines[i].split(':')
            lines[i] = RED + titlesplit[0] + ":" + BOLD_RED + titlesplit[1] + PLAIN
            
        # if line describing number of networks found, change the number to bold green 
        if line.startswith('There'): 
            # use regex \d to match digits from 0-9
            number = re.findall(r'\d+', line)

            lines[i] = re.sub(r'\d+', BOLD_GREEN+str(number[0])+PLAIN, line)

        # if line listing a network, cyan bold the network name
        if line.startswith('SSID'): 
            SSIDsplit = line.split(':') 
            if len(SSIDsplit[1]) < 2: 
                lines[i] = SSIDsplit[0] + ':' + BOLD_PURPLE + 'HIDDEN NETWORK' + BOLD_CYAN + SSIDsplit[1] + PLAIN
                continue
            lines[i] = SSIDsplit[0] + ':' + BOLD_CYAN + SSIDsplit[1] + PLAIN

        if 'Authentication' in line:
            # edit the encryption font
            auth_split = line.split(':')
            if auth_split[1] != " Open":
                lines[i] = auth_split[0] + ':' + BOLD_YELLOW + auth_split[1] + PLAIN


        

    # after coloring is finished, join the list of strings/lines back into legible format 
    final = '\n'.join(lines)
    return final


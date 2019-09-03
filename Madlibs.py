from collections import defaultdict # Imports the ability to create writable instance variables
from colorama import init, Fore, Back, Style # Imports the ability to color text and characters
import random
import re
import sys

init()

#  Credit to http://patorjk.com/software/taag/

scriptTitle = """
_______________________________________________________________________________________________________________________________ 
       /\_\/\_\ _           / /\              /\ \               _\ \            /\ \             / /\             / /\      
      / / / / //\_\        / /  \            /  \ \____         /\__ \           \ \ \           / /  \           / /  \     
     /\ \/ \ \/ / /       / / /\ \          / /\ \_____\       / /_ \_\          /\ \_\         / / /\ \         / / /\ \__  
    /  \____\__/ /       / / /\ \ \        / / /\/___  /      / / /\/_/         / /\/_/        / / /\ \ \       / / /\ \___\ 
   / /\/________/       / / /  \ \ \      / / /   / / /      / / /             / / /          / / /\ \_\ \      \ \ \ \/___/ 
  / / /\/_// / /       / / /___/ /\ \    / / /   / / /      / / /             / / /          / / /\ \ \___\      \ \ \       
 / / /    / / /       / / /_____/ /\ \  / / /   / / /      / / / ____        / / /          / / /  \ \ \__/  _    \ \ \      
/ / /    / / /       / /_________/\ \ \ \ \ \__/ / /      / /_/_/ ___/\  ___/ / /__        / / /____\_\ \   /_/\__/ / /      
\/_/    / / /       / / /_       __\ \_\ \ \___\/ /      /_______/\__\/ /\__\/_/___\      / / /__________\  \ \/___/ /       
        \/_/        \_\___\     /____/_/  \/_____/       \_______\/     \/_________/      \/_____________/   \_____\/  
By: Ninjer27                                                                                         Art: @http://patorjk.com/       
_______________________________________________________________________________________________________________________________                                                      
"""

print(Fore.BLUE + scriptTitle + Back.RESET + Fore.RESET)





# Dictionary contains predetermined words that will be selected at random incase the user doesn't input anything
noInput = {
    'adjList': ['Amazing', 'FABULOUSE', 'GORGEOUSE', 'GOD SEND'],
    'nounList': ['robin', 'flea', 'dog', 'fly'],
    'verbList': ['mock', 'hate', 'laugh', 'teas'],
    'nameList': ['Jason', 'Tod', 'Danny', 'Ninja'],
    'locationList': ['basement', 'Africa', 'Zimbabewa', 'Makeschool']
 }


    
    
# Collection of all User Input data collected and pulled into a list

userAdj = input('Give me a Adjective: ')
if not userAdj.strip():
    userAdj = random.choice(noInput.get('adjList'))

userNoun = input('Give me a noun(Prefered Animal): ')
if not userNoun.strip():
    userNoun = random.choice(noInput.get('nounList'))
        
userVerb = input('Give me a verb: ')
if not userVerb.strip():
    userVerb = random.choice(noInput.get('verbList'))
    
serLocation = input('Give me a location: ')
if not userLocation.strip():
    userLocation = random.choice(noInput.get('locationList'))

userName = input('Gime me someone\'s name: ')
if not userName.strip():
    userName = random.choice(noInput.get('nameList'))

    
print(
    f'greg looked quite {userAdj.lower()} on a good day. He hated {userNoun.lower()}s because they {userVerb.lower()}ed him for the way he looked. ' +
    f'In till he met {userName.title()}\'s {userNoun.lower()} his one true love in life in {userLocation.lower()}. {userName.title()} was honestly quite disgusted when he heard about this.')


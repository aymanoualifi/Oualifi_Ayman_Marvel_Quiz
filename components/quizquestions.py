database = [

    {"name":"iron man", "human":True, "woman":False, "big":False, "mask":False},
    
    {"name":"black widow", "human":True, "woman":True, "big":False, "mask":False },

    {"name":"hulk", "human":False, "woman":False, "big":True, "mask":False},

    {"name":"spider man", "human":True, "woman":False, "big":False, "mask":True}

    ]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("your character is "+database[0]["name"])
        quit()



ans = input("Is your character human? [Y/N]")
take_chance(ans, "human")

ans = input("Is your character a woman? [Y/N]")
take_chance(ans, "woman")

ans = input("Is your character big? [Y/N]")
take_chance(ans, "big")

ans = input("Does your character wear a mask? [Y/N]")
take_chance(ans, "mask")

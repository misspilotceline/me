"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print(
        f"""
    Be careful that your relative paths are
    relative to where you think they are
    LOCAL: {LOCAL}
    CWD: "CWD
    """
    )


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(json_data)

    results = data.get("results",[])

    if results:
        user_info = results[0]
        name_info = user_info.get("name",{})
        location_info = user_info.get("location",{})
        id_value = int(user_info.get("id",{}).get("value","0"))
        post_code = int(location_info.get("postcode","0"))
        last_name = name_info.get("last","")
        pass_word= (user_info.get("login",{}).get("password",""))

        postcode_plus_id = post_code + id_value

        return {"lastName":last_name,"password":pass_word,"postcodePlusID":postcode_plus_id}
    else:
      
        return {"lastName": None, "password": None, "postcodePlusID": None}


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20
    The generator takes a single argument, length (`wordlength`) of the word.
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &wordlength=
    """
    base_url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
    pyramid = []
    for i in range(3,20,2):
        url = f"{base_url}{i}"
        response = requests.get(url)
        word = response.text.strip()
        pyramid.append(word)

    for i in range(20,2,-2):
        url = f"{base_url}{i}"
        response = requests.get(url)
        word = response.text.strip()
        pyramid.append(word)



    return pyramid

def pokedex(low, high):
    """Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """

    tallest_pokemon_height = 0
    tallest_pokemon_weight = 0
    tallest_pokemon_name = ""
    pokemon_bucket=[]
    for id in range (low, high + 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            height = the_json.get("height","0")
            weight = the_json.get("weight","0")
            if height > tallest_pokemon_height:
                tallest_pokemon_height = height
                tallest_pokemon_name = the_json.get("name","")
                tallest_pokemon_weight = weight


    return {"name": tallest_pokemon_name, "weight": tallest_pokemon_weight, "height": tallest_pokemon_height}


import os
def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the Set4 directory.

    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.

    NOTE: this function doesn't return anything. It has the _side effect_ of modifying the file system
    """
    input_file_path = "Trispokedovetiles(laser).gcode"
    output_directory = "set4"
    output_file_path = os.path.join(output_directory,"lasers.pew")

    command_count = 0
    mode = "r"
    writemode = "w"
    try:
        with open(input_file_path,mode,encoding="utf-8") as file:
            contents= json.load(file)
            for line in contents:
                if "M10 P1" in line:
                 command_count+= 1

    except FileNotFoundError:
        print("G-code file not found")
        return
    
    os.makedirs(output_directory,exist_ok=True)

    with open(output_file_path,writemode,encoding="utf-8") as file:
        file.write(str(command_count))
        file.close()
    


    pass


if __name__ == "__main__":
    print(get_some_details())

    wp = wordy_pyramid()
    [print(f"{word} {len(word)}") for word in wp]

    print(pokedex(low=3, high=7))

    diarist()

    in_root = os.path.isfile("lasers.pew")
    in_set4 = os.path.isfile("set4/lasers.pew")
    if not in_set4 and not in_root:
        print("diarist did not create lasers.pew")
    elif not in_set4 and in_root:
        print(
            "diarist did create lasers.pew, but in the me folder, it should be in the set4 folder"
        )
    elif in_set4:
        print("lasers.pew is in the right place")

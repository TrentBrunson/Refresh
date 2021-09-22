# read in states file and split into 2 separate files
# list1 for state names starting with a consonant
# list2 for state names starting with a vowel

from os import write


def read_file_to_list():
    with open("SomeStates.txt", "r") as infile:
        states = [line.rstrip() for line in infile]
        return states

def display_header():
    # tell user what the program does
    print(
        f"Creating two list of US state names.\n"
        f"One list of states having names starting with a vowel.\n"
        f"Second list of states having names starting with a consonant\n"
    )

def split_states(states):
    vowels = "aeiou"
    vowelStates = []
    consonantStates = []
    for state in states:
        if state[0].lower in vowels:
            vowelStates.append(state)
        else:
            consonantStates.append(state)
    return vowelStates, consonantStates

def write_state_file(vStates, cStates):
    with open("vowelStates.txt", "w") as outfile:
        vStates.sort()
        for state in vStates:
            outfile.write(f"{state}\n")

    with open("consonantStates.txt", "w") as outfile:
        cStates.sort()
        for state in cStates:
            outfile.write(f"{state}\n")

def main():
    display_header()
    stateList = read_file_to_list()
    vStates, cStates = split_states(stateList)
    write_state_file(vStates, cStates)

if __name__ == "__main__":
    main()


import json, random

CBT_FILE = '/home/cbt/challenging_thoughts.json'

def main():
    pref_thought = "I am bad"
    name = "Alu"
    done_bias = []
    with open(CBT_FILE) as f:
        cbt = json.load(f)
        bias_pick = random.randint(1, len(cbt))
        node = bias_pick - 1
        print("Consider your thought: ", pref_thought)
        print(cbt[node]['intro'])
        bias_y_n = input("Y/N/Maybe: ")
        while bias_y_n.lower() == 'n' and len(done_bias)!=len(cbt):
            done_bias.append(node)
            print("Thats' great "+str(name)+"!")
            bias_pick = random.randint(1,len(cbt))
            node = bias_pick-1
            while node in done_bias and len(done_bias)!=len(cbt):
                bias_pick = random.randint(1,len(cbt))
                node = bias_pick - 1
            if len(done_bias)==len(cbt):
                print("Let's move to another thought "+str(name)+"!")
                return 1
            else:
                print(cbt[node]['intro'])
                bias_y_n = input("Y/N/Maybe: ")
        print(cbt[node]['affirmation'])
        enter = input("Do you want to know what this bias is?\n")
        print("Well "+str(name)+", this distortion is called "+ str(cbt[node]['name']))
        enter = input("")
        enter = input(cbt[node]['opening'])
        enter = input(cbt[node]['example'])
        print("Do you want to learn more about "+str(cbt[node]['name']))
        more_y_n = input('(Y/N) ?: ')
        if more_y_n.lower()=='y':
            print(cbt[node]['explanation'])
        print('\n')
        enter= input("Let's try to work on it with an exercise "+str(name))
        enter = input(cbt[node]['exercise'])
        

if __name__ == '__main__':
    main()

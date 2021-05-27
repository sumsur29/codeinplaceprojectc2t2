'''
This program is inspired by CBT bots around the world,  such as Woebot and Wysa, 
and modified to deal with common issues that people stuck in the lockdown or 
dealing with covid anxiety might face.
In no way a perfect bot, but a good first step to help the world!

'''
import csv, json, datetime, random

ANALYTICS_FILE = '/home/data/analytics.csv'
CBT_FILE = '/home/cbt/challenging_thoughts.json'

def main():
    name = cbt_intro_get_name()                                     #takes user's name in a friendly and introductory way
    feeling_scale_pre = feeling_scale_beginning(name)               #ask user input of the item she needs help with
    three_thoughts = get_thoughts(feeling_scale_pre,name)           #collects the train of thoughts in three thoughts list
    pref_thought = cognitive_distortion(three_thoughts, name)       #ask the user to pick the thought she wants to work on
    intro_to_CD(three_thoughts, pref_thought, name)                 #gives intro to cognitive distortion
    move = bias_check(three_thoughts[pref_thought], name)           #where the real magic happens, returns whether user wants to work on new thought or exit
    while move:                                                     #moves to the next thought and redoes the process of bias check
        pref_thought = cognitive_distortion(three_thoughts, name)
        move = bias_check(three_thoughts[pref_thought], name)
    print("\n\nGreat work today "+str(name)+"!\nBefore you go, I have something to ask\n")
    feeling_scale_post = feeling_scale_end(feeling_scale_pre, name) #collects user feedback on how effective it was
    write_in_file(feeling_scale_pre,feeling_scale_post)             #collects data to get its effectiveness, does not collect any personal data
    show_analysis(name)                                             #analyzes realtime data from the file and shows its effectiveness



#Give's intro of CBT and CovBot and returns the name of the user
def cbt_intro_get_name():
    '''
    This function gives an intro to CBT and asks user's name 
    in an interactive and fun way
    '''
    print("\nHi! I'm C2T2 🤹 - short for 'Computer for Challenging Train of Thought'!\nI'm one of the many CBT bots.")
    cbt_know = input("\nDo you know what is CBT? (y/n) \n")
    if cbt_know.lower() == 'y':
        enter= input("Wow, that's great! you are awesome!! 😎\n")
    else:
        print("\nCBT is short for Cognitive Behavioural therapy.")
        print("Mostly, it's a way to challenge your thinking. 🧐 ")
        enter = input('')
        enter = input("You can learn more about it here: \nhttps://en.wikipedia.org/wiki/Cognitive_behavioral_therapy \n")
    name = input('\nGreat, now what should I call you? \n')
    while name =='':
        print("Uh oh! You missed it 🙇")
        name = input('\nGreat, now what should I call you? \n')
    print("\nThat's a nice name, "+str(name)+"!")
    enter = input('')
    print("Let's start challenging some thoughts,", name )
    enter = input("\nPress Enter to 'enter' my world of positivity 🙌\n")
    return name


def feeling_scale_beginning(name):
    '''
    This function ask the user what she is feeling
    and the scale of the feeling
    returns the feeling scale pre CBT as a list
    '''
    feeling_scale = []
    feelings = {1:"Sad", 2:"Hopeless", 3:"Anxious", 4:"Frustrated", 5:"Worried"}
    print('')
    print(str(name)+", let's start with understanding how are you feeling currently!!🙇")
    for key in feelings:
        print(str(key)+".", feelings[key])
    print(str(len(feelings)+1)+". Other",)
    feeling = input("Enter the number from the above list that explains your feeling: ")
    while feeling =='':
        print("Uh oh! You missed it 🙇")
        feeling = input("Enter the number from the above list that explains your feeling: ")
    feeling = int(feeling)
    while feeling <1 or feeling >(len(feelings)+1):
        print("Uh oh! Invalid entry 🙇")
        feeling = (input("Enter the number from the above list that explains your feeling: \n"))
    if feeling ==6:
        feel = input("\nTell me, what are you feeling? ")
        print('')
        print(str(name)+", Thanks for sharing that you are feeling", feel)
        enter = input('')
    else:
        print('')
        print(str(name)+", I'm sorry to hear that you are feeling", feelings[feeling])
        enter = input('')
    scale = input("\nOn a scale of 1 to 10, how would you rate your feeling. 10 being the most: \n")
    while scale =='':
        print("Uh oh! You missed it 🙇")
        scale = input("\nOn a scale of 1 to 10, how would you rate your feeling. 10 being the most: \n")
    scale = int(scale)
    while scale <1 or scale>10:
        print("Uh oh! Invalid entry 🙇")
        scale = int(input("\nOn a scale of 1 to 10, how would you rate your feeling. 10 being the most: \n"))
    print("\nGot it!\n")
    if feeling == 6:
        feeling_scale = [feel, scale]
    else:
        feeling_scale = [feelings[feeling], scale]
    return feeling_scale


def get_thoughts(feeling_scale_pre,name):
    '''
    This fuction collects the train of thought
    For ease we are collecting three thoughts form the user
    It returns the three thoughts as a list
    '''
    three_thoughts = []
    print(str(name)+", I'm glad to help you challenge the thoughts that make you feel", feeling_scale_pre[0])
    print("\nI want you to think about the time when you felt", feeling_scale_pre[0], "most intesely! 🙇")
    enter = input("Got it?\n")
    enter = input("\nNext, try listening to your thoughts in this time\nImagine that these thoughts have a voice.🗣\n")
    print("Can you listen to this voice?🎧")
    three_thoughts_1 = input("\nOk, write one of these thoughts here, keep them short 📝...\n")
    while three_thoughts_1 =='':
        print("Uh oh! You missed it 🙇")
        three_thoughts_1 = input("\nOk, write one of these thoughts here, keep them short 📝...\n")
    three_thoughts.append(three_thoughts_1)

    three_thoughts_2 = input("\n...and now another one..📝 \n")
    while three_thoughts_2 =='':
        print("Uh oh! You missed it 🙇")
        three_thoughts_2 = input("\n...and now another one..📝 \n")
    three_thoughts.append(three_thoughts_2)

    three_thoughts_3= input("\nAnd just one more..📝 \n")
    while three_thoughts_3=='':
        print("Uh oh! You missed it 🙇")
        three_thoughts_3= input("\nAnd just one more..📝 \n")
    three_thoughts.append(three_thoughts_3)

    print("\nThat must be hard. Thanks for sharing these thoughts with me "+str(name)+" 🙏🙏")
    enter = input("\nAre you ready to challenge these thoughts with me?💪💪\n")
    return three_thoughts


def cognitive_distortion(three_thoughts, name):
    '''
    This function uses these three thoughts and asks user
    which thought she wants to work on
    It returns the index of that thought in the three thought list
    '''
    print("\nWhich one of these three thoughts would you like to work on now?")
    for i in range(len(three_thoughts)):
        print(str(i+1)+".", three_thoughts[i])
    pref = input("Enter the number of selected thought: \n")
    while pref =='':
        print("Uh oh! You missed it 🙇")
        pref = input("Enter the number of selected thought: \n")
    pref = int(pref)
    while pref < 1 or pref > 3:
        print("Uh oh! Invalid entry 🙇")
        pref = int(input("Enter the number of selected thought: "))
    pref -= 1
    pref_thought = three_thoughts[pref]
    print('')
    print("Great!", name, "let's work on '"+str(pref_thought)+"'.")
    return pref

def intro_to_CD(three_thoughts, pref, name):
    '''
    This function gives the user an intro to Cognitive Distortion
    '''
    pref_thought = three_thoughts[pref]
    print("\nDo you know '"+str(pref_thought)+"' might have Cognitive Distortion in it?")
    y_n = input("\nWait⌚! before we go there, "+str(name)+" do you know what is Cognitive Distortion?(y/n) \n")
    if y_n.lower() == 'y':
        print("\nThat's great "+str(name)+"!")
    else:
        print("\nWell "+ str(name)+" Cognitive Distortions are thought patterns\nthat cause people to view reality in inaccurate - usually negative — ways.🙅‍")
        enter = input('')
        enter = input("\nIn short, they’re habitual errors in thinking🤦‍.\nWhen you’re experiencing a cognitive distortion,\nthe way you interpret events is usually negatively biased.🤷\n")
    enter = input("\nLets work on this thought to see if it has any cognitive distortions? \n")


def bias_check(pref_thought, name):
    '''
    This function picks the preferred thought and applies CBT
    It loads the json file (Challengin thoughts) where 8 biases are listed as a list of dictionaries
    This function limits the bias check to three/thought as not to overwhelm the user
    It also gives user an option to exit
    '''
    done_bias = []
    worked_on_bias = 0
    with open(CBT_FILE) as f:
        cbt = json.load(f)
        node = get_new_node(done_bias)
        print("Consider your thought: ", pref_thought)
        while worked_on_bias<3:
            if len(done_bias)==len(cbt):
                    print("\nI think we have covered it all.\nLet's move to another thought "+str(name)+"!")
                    return 1
            else:
                print(cbt[node]['intro'])
                bias_y_n = input("Y/N/Maybe: ")
                done_bias.append(node)
                while bias_y_n.lower() == 'n' and len(done_bias)!=len(cbt):
                    print("\nThats' great "+str(name)+"! Let's check if it has other bias.")
                    node = get_new_node(done_bias)
                    if node == (len(cbt)+1):
                        return 1
                    else:
                        print(cbt[node]['intro'])
                        bias_y_n = input("Y/N/Maybe: ")
                        done_bias.append(node)
                thought_bias_exit = run_bias_cycle(node,name)
                worked_on_bias += 1
                if thought_bias_exit == 1:
                    return 1
                elif thought_bias_exit == 0:
                    return 0
                elif len(done_bias)==len(cbt):
                    print("\nI think we have covered it all.\nLet's move to another thought "+str(name)+"!")
                    return 1
                else:
                    node = get_new_node(done_bias)



def get_new_node(done_bias):
    '''
    This function returns the index for the bias from the json file
    It also checks if this bias has already been worked at on this thought
    and if all the biases are covered
    '''
    with open(CBT_FILE) as f:
        cbt = json.load(f)
        bias_pick = random.randint(1,len(cbt))
        node = bias_pick-1
        while node in done_bias and len(done_bias)!=len(cbt):
            bias_pick = random.randint(1,len(cbt))
            node = bias_pick - 1
        if len(done_bias)==len(cbt):
            print("\nI think we have covered it all.\nLet's move to another thought "+str(name)+"!")
            return (len(cbt)+1) 
        else:
            return node

def run_bias_cycle(node,name):
    '''
    This function runs the stage of the bias cycle
    and returns if user wants to work on another thought
    or exit or check other biases
    '''
    with open(CBT_FILE) as f:
        cbt = json.load(f)
        print(cbt[node]['affirmation'])
        enter = input("Do you want to know what this bias is?\n")
        print(str(name)+", this distortion is called '"+ str(cbt[node]['name'])+"'")
        enter = input("")
        enter = input(cbt[node]['opening'])
        enter = input(cbt[node]['example'])
        print("\nDo you want to learn more about "+str(cbt[node]['name']))
        more_y_n = input('(Y/N) ?: ')
        if more_y_n.lower()=='y':
            print(cbt[node]['explanation'])
        print('')
        enter= input("Let's try to work on it with an exercise "+str(name)+"\n")
        enter = input(cbt[node]['exercise'])
        print('')
        rewrite = input("Let's take a stab at this exercise 📝...\n")
        print("That's great work "+str(name))
        helped = input("So, how did it go? Did it help (y/n):\n")
        if helped.lower()=='n':
            print("\nNo worries, "+str(name)+" you tried🤗. That's what matters!")
        else:
            print("\nYayy!!🤩🎊🥳🎉") 
        thought_bias = input("\nGreat work "+str(name)+", do you want to see if this thought has any other bias? (y/n): \n")
        if thought_bias == 'y':
            return 2
        else:
            thought_bias = input("Would you want to \n1. Work on the next thought or \n2. Exit the program \nEnter the number from the menu: " )
            if int(thought_bias) == 1:
                return 1
            else:
                return 0


def feeling_scale_end(feeling_scale_pre, name):
    '''
    This function collects the feedback after the process is complete
    '''
    feeling_scale_post = []
    enter = input("\nOk, now it is time to check my effectiveness...🤞🤞\n")
    print(str(name)+", you said you are feeling "+str(feeling_scale_pre[0])+", before we begin, at a scale of "+str(feeling_scale_pre[1]))
    enter = input("Correct?\n")
    post_scale = input("\nAfter challenging your thoughts, how "+str(feeling_scale_pre[0])+" are you now.\nOn a scale of 1 to 10, 10 being the most: ")
    while post_scale =='':
        print("Uh oh! You missed it 🙇")
        post_scale = input("How "+str(feeling_scale_pre[0])+" are you now.\nOn a scale of 1 to 10, 10 being the most: ")
    post_scale = int(post_scale)
    feeling_scale_post = [feeling_scale_pre[0], post_scale]
    if post_scale<int(feeling_scale_pre[1]):
        print("\nGlad I could be of help to you, "+str(name)+"!! 🥰🥰\n")
    else:
        print("\nI'm sorry "+str(name)+" 😞.\nI will try to rewire my circuits and help you next time. 🤖\n")
    return feeling_scale_post

def write_in_file(feeling_scale_pre,feeling_scale_post):
    '''
    This function writes the feedback: Timestamp, Feeling, Feeling scale and Feeling scale post
    It does not capture any user data
    '''
    ct = datetime.datetime.now() # get timestamp
    with open(ANALYTICS_FILE,'a') as f:
        writer = csv.writer(f)
        writer.writerows([
            [ct,feeling_scale_pre[0],feeling_scale_pre[1], feeling_scale_post[1]]
        ])

def show_analysis(name):
    '''
    This function calculates the effectiveness of C2T2 and presents it to the user
    '''
    line_count = 0
    sum_pre = 0
    sum_post = 0
    with open(ANALYTICS_FILE) as f:
        reader = csv.DictReader(f)
        for line in reader:
            line_count += 1
            sum_pre += float(line['pre_score'])
            sum_post += float(line['post_score'])
        average_pre = sum_pre/line_count
        average_post = sum_post/line_count
        effectiveness = -1*((average_post-average_pre)/average_pre)
        effectiveness *= 100
        enter = input("Would you want to know something interesting about how I am helping?")
        print("\nDo you know "+str(name)+",I have helped "+str(line_count)+" people till today 🥳.\nAnd on an average, reduced negative feelings by "+str(int(effectiveness))+"%.🎊 🎉")
        enter= input("\nPlease do share it with your friends if I was able to help you,\nmaybe I can help them too 😍💞.\n")
        print("\nHave a nice day!\n")


if __name__ == '__main__':
    main()

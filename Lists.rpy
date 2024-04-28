#Lists
#This script contains the list of comments and chats that can appear in the stream


init python:
    class ChatEntry():
        #This function defines a new class of objects called ChatEntry.
        #ChatEntry objects have four potential attributes that can be defined.
        def __init__(self, click, prompt, tag, target = "", ): #"click" has to go earlier because of the kind of argument it is.
            #self identifies the object as itself, allowing the object to reference its own attributes
            self.click = click #click is a boolean that determines if a comment is clickable or not. True is clickable, False is not.
            self.prompt = prompt #prompt is the string that will appear when the chat is shown
            self.tag = tag #tag is a numeric identifier that will allow us to "batch" comments together.
                            #Then we can do things like remove every object in the comments list with a tag == 2.
            self.target = target #target indicates a label that a clickable object will call.
    
init python:
    def AddToChats():
    #This function will add a random comment from the list "comments" to the "chats" list
    #This "chats" list will be displayed on the stream UI
    #To reference where this is appearing, go to the Screens script and check the streamChat screen on line 83
        global comment_list
        global chats_list

        renpy.random.shuffle(comments_list) #This shuffles the comments_list so they appear in a random order
        if len(chats_list) >= 4: #Checks the "length" of the chats_list - how many objects are currently stored in it.
        #If the number of items in Chats gets to a certain threshold, we need to remove the earliest object to make room for new ones.
            chats_list.remove(chats_list[0]) #removes the earliest object in the chats list.
            chats_list.append(comments_list[0]) #adds the first object from the comments list (after shuffling) to the chats_list
            #comments_list.remove(comments_list[0]) -- This line would remove the top of the comments list that was just added to chats (currently disabled for testing)
        else:
            chats_list.append(comments_list[0]) #If the chats list is not at the threshold yet, we don't need to delete any objects
        return

    def addStoryBeat(): #This function allows us to add a specific chat to the stream
    #Priror to implementing this function, you must set the variable "newChat" equal to the comment you would like to be added
    #Ex: newChat = comment5
        global chats_list
        global comments_list
        global newChat
        if len(chats_list) >= 4:
            chats_list.remove(chats_list[0])
            chats_list.append(newChat)
        else:
            chats_list.append(newChat)
        return
    
    #The following function is an example for how we can use a ChatEntry's .tag attribute to modify the list.
    #This function will delete all objects in the "comments" list that have a tag of 1.
    def removeChatsv1():
        global comments_list
        global chats_list
        for c in comments_list:
            if c.tag == 1:
                comments_list.remove(c)
        return

#The following five lines define five ChatEntry objects that can be added and rearranged amongst the "comments" and "chats" lists
#Note how many of these do not have a "target" attribute. Only clickable ChatEntries require "targets"
default comment1 = ChatEntry( False, "Hi! I'm the first chat!", 1 )
default comment2 = ChatEntry( False, "Sup, I'm second in chat", 2 )
default comment3 = ChatEntry( True, "Help, I'm the third chat and I'm stuck in here" , 1, "comment3Choice")
default comment4 = ChatEntry( False, "This is the legendary 4th chat", 1 )
default comment5 = ChatEntry( False, "And I'm the godlike 5th chat", 1)


default comments_list = [comment1, comment2, comment3] #This list contains the objects that will be shuffled and chosen from to add to "chats"
#Objects will be taken from this list and added to "chats_list"

default chats_list = [ ] #This is the list that displays on the Stream UI

#############################################################################
#Below this point contains the labels that are called by clickable comments:
label comment3Choice():
    $ macroChoice = True #If this is a decision happening in the macrogame, change this boolean so that the choice screen will appear in its default state
    $ comment3.click = False #makes the chat unclickable once it has been clicked.
    #This should reference the specific ChatEntry object that directs here through its target attribute.
    # eg. if comment64 directs to a certain label, add $ comment64.click = False, to turn it off
    $ narrator = reg_narrator # you also need to manually change the narrator so that the text appears outside the micro game
    menu:
        "Make a Choice"
        "Who let you out of your hole?":
            "A bit rude. Morality -1."
        "Why is my computer sentient?":
            "Recognizing agency outside of humans. Morality +1."
    "See how the menu appeared in the center of the screen?"
    $ macroChoice = False #set macroChoice back to false at the end of this interaction so that the 
    #choice screen will appear appropriately for micro-game choices.
    $ narrator = alt_narrator #And you will need to manually revert the narrator back to the in-game narrator to shift their textbox properly.
    return










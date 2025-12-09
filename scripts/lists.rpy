#This script contains the list of comments and chats that can appear in the stream

init python:
    class ChatEntry():
        #This function defines a new class of objects called ChatEntry.
        #ChatEntry objects have four potential attributes that can be defined.
        def __init__(self, click, prompt, tag, colour = "", target = "", ): #"click" has to go earlier because of the kind of argument it is.
            #self identifies the object as itself, allowing the object to reference its own attributes
            self.click = click #click is a boolean that determines if a comment is clickable or not. True is clickable, False is not.
            self.prompt = prompt #prompt is the string that will appear when the chat is shown
            self.tag = tag #tag is a numeric identifier that will allow us to "batch" comments together.
                            #Then we can do things like remove every object in the comments list with a tag == 2.
            self.colour = colour #added an attribute that will allow us to change the color of the text that appears.
                                #this probably won't be necessary, but wanted to play around with some possibilities.
                                #called it "colour" because "color" is often used by Renpy to refer to specific things and handle already determined attributes.
            self.target = target #target indicates a label that a clickable object will call.

    class bThread():
        def __init__(self, tag, target = "", image = ""):
            self.tag = tag
            self.target = target
            self.image = image

#defining useful functions
default yadj = ui.adjustment()

init python:

    def AddChatter(message):
        global chatter_list
        global yadj

        chatter_list.append(message)
        renpy.pause(0.01) #bc reasons
        yadj.change(float('inf'))
        #yadj.value = float('inf') #- Getting this to work would be ideal
        #but it's still behaving weird, so stick with yadj.change for now

        if commentPing == True:
            renpy.sound.play("audio/ReceiveText.ogg")
        else:
            pass #Is there a "Pass" syntax?
        return

    def addWriteUp(paragraph):
        global writeUp_list
        global yadj

        writeUp_list.append(paragraph)
        renpy.pause(0.01)
        yadj.change(float('inf'))
        return

    def AddRandomChatter():

        global comment_list
        global chatter_list

        renpy.random.shuffle(comments_list) #This shuffles the comments_list so they appear in a random order
        chatter_list.append(comments_list[0]) 
        comments_list.remove(comments_list[0])
        return

    def setEngagement():
        global csEngagement
        global kcEngagement
        global pdEngagement

        if csEngagement > 15:
            csEngagement = 15
        elif csEngagement < -15:
            csEngagement = -15
        else:
            pass
        
        if kcEngagement > 15:
            kcEngagement = 15
        elif kcEngagement < -15:
            kcEngagement = -15
        else:
            pass

        if pdEngagement > 15:
            pdEngagement = 15
        elif pdEngagement < -15:
            pdEngagement = -15
        else:
            pass

        return

    def setAlignment():
        global marshal
        global outlaw
        pass
        #if marshal > 20:
        #    marshal = 20
        #elif marshal < -20:
        #    marshal = -20
        #else:
        #    pass
        
        #if outlaw > 20:
        #    outlaw = 20
        #elif outlaw < -20:
        #    outlaw = -20
        #else:
        #    pass

        return

label TurnSound():
    #$ commentPing = ! commentPing #There's a one liner for this but I don't know the syntax
    #so we do it unwieldy
    if commentPing == False:
        $ commentPing = True
        $ pingText = "Sound is On"
        $ pingImage = "stream ui/soundon.png"
    elif commentPing == True:
        $ commentPing = False
        $ pingText = "Sound is Off"
        $ pingImage = "stream ui/soundoff.png"
    return

label turnDebug():
    if debugMode == False:
        $ debugMode = True
        $ debugText = "On"
    elif debugMode == True:
        $ debugMode = False
        $ debugText = "Off"
    return

    
default chatter_list = [ ] #This is the list that displays on the Stream UI
default comments_list = [ ] #This list contains the objects that will be shuffled and chosen from to add to "chats"
default blueitPages = [ ]
#Objects will be taken from this list and added to "chats_list"




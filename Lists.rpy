#Lists
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

#defining useful functions
init python:
    def AddToChatter():

        global comment_list
        global chatter_list

        renpy.random.shuffle(comments_list) #This shuffles the comments_list so they appear in a random order
        chatter_list.append(comments_list[0]) 
        comments_list.remove(comments_list[0])
        return
    
default chatter_list = [] #This is the list that displays on the Stream UI
default comments_list = [ ] #This list contains the objects that will be shuffled and chosen from to add to "chats"
#Objects will be taken from this list and added to "chats_list"

#Example Chat Entries:
default comment1 = ChatEntry( False, "{b}Squeejieboy33:{/b} Hope everyone's week is going well!", 1, "#000000ff" )
default comment2 = ChatEntry( False, "{b}topOmornin:{/b} Really dig the art style of this game", 2, "#000000ff", "comment2Choice")
default comment3 = ChatEntry( True, "{b}xKSamuraiKx:{/b} Hey [player], how's your week been?" , 1, "#000000ff", "comment3Choice")
default comment4 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} Glad to see you still streaming this game!", 1, "#000000ff", )

#comments for decision 1
default commentEngineerPD = ChatEntry (False, "{b}PickledDragons:{/b} Yo good to be back in stream!", 0, "#000000ff")
default commentPilotCS = ChatEntry (False, "{b}Coriolis:{/b} Good to see Jennica speaking some sense!", 0, "#000000ff")
default commentNothingKK = ChatEntry (False, "{b}KitKat:{/b} Playing, neutral captain, I respect that", 0, "#000000ff")
default commentNothingPD = ChatEntry (False, "{b}PickledDragons:{/b} Yessss! OMG I want the Ama drama so bad!", 0, "#000000ff")
default commentNothingKK2 = ChatEntry (False, "{b}KitKat:{/b} Turn the big bad with love? Dig it!", 0, "#000000ff")
default kkAsksRomance = ChatEntry (True, "{b}KitKat:{/b} Hey [player]! Who are you thinking of romancing on this playthrough?", 0, "#000000ff", target = "streamAsksRomance")
default csJennica = ChatEntry(False, "{b}Coriolis:{/b} Jennica ftw!", 0, "#000000ff")
default kkTeresa = ChatEntry(False, "{b}Teresa:{/b} Crazy engineer ftw!", 0, "#000000ff")

#comments for decision 2
default pdLovesChaos = ChatEntry (False, "{b}PickledDragons:{/b} chaos chaos chaos chaos", 0, "#000000ff")
default kkMac = ChatEntry (False, "{b}KitKat:{/b} Oh no Mac!", 0, "#000000ff")
#comments for outlaw decision 2
default pdOutlawD2 = ChatEntry (False, "{b}PickledDragons:{/b} CHAOS CHAOS CHAOS", 0, "#000000ff")
default csOutlawD2 = ChatEntry(True, "{b}Coriolis:{/b} bahahaha just like my DnD group's stealth rols", 0, "#000000ff", "CoriolisTalksDnDOutlaw")

#comments for marshal decision 2
default csMarshalD2 = ChatEntry(True, "{b}Coriolis:{/b} Jennica the top-tier support character of the DnD party", 0, "#000000ff", "CoriolisTalksDnDMarshal")
default kkMarshalD2 = ChatEntry(False, "{b}KitKat:{/b} Awww I wanted to see what Teresa had up her sleeve", 0, "#000000ff" )

#comments for CoriolisDnD talk
default csDnDvg2 = ChatEntry (False, "{b}Coriolis:{/b} nooooo hit her up again, make it happen!", 0, "#000000ff")
default csDnD2vg2 = ChatEntry (False, "{b}Coriolis:{/b} same! I go cleric a lot of the time, though I typically spec it to be effective in combat too", 0, "#000000ff" )
default kkDnDvg2 = ChatEntry (True, "{b}KitKat:{/b} What class do you think [player] would run?", 0, "#000000ff", "DnDClassTalk")
default kkDnDvg2play = ChatEntry (True, "{b}KitKat:{/b} What class do you think [player] runs?", 0, "#000000ff", "DnDClassTalkplay")
default pdDnDvg2 = ChatEntry (False, "{b}PickledDragons:{/b} I'm seeing Paladin for some reason personally", 0, "#000000ff")
default pdDnD2vg2 = ChatEntry (False, "{b}PickledDragons:{/b} Called it!", 0, "#000000ff")











# The script of the game goes in this file.

################################################################################

# General Coding Tips and Advice

    #fade goes to black first then goes to the next scene
    #call goes to the specified label and comes back after return
    #jump goes to the specified label permanently, return ends the game

    #there are specific syntax for button actions, for example normally to show
    #a screen you would say show screen screenName but in a button, you would say:
    #   action Show(screenName)
    #also Function() is specifically to call python statements. you can also
    #call multiple actions in one instance of 'action' by separating them in commas
    #it is good syntax to put the list inside brackets [], but not necessary

################################################################################

######## KNOWN BUGS ############################################################

#1. Phone pops back up when you hit replay when you had phone open
#2. Replay tooltip is persistent when clicked

################################################################################

init python:
    config.layers = [ 'master', 'transient', 'screens', 'overlay', 'gallery']

    # Use a persistent variable (whose value persists, or stays, even after you quit the game) to check
    # if we've set the default value yet.  By doing this, we'll only set the default value the first time the
    # player runs the game, so that after the player sets the preference themselves, the player's preference will stay.
    if not persistent.set_skip_unseen:
        persistent.set_skip_unseen = False
        _preferences.skip_unseen = False    # No, don't be able to skip dialogue that we haven't seen before by default.

    credits = ('BGs from Unsplash', 'ÇaĞin Kargi'), ('', 'Kevin Schmid'), ('', 'Matt Whitacre'), ('', 'Jake Blucker'), ('', 'Dawid Zawila'), ('', 'Wil Stewart'), ('Sprites, CG, GUI, Programming', 'BlueStylusArt'), ('Writing', 'algol_ardhanari'), \
    ('Music', 'In the forest-Les Free Music'), ('', 'Morning light-Les Free Music'), ('', 'Uplifting Dreams-Les Free Music'), ('', 'Summer night in the forest-Mixkit'), ('', 'The sound of light-Tomomi Kato')
    credits_s = "{size=40}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        #c1=c[0]
    credits_s += "\n{size=30}Engine\n{size=30}" + renpy.version()

    #The following code should put a pause after each comma+space and period+space,
    #but it shouldn't affect the period at the end of the dialog.
    def alter_say_strings( str_to_test ):
        str_map = {
            ". " : ". {w=0.3}",
            #"! " : "! {w=0.5}",
            #"? " : "? {w=0.5}",
            #"; " : "; {w=0.3}",
            #", " : ", {w=0.3}",
            #"— " : "—{w=0.3}",
        }
        for key in str_map:
            str_to_test = str_to_test.replace( key, str_map[ key ] )
        return str_to_test

    #this function defines how to add new messages to the message chain
    def add_msg(convo, message):
        convo.append(message) #this adds a new text to the end of the convo
        # also the text seems to be permanently added, (which is good lmao)

define config.say_menu_text_filter = alter_say_strings

#first one is to add a keybind, second is to remove
#$ config.keymap['rollback'].append('t')
init:
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['rollback'].remove('K_PAGEUP')
    $ config.keymap['rollback'].remove('repeat_K_PAGEUP')
    $ config.keymap['rollback'].remove('K_AC_BACK')

    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['toggle_skip'].remove('K_TAB')
    $ config.keymap['fast_skip'].remove('>')
    $ config.keymap['fast_skip'].remove('shift_K_PERIOD')

    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=40}Nihil will return...", text_align=0.5)
    image thanks = Text("{size=40}Thank you for playing", text_align=0.5)


transform ctcblink:
    xalign 0.5 yalign 0.5
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

default ctcOn = False

#This is to turn on the profile box in the say screen/textbox.
default noprofile_true = False
#This is for show/hide the say screen
default hide_say = False
default profileshow = True
default autoOn = False
default profileblush = False

#This is for the phoneMenu screen. by default its state is closed (aka false)
default appOpen = False
#This is for the contacts app, it starts with six rows and keeps going up with
#each contact you add
default contactRows = 0
default contactsOpen = False
#This is for the notes app. You start with 1 row with a locked (and non-interact
#button), and you add as you continue.
default notesRows = 0
default persistent.notesNumber = 0 #keep increasing to get new notes

#This is for the gallery app. You start with 1 row with a locked (and non-interact
#button), and you add as you continue.
default galleryRows = 0
default galleryNumber = 0 #keep increasing to get new notes

#This is for the notification system. if newApp is set to true, then the blue
#notification circle will show
default newMap = False
default newContact = False
default newGallery = False
default newNote = False
##Messages
default michaelNewText = False
default jamesNewText = False
default brettNewText = False
default tylerNewText = False
default bossNewText = False
default andyNewText = False

#Turn the game helper on by default
default gameHelperOn = True
default beginningTutorial = True

#Turn this variable on after the player has played through once.
default persistent.completed = False
default played_through = False

#This is for the inventory
#default giveGift = False #if you are giving a gift to someone
#default useOn = False #if you are trying to use an item on something

default dayofWeek = "FRIDAY"
default date = "June 15"
default timeofDay = "Morning"

#these were for my vn prototype where jumping saves was a major game mechanic, so ignore
#default latestSave = 0
#default latestSaveTime = "Day 1 Morning"

#This is for transforms I guess
#most of this is copied from Far Beyond the World. Sorry Kael!

default move = MoveTransition(1.0)
default dis = Dissolve(0.5)
default slow_dis = Dissolve(2.0)
default slower_dis = Dissolve(3.0)

#for hm part
default player = os.environ.get('username')
default hm1 = False
default hm2 = False
default hm3 = False

transform far_left:
    xalign -0.4 yalign 1.0 xanchor 0.5
transform zero:
    xalign -0.2 yalign 1.0 xanchor 0.5
transform one:
    xalign -0.1 yalign 1.0 xanchor 0.5
transform two:
    xalign 0.1 yalign 1.0 xanchor 0.5
transform three:
    xalign 0.2 yalign 1.0 xanchor 0.5
transform four:
    xalign 0.3 yalign 1.0 xanchor 0.5
transform five:
    xalign 0.4 yalign 1.0 xanchor 0.5
transform six:
    xalign 0.5 yalign 1.0 xanchor 0.5
transform seven:
    xalign 0.6 yalign 1.0 xanchor 0.5
transform eight:
    xalign 0.7 yalign 1.0 xanchor 0.5
transform nine:
    xalign 0.8 yalign 1.0 xanchor 0.5
transform ten:
    xalign 0.9 yalign 1.0 xanchor 0.5
transform eleven:
    xalign 1.0 yalign 1.0 xanchor 0.5
transform twelve:
    xalign 1.1 yalign 1.0 xanchor 0.5
transform thirteen:
    xalign 1.2 yalign 1.0 xanchor 0.5
transform fourteen:
    xalign 1.3 yalign 1.0 xanchor 0.5
transform fifteen:
    xalign 1.4 yalign 1.0 xanchor 0.5

transform sit_one:
    xalign .0 yalign .5
transform sit_one_stand:
    xalign .0 yalign .1
transform sit_two:
    xalign .7 yalign .5
transform sit_two_stand:
    xalign .7 yalign .1
transform sit_three:
    xalign 1.5 yalign .2
transform sit_three_stand:
    xalign 1.5 yalign .5
transform sit_four:
    xalign -0.9 yalign .2
transform sit_five:
    xalign 1.34 yalign .5
transform sit_five_stand:
    xalign 1.34 yalign .1
transform post:
    xalign .3 yalign -.1
transform post_front:
    xalign .4 yalign .5
transform lap:
    xalign -0.15 yalign .5
transform lap_stand:
    xalign -0.15 yalign .0
transform sit_mid:
    xalign .5 yalign .2


################################################################################

# Logos, account choosing, all that stuff happens in this label. Defined by
# default. (account choosing was a game mechanic in prototype, ignore that)

label splashscreen:

    $ renpy.movie_cutscene("intro_1.ogv") #This video format is Theora
    #Theora has extension .ogv, used by lots of web apps (also V8, V9, idk how to get)
    return

################################################################################

# The game starts here.

label start:

    scene bg black
    with Dissolve(3.0)
    stop music fadeout 3.0

    window hide
    $ right_menu = False
    $ quick_menu = False
    $ pause_unlocked = False
    $ right_menu_turnedOn = False

    #$ thursday = DateDivider('0')
    #$ friday = DateDivider('1')

    #clear the tutorial history
    #$ _history_list.clear()

    #Create all the items in the inventory
    #python:
        #player = Player("Josh", 100, 50)
        #player.hp = 50
        #player.mp = 10
        #chocolate = Item("Chocolate", hp=40, image="inv/inv_chocolate.png")
        #banana = Item("Banana", mp=20, image="inv/inv_banana.png")
        #gun = Item("Gun", element="bullets", image="inv/inv_gun.png", cost=7)
        #laser = Item("Laser Gun", element="laser", image="inv/inv_laser.png")
        #inventory = Inventory()
        #add items to the initial inventory:
        #inventory.add(chocolate)
        #inventory.add(chocolate)
        #inventory.add(banana)

    #turn all the quickmenu buttons on after the tutorial
    if beginningTutorial:
        $ back_button = False
        $ history_button = False
        $ fastforward_button = False
        $ auto_mode_button = False

    if not persistent.completed:
        call prePlay

    if persistent.completed:
        $ fastforward_button = True
        $ config.keymap['rollback'].append('mousedown_4')
        $ config.keymap['rollback'].append('K_PAGEUP')
        $ config.keymap['rollback'].append('repeat_K_PAGEUP')
        $ config.keymap['rollback'].append('K_AC_BACK')
        $ config.keymap['skip'].append('K_LCTRL')
        $ config.keymap['skip'].append('K_RCTRL')

    call theWatcher

    #turn on all the quick menu buttons
    #$ beginningTutorial = False

    #call phone_testing

    # This ends the game.
    return

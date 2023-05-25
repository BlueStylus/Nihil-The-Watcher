#This code defines characters, colors, profile images and their properties
#Each section is dedicated to 1 character's profile pictures

################################################################################
# Default character colors

#color of the narration, aka color of all text everywhere
#the narrator character is just no prefix before text
default narratorColor = "#ffffff"
define narrator = Character (None)

#expo, short for exposition, is the narration done by jackie
define think = Character(what_color="#00B2EE")
#image expo think = "Sprites/J 10.png" #this would be the thinking sprite

#this is used for tutorials and things of the like
define gameHelper = Character("", what_color="#008000") #green

screen profile(sprite):
    zorder 99

    if profileshow:
        #add "gui/textbox/textbox profile.png" yalign 1.0
        add "gui/textbox/profilebox.png" yalign 1.0
        add sprite xpos 59 ypos 838 xsize 190 ysize 225
        if profileblush:
            add "Sprites/profile blush.png" xpos 59 ypos 838 xsize 190 ysize 225

default blank = "Sprites/blank.png" #this is for when you want the frame but no character in it. good for transitions

################################################################################
# NIHIL Characters

# Josh
define jo = Character("Joshua", who_color= "#8f8f8f", what_color="#8f8f8f", image = "jo")
image jo 0 = "Sprites/josh 0.png" #tired, looking away, looking down, dejected
image jo 1 = "Sprites/josh 1.png" #looking forward, neutral expression
image jo 2 = "Sprites/josh 2.png" #neutral, looking to the side, mouth closed, serious/a bit concerned expression
image jo 3 = "Sprites/josh 3.png" #same as above but a tiny smile and mouth open

default jo0 = "Sprites/josh0.png" #closed mouth, this is the neutral sprite
default jo1 = "Sprites/josh1.png" #talk sprite
default jo2 = "Sprites/josh2.png" #talk sprite, eyes closed
default jo3 = "Sprites/josh3.png" #nodding talking, eyes closed
default jo4 = "Sprites/josh4.png" #closed mouth, eyes closed
default jo5 = "Sprites/josh5.png" #look to side talk sprite
default jo6 = "Sprites/josh6.png" #look to side talk sprite eyebrow raised
default jo7 = "Sprites/josh7.png" #eyebrows raised, mouth closed
default jo8 = "Sprites/josh8.png" #eyebrows raised, mouth opened
default jo9 = "Sprites/josh9.png" #head turned to front facepalm smile
default jo10 = "Sprites/josh10.png" #look to side smile talk
default jo11 = "Sprites/josh11.png" #look forward slight smile open mouth
default jo12 = "Sprites/josh12.png" #look forward slight smirk close mouth
default jo13 = "Sprites/josh13.png" #closed eyes and a bit angry
default jo14 = "Sprites/josh14.png" #eyes open and a bit angry talking
default jo15 = "Sprites/josh15.png" #head turned to front facepalm angry mouth open
default jo16 = "Sprites/josh16.png" #head turned to front facepalm angry mouth closed
default jo17 = "Sprites/josh17.png" #look down mouth open
default jo18 = "Sprites/josh18.png" #serious look mouth open
default jo19 = "Sprites/josh19.png" #serious look mouth closed eyes closed
default jo20 = "Sprites/josh20.png" #concerned/serious look mouth closed
default jo21 = "Sprites/josh21.png" #eyes closed smile
default jo22 = "Sprites/josh22.png" #transition in drunk part, 1
default jo23 = "Sprites/josh23.png" #transition in drunk part, 2
default jo24 = "Sprites/josh24.png" #transition in drunk part, 3

# James
define ja = Character("James", who_color="#65b871", what_color="#65b871", image = "ja")
image ja 0 = "Sprites/james 0.png" #normal smile, this is his neutral sprite
image ja 1 = "Sprites/james 1.png" #warm smile mouth closed, eyes a little squinty
image ja 2 = "Sprites/james 2.png" #warm smile with mouth open
image ja 3 = "Sprites/james 3.png" #^w^ with mouth open
image ja 4 = "Sprites/james 4.png" #^w^
image ja 5 = "Sprites/james 5.png" #a bit surprised, mouth closed, small, low, eyebrows up, eyes open a bit bigger than normal (huh? are you talking to me? face)
image ja 6 = "Sprites/james 6.png" #one eyebrow down, one eyebrow up, smirking, (is that so? face) arms crossed
image ja 7 = "Sprites/james 7.png" #warm smile arms crossed
image ja 8 = "Sprites/james 8.png" #drunk, head facing down, eyes looking down, UuU like this kind of face
image ja 9 = "Sprites/james 9.png" #drunk, head facing down, eyes looking forward hooded lids
image ja 10 = "Sprites/james 10.png" #drunk, head facing down, eyes looking forward bright
image ja 11 = "Sprites/james 11.png" #drunk, head facing down, eyes looking forward sad
image ja 12 = "Sprites/james 12.png" #drunk, head facing down, eyes closed sad
image ja 13 = "Sprites/james 13.png" #drunk, head facing down, eyes closed happy, content
image ja 14 = "Sprites/james 14.png" #drunk, head facing down, eyes closed happy, laughing
image ja 15 = "Sprites/james 15.png" #concentrating, a bit confused, mouth kind of pouty/tsundere, looking down
image ja 16 = "Sprites/james 16.png" #drunk, head facing down, eyes closed, shoulders high, mouth grimacing, expression scared and panicing
image ja 17 = "Sprites/james 17.png" #drunk, head facing forward, serious face, mouth closed, studying/concentrating face
image ja 18 = "Sprites/james 18.png" #drunk, head facing forward, serious face, eyebrows sad and mouth tightened but same expression
image ja 19 = "Sprites/james 19.png" #drunk, head facing forward, serious face, mouth open
image ja 20 = "Sprites/james 20.png" #drunk, head facing forward, serious face, smiling with mouth open
image ja 21 = "Sprites/james 21.png" #drunk, head facing forward, serious face, eyes closed, kiss
image ja 22 = "Sprites/james 22.png" #drunk, head facing forward, one hand a little up, (wait, come back!), surprised
image ja 23 = "Sprites/james 23.png" #drunk, head facing forward, one hand a little up, (wait, come back!), crying
image ja 24 = "Sprites/james 24.png" #drunk, solemn expression
image ja 25 = "Sprites/james 25.png" #drunk, solemn expression speaking looking forward
image ja 26 = "Sprites/james 26.png" #drunk, solemn expression not speaking looking forward
image ja 27 = "Sprites/james 27.png" #drunk, solemn expression not speaking looking down
image ja 28 = "Sprites/james 28.png" #drunk, solemn expression not speaking looking down
image ja 29 = "Sprites/james 29.png" #side view
image ja 30 = "Sprites/james 30.png" #side view, grimace
image ja 31 = "Sprites/james 31.png" #side view, calm eyes closed
image ja 32 = "Sprites/james 32.png" #drunk, head facing down, eyes closed happy, grinning

# Michael
define m = Character("Michael", who_color="#d96a25", what_color="#d96a25", image = "m")
image m 0 = "Sprites/michael 0.png" #neutral smiling
image m 1 = "Sprites/michael 1.png" #neutral smiling with mouth open
image m 2 = "Sprites/michael 2.png" #neutral, mouth open, not smiling, just has mouth open (talking matter-of-factly), eyebrows up a bit
image m 3 = "Sprites/michael 3.png" #Annoyed, looking at phone
image m 4 = "Sprites/michael 4.png" #looking to side, concerned, mouth grimacing but eyes open, squeezing his arm
image m 5 = "Sprites/michael 5.png" #same as above, but arms crossed and looking to the front
image m 6 = "Sprites/michael 6.png" #smirk with eyes closed, eyebrows down, mischievious look
image m 7 = "Sprites/michael 7.png" #neutral mad
image m 8 = "Sprites/michael 8.png" #laughing/chuckling, eyes open just a little bit but otherwise like ^ᗜ^, same pose as the smirk like ^u^
image m 9 = "Sprites/michael 9.png" #facing front, angry, head angled down a bit, eyebrows down, a bit of a snarl
image m 10 = "Sprites/michael 10.png" #surprised, with arms out in kind of an aggressive-ish pose, also a bit of scared
image m 11 = "Sprites/michael 11.png" #facing front, head angled up, a sad/scared expression, one of regret
image m 12 = "Sprites/michael 12.png" #Hand on head, head angled down a bit, grimacing because of drinking too much, or annoyance, but not too much
image m 13 = "Sprites/michael 13.png" #warm smile, looking up
image m 14 = "Sprites/michael 14.png" #warm smile, looking up eyes closed
image m 15 = "Sprites/michael 15.png" #neutral smiling holding beer
image m 16 = "Sprites/michael 16.png" #neutral holding beer mouth open happy smile
image m 17 = "Sprites/michael 17.png" #neutral holding beer mouth angy smile >:) for when he's crushing a can
image m 18 = "Sprites/michael 18.png" #warm smile looking up mouth open
image m 19 = "Sprites/michael 19.png" #warm smile looking up mouth open eyes closed

default m0 = "Sprites/michael0.png" #shocked
default m1 = "Sprites/michael1.png" #serious/neutral
default m2 = "Sprites/michael2.png" #looking up, a bit surprised and mad
default m3 = "Sprites/michael3.png" #looking up, a bit surprised and mad mouth open
default m4 = "Sprites/michael4.png" #eyes closed grimace kinda

# Brett
define b = Character("Brett", who_color="#df4946", what_color="#df4946", image = "b")
image b 0 = "Sprites/brett 0.png" #Neutral smiling
image b 1 = "Sprites/brett 1.png" #neutral smiling with eyes closed, holding a beer
image b 2 = "Sprites/brett 2.png" #same as above but eyes open
image b 3 = "Sprites/brett 3.png" #Warm smile
image b 4 = "Sprites/brett 4.png" #Grimacing
image b 5 = "Sprites/brett 5.png" #^ᗜ^
image b 6 = "Sprites/brett 6.png" #facing forward, shocked, mouth open, eyes wide
image b 7 = "Sprites/brett 7.png" #looking down a bit, mouth closed, eyes glassy, shocked/despair look
image b 8 = "Sprites/brett 8.png" #holding beer mouth open smiling
image b 9 = "Sprites/brett 9.png" #holding beer mouth smiling

default b0 = "Sprites/brett0.png" #shocked

# Tyler
define t = Character("Tyler", who_color="#75e1ff", what_color="#75e1ff", image = "t")
image t 0 = "Sprites/tyler 0.png" #neutral smiling
image t 1 = "Sprites/tyler 1.png" #kind of surprised, eyebrows up, mouth open, talking (do you need help? face)
image t 2 = "Sprites/tyler 2.png" #warm smile with mouth open
image t 3 = "Sprites/tyler 3.png" #neutral pose but eyebrows curved down sad a bit, and mouth closed but small
image t 4 = "Sprites/tyler 4.png" #do you need help? face but holding a beer
image t 5 = "Sprites/tyler 5.png" #warm smile with mouth open but holding a beer
image t 6 = "Sprites/tyler 6.png" #looking down, mouth open talking, holding a beer
image t 7 = "Sprites/tyler 7.png" #looking down, eyes closed and smiling, holding a beer
image t 8 = "Sprites/tyler 8.png" #yawn with hand covering mouth a bit
image t 9 = "Sprites/tyler 9.png" #giggling, hand over mouth
image t 10 = "Sprites/tyler 10.png" #gasp, both hands over mouth, eyes wide, eyebrows saddened but raised, shoulders raised
image t 11 = "Sprites/tyler 11.png" #head angled a bit down, kind of despair looking eyes, glassy, staring ahead, mouth a tiny bit open
image t 12 = "Sprites/tyler 12.png" #head angled a bit down, closed eyes, staring ahead, mouth grimaced

default t0 = "Sprites/tyler0.png" #gasp

################################################################################
# Main Characters

## Jackie

#this is only for the beginning when there is no profile
#define whoJ = Character(" ", who_color="#00B2EE", what_color="ffffff") #sky blue

#used for the rest of the game even when jackie is thinking
#define j = Character("Jackie", who_color="#00B2EE", image = "j", what_color="ffffff")

# these are variables rather than images because they are parameters for a
# screen with the profile in the bottom left. use this syntax for all profile sprites
#default j0 = "Sprites/Jackie/j0.png" #jackie neutral expression
#default j1 = "Sprites/Jackie/j1.png" #jackie neutral expression with mouth open
#default j2 = "Sprites/Jackie/j2.png" #jackie eyes closed with sweat
#default j3 = "Sprites/Jackie/j3.png" #jackie eyes closed with sweat with mouth open
#default j4 = "Sprites/Jackie/j4.png" #jackie eyebrows low a bit angry
#default j5 = "Sprites/Jackie/j5.png" #jackie eyebrows low a bit angry with mouth open
#default j6 = "Sprites/Jackie/j6.png" #jackie thinking
#default j7 = "Sprites/Jackie/j7.png" #jackie neutral expression smiling
#default j8 = "Sprites/Jackie/j8.png" #jackie neutral expression smiling with mouth open
#default j9 = "Sprites/Jackie/j9.png" #jackie eyes closed neutral

## Pete

#define whoP = Character("???", who_color="#D2B48C", image = "p")
#define p = Character("Pete", who_color="#D2B48C", image = "p") #tan

#define pPhone = Character("Pete", who_color="#D2B48C", image = "pete", what_color = "#00B2EE") #tan

#image p 0 = "Sprites/Pete/p0.png" #pete neutral expression
#image p 1 = "Sprites/Pete/p1.png" #pete neutral expression with mouth open
#image p 2 = "Sprites/Pete/p2.png" #pete smile
#image p 3 = "Sprites/Pete/p3.png" #pete smile with mouth open
#image p 4 = "Sprites/Pete/p4.png" #pete confused and looking up
#image p 5 = "Sprites/Pete/p5.png" #pete confused and looking up with mouth open
#image p 6 = "Sprites/Pete/p6.png" #pete eyes closed teeth smile (grin?) with sweat
#image p 7 = "Sprites/Pete/p7.png" #pete confused looking forward

## Mateo

#who version is before introduction
define whoM = Character("???", who_color="#b5a3a9") #silver, a little pink
#define m = Character("Mateo", who_color="#b5a3a9", image = "mateo") #silver

## Ria

#who version is before introduction
define whoR = Character("???", who_color="#3abb9d") #eden green
define r = Character("Ria", who_color="#3abb9d", image = "r") #eden green

image r0 = "Sprites/R 0.png"

## Stephen

#who version is before introduction
define whoS = Character("???", who_color="#9a689b") #violet
#define s = Character("Stephen", who_color="#9a689b") #violet

## Noel

#who version is before introduction
define whoN = Character("???", who_color="#eed202") #yellow
define n = Character("Noel", who_color="#eed202") #yellow


################################################################################
# Side Characters

## Saburo
define sa = Character("Saburo", who_color="#FFC0CB") #pink

## Haliam
define whoH = Character("???", who_color= "#FFFFFF") #white for now, may change

################################################################################
# NPCs

define mom = Character("Mom", who_color="#FFFFFF")

define attendant = Character("Train Attendant", who_color="#FFFFFF")

define station = Character("Station Speakers", who_color="#FFFFFF")

define receptionist = Character("Receptionist", who_color="#FFFFFF")
default rec = "Sprites/receptionist.png"

define mm1 = Character("Mysterious Man 1", who_color="#FFFFFF")
define mm2 = Character("Mysterious Man 2", who_color="#FFFFFF")
define mm3 = Character("Mysterious Man 3", who_color="#FFFFFF")
define hm = Character("", what_font="fonts/Youmurdererbb-pwoK.otf", what_size=50, what_color="#7d0000")

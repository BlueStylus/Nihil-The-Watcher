################################################################################

#PHONE MAIN PART

screen phoneMenu():

    variant "touch"

    zorder 1

    ## Ensure other screens do not get input while this screen is displayed.

    modal False
    on "hide" action [Hide("contacts"), Hide("gallery"), Hide("messagesMenu"), Hide("notes"), Hide('jamesProfile'), Hide('brettProfile'), Hide('tylerProfile'), Hide('michaelProfile'), SetVariable('appOpen', False)] #efsss
    style_prefix "phoneMenu"

    #image "images/phoneMenu/phone.png" at ramp_up
    #textbutton "back" action Hide("phoneMenu") at ramp_up
    #textbutton "map" action ShowMenu("phoneMenu/map")

    imagemap at ramp_up:
        idle "phoneMenu/phone.png"
        hover "phoneMenu/phone interact.png"
        ground "phoneMenu/phone.png"

        if not appOpen:
            if mapUnlocked:
                hotspot (85, 228, 124, 118): #map app
                    action [If(appOpen == False, true=Show('map'), false=NullAction()), Function(renpy.transition, dissolve)]
            hotspot (215, 227, 111, 119): #contacts app
                action [If(appOpen == False, true=Show('contacts'), false=NullAction()), Function(renpy.transition, dissolve)]
            hotspot (92, 344, 118, 115): #gallery app
                action [If(appOpen == False, true=Show('gallery'), false=NullAction()), Function(renpy.transition, dissolve)]
            hotspot (212, 349, 116, 112): #messages app
                action [If(appOpen == False, true=Show('messagesMenu'), false=NullAction()), Function(renpy.transition, dissolve)]
            hotspot (96, 465, 113, 110): #notes app
                action [If(appOpen == False, true=Show('notes'), false=NullAction()), Function(renpy.transition, dissolve)]

        if newMap:
            add "phoneMenu/notification.png" xpos 101 ypos 242
        if newContact:
            add "phoneMenu/notification.png" xpos 218 ypos 242
        if newGallery:
            add "phoneMenu/notification.png" xpos 101 ypos 355
        if newNote:
            add "phoneMenu/notification.png" xpos 101 ypos 469
        if michaelNewText or jamesNewText:
            add "phoneMenu/notification.png" xpos 218 ypos 355

        hotspot (270, 0, 87, 25):
            action [Hide('phoneMenu')] #off button, hides phone

        hotspot (179, 733, 61, 62):
            if appOpen:
                action [Hide('contacts'), Hide('gallery'), Hide('messages'), Hide('notes'), Function(renpy.transition, dissolve)]
            else:
                action [Hide('phoneMenu')]
        #the home button closes the phone if no apps are open, goes back to home page if apps are open

        text "[dayofWeek]":
            size 42
            pos (49, 152)
            font "fonts/Metropolis/Metropolis-Bold.otf"
        text "[date]":
            size 15
            pos (49, 199)
            font "fonts/Metropolis/Metropolis-Light.otf"
        text "[timeofDay]":
            size 18
            pos (387, 96)
            color "#FFFFFF"
            xanchor 1.0
            font "fonts/Metropolis/Metropolis-Medium.otf"

#this is the transition used to pull out and put back the phone
transform ramp_up:
    on show:
        xalign 1.7 yalign 0.05
        easein 1.0 xalign 0.97
    on hide:
        xalign 0.97 yalign 0.05
        easein 1.0 xalign 1.7

################################################################################

#MAP APP

screen map():

    variant "touch"

    # this doesn't allow the scrollwheel to get rid of the phone
    $ renpy.block_rollback()

    #This is an example from online lol
    #First- a 'screen' (as far as I know) is for 'menus'....they have a set of commands
    #and actions that are specific to them (that will not work with 'labels'.)  You should
    #google 'renpy screen commands' if you would like to learn more.
    tag map
    zorder 120
    modal True
    style_prefix "phoneMenu/map"

    #The various buttons.
    imagemap:

        #Everything needs to be indented a certain way, or you will get an error when you start your game#

        idle "phoneMenu/map/forest idle.png"
        hover "phoneMenu/map/forest hover.png"
        ground "phoneMenu/map/forest ground.png"

        #^^^Here is where you add the names of your image files.  My image files are called group_idle.png, group_hover.png, and group_ground.png....you need to replace my
        #images with your own.  make sure the name of your image goes between the parenthesis ("") and that you add the .png or .jpg after the image name.
        #for this menu screen your images will need to be in the game folder labeled "images" to be found.  If you have an additional folder inside of the
        #images folder, you will need to add the name of that folder to your image for it to be found. Example; if my image were in a folder labeled "mainmenu"  I would
        #put "mainmenu/group_idle.png" in parenthesis after the word idle above.

        if persistent.completed:
            if not hm1:
                if hm2 == True:
                    if hm3 == True:
                        hotspot (927,393,50,50) action [Jump("hmmmMobile"), Hide("map"), Hide('phoneMenu')]
                    else:
                        hotspot (927,393,50,50) action SetVariable('hm1', True)
                else:
                    hotspot (927,393,50,50) action SetVariable('hm1', True)
        #hotspot (647,556,542,129) action Show('charchoicea')
        #hotspot (656,375,140,143) action ShowMenu('load')
        #hotspot (845,376,140,143) action ShowMenu('gallery')
        #hotspot (1002,367,176,150) action Show('mail_main')
        #hotspot (1199,35,1248,88) action Quit('quit')

    #You are here marker
    if youMarker_show:
        add "phoneMenu/map/youMarker.png" pos yM_pos anchor (104, 51)

    if library_show:
        imagebutton:
            idle "phoneMenu/map/libraryMarker.png"
            hover "phoneMenu/map/libraryMarker_interact.png"
            anchor (104, 51) pos (1442, 277)
            action NullAction()

    imagebutton:
        idle "phoneMenu/map/cabinsMarker.png"
        hover "phoneMenu/map/cabinsMarker_interact.png"
        anchor (104, 51) pos (1698, 778)
        action NullAction()

    imagebutton:
        idle "phoneMenu/map/dockMarker.png"
        hover "phoneMenu/map/dockMarker_interact.png"
        anchor (104, 51) pos (624, 406)
        action NullAction()

    imagebutton:
        idle "phoneMenu/map/trailMarker.png"
        hover "phoneMenu/map/trailMarker_interact.png"
        anchor (104, 51) pos (1022, 135)
        action NullAction()

    imagebutton:
        idle "phoneMenu/map/trail1Marker.png"
        hover "phoneMenu/map/trail1Marker_interact.png"
        anchor (104, 51) pos (432, 854)
        action NullAction()

    text "Grundy Lake Provincial Park" xpos 20 ypos 20 size 40 color "#ffffff"
    text "ON-522, Ontario, Canada" xpos 20 ypos 70 size 30 color "#ffffff"

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/map/map exit button half invis.png"
        hover "phoneMenu/map/map exit button.png"
        action [Hide("map"), Function(renpy.transition, dissolve)]

################################################################################

#CONTACTS APP
screen contacts():

    variant "touch"

    tag phone
    zorder 81
    modal True

    #add "contacts screen"
    add "phoneMenu/contacts bg.png" xpos 1486 ypos 131
    vpgrid:

        rows 1 + contactRows
        cols 1
        spacing 0
        #scrollbars "vertical"
        #xpos 1670 #this is for if i have the scroll turned on
        xpos 1495 #this is for if the scroll is off
        ypos 131
        xsize 365
        ysize 599
        #draggable True
        #mousewheel True

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        #side_xalign 0.5

        if not contactsOpen:
            imagebutton:
                idle "phoneMenu/contact james.png"
                hover "phoneMenu/contact james-interact.png"
                action Show("jamesProfile"), Function(renpy.transition, dissolve)
            imagebutton:
                idle "phoneMenu/contact brett.png"
                hover "phoneMenu/contact brett-interact.png"
                action Show("brettProfile"), Function(renpy.transition, dissolve)
            imagebutton:
                idle "phoneMenu/contact tyler.png"
                hover "phoneMenu/contact tyler-interact.png"
                action Show("tylerProfile"), Function(renpy.transition, dissolve)
            imagebutton:
                idle "phoneMenu/contact michael.png"
                hover "phoneMenu/contact michael-interact.png"
                action Show("michaelProfile"), Function(renpy.transition, dissolve)

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('contacts'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

screen jamesProfile():

    variant "touch"

    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)

    add "phoneMenu/profile james.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('jamesProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

screen brettProfile():

    variant "touch"

    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)
    add "phoneMenu/profile brett.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('brettProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

screen tylerProfile():

    variant "touch"

    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)
    add "phoneMenu/profile tyler.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('tylerProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

screen michaelProfile():

    variant "touch"

    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)
    add "phoneMenu/profile michael.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('michaelProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

################################################################################

#NOTES APP, individual notes are defined in notes.rpy
screen notes():

    variant "touch"

    tag phone #apps (screens) with phone tag can only be shown one at a time
    zorder 81
    modal True

    #add "notes screen"
    add "phoneMenu/notes bg.png" xpos 1486 ypos 131
    vpgrid:

        rows 1 + notesRows
        cols 2
        spacing 0
        scrollbars "vertical"
        draggable True
        mousewheel True

        #this vpgrid is positioned exactly where the phone screen is. don't touch!
        #also don't try to replace with area(). doesn't work
        xpos 1670
        ypos 131
        xsize 365
        ysize 599

        #since we have scrollbars, we have to position the side rather than
        #the vpgrid proper.
        side_xalign 0.5

        #the following syntax shows a locked notes for when there are no notes
        #(aka at the beginning of the game). you unlock notes by incrementing the
        #notesNumber variable at certain points in the game script. Syntax is:
        #$ notesNumber += 1
        #if persistent.notesNumber == 0:
        if not persistent.completed:
            imagebutton:
                idle "phoneMenu/notes button lock.png"
                hover "phoneMenu/notes button lock.png"

        #this syntax makes it so that the lock disappears and is replaced by a
        #new note button. Using >= notation, you can increment and still keep the
        #original notes
        #if persistent.notesNumber >= 1:
        if persistent.completed:
            imagebutton:
                idle "phoneMenu/notes button.png"
                hover "phoneMenu/notes button interact.png"
                action [Show("findme"), SetVariable('newNote', False)]

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('notes'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

################################################################################

#gallery APP, individual pictures are defined as screens in gallery.rpy
screen gallery():

    variant "touch"

    tag phone
    zorder 81
    modal True

    #add "gallery screen"
    add "phoneMenu/gallery bg.png" xpos 1486 ypos 131
    vpgrid:

        rows 1 + galleryRows
        cols 2
        spacing 0
        scrollbars "vertical"
        draggable True
        mousewheel True

        #this vpgrid is positioned exactly where the phone screen is. don't touch!
        #also don't try to replace with area(). doesn't work
        xpos 1670
        ypos 131
        xsize 365
        ysize 599

        #since we have scrollbars, we have to position the side rather than
        #the vpgrid proper.
        side_xalign 0.5

        #the following syntax shows a picture. just keep repeating this syntax
        #with a new variable in the if statement, and it'll show more pics
        if shopPic: #shopPic is a tester to make sure this works, don't worry about it lol
            imagebutton:
                idle "phoneMenu/gallery/gallery button.png"
                hover "phoneMenu/gallery/gallery button interact.png"
                action [Show('shopPicture'), Function(renpy.transition, dissolve)]

        if not persistent.kissPic:
            imagebutton:
                idle "phoneMenu/notes button lock.png"
                hover "phoneMenu/notes button lock.png"

        if persistent.kissPic:
            imagebutton:
                idle "phoneMenu/gallery/campfire kiss button.png"
                hover "phoneMenu/gallery/campfire kiss button interact.png"
                action [Show('kissPicture'), Function(renpy.transition, dissolve)]

        if persistent.passionPic:
            imagebutton:
                idle "phoneMenu/gallery/campfire kiss button.png"
                hover "phoneMenu/gallery/campfire kiss button interact.png"
                action [Show('passionPicture'), Function(renpy.transition, dissolve)]

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('gallery'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

################################################################################

#MESSAGES APP, add messages throughout the story using below function
screen messagesMenu():

    variant "touch"

    tag phone
    zorder 81
    modal True

    #add "contacts screen"
    add "phoneMenu/messages bg.png" xpos 1486 ypos 131
    viewport:

        spacing 10
        child_size (365, 150)
        scrollbars "vertical"
        xpos 1670
        ypos 131
        xsize 365
        ysize 599
        draggable True
        mousewheel True

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        #each button to get to the text thread is the imagebutton on top
        #of text, so that you can only click the imagebutton and not anything else

        #tyler
        fixed:
            ypos 0
            text "Tyler Moore" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text tylerTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text tylerTextDate xpos 225 ypos 55 size 18 color "#3d3d3d"
            imagebutton:
                idle "phoneMenu/messages button.png"
                hover "phoneMenu/messages button interact.png"
                action [Show("msgConvo", msgList=tylerConvo), Function(renpy.transition, dissolve), SetVariable('tylerNewText', False)]
            if tylerNewText:
                add "phoneMenu/notification.png" xalign 1.0 ypos 10

        #brett
        fixed:
            ypos 100
            text "Brett Taylor" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text brettTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text brettTextDate xpos 225 ypos 55 size 18 color "#3d3d3d"
            imagebutton:
                idle "phoneMenu/messages button.png"
                hover "phoneMenu/messages button interact.png"
                action [Show("msgConvo", msgList=brettConvo), Function(renpy.transition, dissolve), SetVariable('brettNewText', False)]
            if brettNewText:
                add "phoneMenu/notification.png" xalign 1.0 ypos 10

        #michael
        fixed:
            ypos 200
            text "Michael Kim" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text michaelTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text michaelTextDate xpos 225 ypos 58 size 18 color "#3d3d3d"
            imagebutton:
                idle "phoneMenu/messages button.png"
                hover "phoneMenu/messages button interact.png"
                action [Show("msgConvo", msgList=michaelConvo), Function(renpy.transition, dissolve), SetVariable('michaelNewText', False)]
            if michaelNewText:
                add "phoneMenu/notification.png" xalign 0.9 ypos 10

        #james
        fixed:
            ypos 300
            text "James Mason" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text jamesTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text jamesTextDate xpos 225 ypos 55 size 18 color "#3d3d3d"
            if hm2 == False and persistent.completed:
                imagebutton:
                    idle "phoneMenu/messages button.png"
                    hover "phoneMenu/messages button interact.png"
                    action [Show("msgConvo", msgList=jamesConvo), Function(renpy.transition, dissolve), SetVariable('jamesNewText', False)]
            else:
                imagebutton:
                    idle "phoneMenu/messages button.png"
                    hover "phoneMenu/messages button interact.png"
                    action [Show("msgConvo", msgList=hmConvo), Function(renpy.transition, dissolve), SetVariable('jamesNewText', False)]
            if jamesNewText:
                add "phoneMenu/notification.png" xalign 1.0 ypos 10

        #boss
        fixed:
            ypos 400
            text "Boss" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text bossTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text bossTextDate xpos 225 ypos 55 size 18 color "#3d3d3d"
            imagebutton:
                idle "phoneMenu/messages button.png"
                hover "phoneMenu/messages button interact.png"
                action [Show("msgConvo", msgList=bossConvo), Function(renpy.transition, dissolve), SetVariable('bossNewText', False)]
            if bossNewText:
                add "phoneMenu/notification.png" xalign 1.0 ypos 10

        #andy
        fixed:
            ypos 500
            text "Andy Cox" xpos 9 ypos 5 size 30 color "#000000" #sender name
            text andyTextPreview xpos 9 ypos 42 size 18 color "#000000"
            text andyTextDate xpos 225 ypos 55 size 18 color "#3d3d3d"
            imagebutton:
                idle "phoneMenu/messages button.png"
                hover "phoneMenu/messages button interact.png"
                action [Show("msgConvo", msgList=andyConvo), Function(renpy.transition, dissolve), SetVariable('andyNewText', False)]
            if andyNewText:
                add "phoneMenu/notification.png" xalign 1.0 ypos 10

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('messagesMenu'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        action [Hide('phoneMenu')] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences")]
            xalign 0
            yalign 0

################################################################################

#this screen is general for any text convo, enter a parameter for msgList to
#specify which convo it is.

define speechBubble = "phoneMenu/speech_bubble.webp"

screen msgConvo(msgList):

    variant "touch"

    tag convo
    zorder 82

    if appOpen:
        fixed:
            pos(1486, 131)
            add "phoneMenu/messages bg.png"
            add "phoneMenu/message convo bg.png"

            text msgList[2][1] size 40 xpos 15

            side "c r":

                area (0, 56, 365, 487)

                viewport id "mes":

                    # Enable screen to be draggable
                    draggable True
                    mousewheel True
                    # Add visual scrollbar indicator
                    # scrollbars "vertical"
                    yinitial 1.0

                    frame:

                        margin (10, 10)
                        padding (0, 0)
                        background None

                        vbox:
                            # Makes so that your own messages appear on the right side of the phone
                            xfill True

                            # Add 10 pixels of distance between speech bubbles
                            spacing 10

                            for sender, senderName, message, picture in msgList:

                                if senderName == "date":

                                    hbox:
                                        xalign 0.5
                                        text message size 20 text_align 0.5

                                elif sender == 0:
                                    # sender 0 is always us
                                    hbox:
                                        # Make it so it goes to the right side of the hbox
                                        xalign 1.0

                                        # Text of the message from us
                                        frame:
                                            # Set background of speech bubble
                                            background Frame(im.MatrixColor(speechBubble, im.matrix.colorize("#fff", "#fff")), 8, 8)
                                            # im.matrix.colorize(black_color, white_color) returns an im.matrix that colorizes a black and white image.
                                            #https://www.renpy.org/doc/html/im.html#im.matrix.colorize
                                            #idk what 8, 8 means :/

                                            # Add space to the left of the message. The space on the right is larger to
                                            # include the avatar.
                                            left_padding 12
                                            right_padding 12

                                            # Add space between the top and bottom edge of the speech bubble
                                            ypadding 12
                                            xpadding 12

                                            # If messages are too long, this makes sure that the speech bubble won't get ultra wide
                                            xmaximum 475

                                            vbox:
                                                spacing 10

                                                #text senderName:
                                                    #size 15
                                                    #color "#000000"
                                                    #if sender == 0:
                                                        #xalign 1.0
                                                    #else:
                                                        #xalign 0.0

                                                text message:
                                                    size 25
                                                    color "#000000"

                                                if picture == "no":
                                                    pass #pass means do nothing, kinda like adding 'not' but that doesn't work for some reason lol
                                                else:
                                                    add picture xsize 200

                                else:
                                    # Someone else is speaking
                                    hbox:
                                        # Make it so it goes to the left side of the hbox
                                        xalign 0.0

                                        if senderName == "Michael":
                                            add "phoneMenu/messages michael.png"
                                        elif senderName == "Tyler":
                                            add "phoneMenu/messages tyler.png"
                                        elif senderName == "James":
                                            add "phoneMenu/messages james.png"
                                        elif senderName == "Brett":
                                            add "phoneMenu/messages brett.png"
                                        elif senderName == "Joshua":
                                            add "phoneMenu/messages josh.png"
                                        elif senderName == "hm":
                                            add "phoneMenu/messages hm.png"

                                        spacing 8

                                        # Text of the message
                                        frame:
                                            # Set background of speech bubble
                                            background Frame(im.MatrixColor(speechBubble, im.matrix.colorize("0f0", "#fff")), 8, 8)

                                            # Add space to the left of the message. The space on the left is larger to
                                            # include the avatar.
                                            left_padding 12
                                            right_padding 12

                                            # Add space between the top and bottom edge of the speech bubble
                                            ypadding 12
                                            xpadding 12

                                            # If messages are too long, this makes sure that the speech bubble won't get ultra wide
                                            xmaximum 475

                                            vbox:
                                                spacing 10

                                                #text senderName:
                                                    #size 15
                                                    #color "#000000"
                                                    #if sender == 0:
                                                        #xalign 1.0
                                                    #else:
                                                        #xalign 0.0

                                                if message == "m̷̡̗̬̳͚̆̐̈́͂̎̚e̶̩̺̩̰͋͆͋̈́͂͘͠l̵͍͈̪͔͚̰̪͚̀͛̍̊i̸̺͆͂̽̌̃͝s̴̗̺͙̳̲̩̄s̸̛̽̅̇̈́̐̕ͅp̴̤̖̦͂͊̌͐̑͒̉̇m̸̰̺̞̻̺͖̭̺̌̉̎̇́̂͘l̷̗̫̓͑͂̍̒ņ̵̛̮̪̭͈̰͈̽̕q̸̹̥̪͓͖̘̮̟͐̌͑̀͘c̴̲̝͂̑͒?̷̭͍̖̝͙̼̟̔̚͝ͅ":
                                                    if hm1 == True:
                                                        if hm3 == True:
                                                            textbutton message style "glitchMsg" action [Jump("hmmmMobile"), Hide('messagesMenu'), Hide('msgConvo', msgList=jamesConvo), Hide('phoneMenu')]
                                                        else:
                                                            textbutton message style "glitchMsg" action [SetVariable('hm2', True), Show('msgConvo', msgList=hmConvo)]
                                                    else:
                                                        textbutton message style "glitchMsg" action [SetVariable('hm2', True), Show('msgConvo', msgList=hmConvo)]
                                                else:
                                                    text message:
                                                        size 25
                                                        color "#000000"

                                                if picture == "no":
                                                    pass
                                                else:
                                                    add picture xsize 200

                vbar value YScrollValue("mes"):
                    unscrollable "hide"
        imagebutton:
            idle "phoneMenu/home button invis.png" #this image is transparent
            hover "phoneMenu/home button invis.png" #this image is transparent
            xpos 1639 #this is the exact x-value. don't touch!!
            ypos 751 #this is the exact y-value. don't touch!!
            action Hide('msgConvo'), Function(renpy.transition, dissolve)

style glitchMsg is button:
    color "00ff0000"

style glitchMsg_text is text:
    font "fonts/arial.ttf"
    color "#000000"
    hover_color "#a10000"
    size 20

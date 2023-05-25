################################################################################

#PHONE MAIN PART

default mtt = MouseTooltip(Text(""), padding={"x": 35, "y": -20})

screen phoneMenu():

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
                    action [If(appOpen == False, true=Show('map'), false=NullAction()), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Map", size=25, font="fonts/GARA.TTF"))]
                    unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            hotspot (215, 227, 111, 119): #contacts app
                action [If(appOpen == False, true=Show('contacts'), false=NullAction()), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Contacts", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            hotspot (92, 344, 118, 115): #gallery app
                action [If(appOpen == False, true=Show('gallery'), false=NullAction()), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Gallery", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            hotspot (212, 349, 116, 112): #messages app
                action [If(appOpen == False, true=Show('messagesMenu'), false=NullAction()), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Messages", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            hotspot (96, 465, 113, 110): #notes app
                action [If(appOpen == False, true=Show('notes'), false=NullAction()), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Notes", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

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
            action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        hotspot (179, 733, 61, 62):
            if appOpen:
                action [Hide('contacts'), Hide('gallery'), Hide('messages'), Hide('notes'), Function(renpy.transition, dissolve)]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            else:
                action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
                unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
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

    #show the tooltip that follows the mouse
    add mtt

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
default mapUnlocked = False
default youMarker_show = True
default library_show = False
default yM_pos = (1253, 562) #This is where the youMarker is located

screen map():
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
                        hotspot (927,393,50,50) action [Jump("hmmm"), Hide("map"), Hide('phoneMenu')]
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
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Go here", size=25, font="fonts/GARA.TTF"))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
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
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        action [Hide("map"), Function(renpy.transition, dissolve), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

################################################################################

#CONTACTS APP
screen contacts():
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
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('contacts'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

screen jamesProfile():
    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)

    add "phoneMenu/profile james.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('jamesProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

screen brettProfile():
    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)

    add "phoneMenu/profile brett.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('brettProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

screen tylerProfile():
    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)

    add "phoneMenu/profile tyler.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('tylerProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

screen michaelProfile():
    zorder 82
    modal True
    on "hide" action SetVariable('contactsOpen', False)
    on "show" action SetVariable('contactsOpen', True)

    add "phoneMenu/profile michael.png" xpos 1486 ypos 131

    #home button
    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('michaelProfile'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

################################################################################

#NOTES APP, individual notes are defined in notes.rpy
screen notes():
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
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('notes'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

################################################################################

#gallery APP, individual pictures are defined as screens in gallery.rpy
screen gallery():
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
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('gallery'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

    on "hide" action SetVariable('appOpen', False)
    on "show" action SetVariable('appOpen', True)

################################################################################

#MESSAGES APP, add messages throughout the story using below function
screen messagesMenu():
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
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25, font="fonts/GARA.TTF"))]
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('messagesMenu'), Function(renpy.transition, dissolve)

    #off button
    imagebutton:
        xpos 1728
        ypos 0
        idle "phoneMenu/off button invis.png" #this image is transparent
        hover "phoneMenu/off button invis.png" #this image is transparent
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Turn off", size=25, font="fonts/GARA.TTF"))]
        unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
        action [Hide('phoneMenu'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] #off button, hides phone

    #pause button
    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]

        if pause_mtt:
            add mtt

################################################################################

#this screen is general for any text convo, enter a parameter for msgList to
#specify which convo it is.

define speechBubble = "phoneMenu/speech_bubble.webp"

screen msgConvo(msgList):
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
                                                            textbutton message style "glitchMsg" action [Jump("hmmm"), Hide('messagesMenu'), Hide('msgConvo', msgList=jamesConvo), Hide('phoneMenu')]
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
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Return", size=25))]
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

################################################################################

#TESTER LABEL TO TEST PHONE

label phone_testing:

    #this... this seems like too many variables
    $ back_button = True
    $ history_button = True
    $ fastforward_button = True
    $ auto_mode_button = True
    $ right_menu = True
    $ right_menu_turnedOn = True
    $ phone_menu_button_turnedOn = True
    $ inventory_button_turnedOn = True
    $ load_button_turnedOn = True
    $ save_load_button_turnedOn = True
    $ youMarker_show = True
    $ mapUnlocked = True
    $ library_show = False
    #$ yM_pos = (1093, 681)

    $ date += 1

    #this is for contacts app in phone: set a boolean variable to false at the
    #beginning of a label, then say $ variable = True later, and the contact
    #will be unlocked in the app
    default secondmichael = False

    scene bg bedroom with dissolve
    show screen profile(jo0) with dissolve
    show ja 0 with dissolve

    ja "a"
    ja "b"
    ja "c"
    ja "d"
    ja "e"
    ja "f"
    ja "g"
    ja "h"
    #$ shopPic = True
    $ contactRows += 1
    $ secondmichael = True
    $ persistent.notesNumber += 1

    $ add_msg([1, "new message!! please check me out in the phone"], michaelConvo)
    $ michaelNewText = True
    $ shopPic = True

    ja "i"
    $ kissPic = True
    ja "j"
    $ passionPic = True
    ja "k"
    ja "l"
    ja "m"
    ja "n"
    ja "o"

    #jump demo_0
    return

################################################################################

# define the thread chains here

default michaelConvo = [
    #[0 is me and 1 2 etc is recipient, "name to show icon", "message text", "no image if no, image if type in file address"]
    [0, "date", "May 28", "no"],
    [0, "Joshua", "do you want to go camping?", "no"],
    [1, "Michael", "oh hell yea when", "no"],
    [0, "Joshua", "not sure. i'm going to ask the others.", "no"],
    [1, "Michael", "ok well i should be free cuz no school, just lemme know", "no"],
    [0, "Joshua", "understood.", "no"],
    [0, "date", "June 2", "no"],
    [0, "Joshua", "is June 15-16 okay?", "no"],
    [1, "Michael", "yuh", "no"],
    [1, "Michael", "we takin ur car?", "no"],
    [0, "Joshua", "yes, i'll be driving.", "no"],
    [0, "Joshua", "i'll have everyone bring something. is that okay?", "no"],
    [1, "Michael", "yea whatchu need", "no"],
    [1, "Michael", "i gotchu B)", "no"],
    [0, "Joshua", "not sure yet.", "no"],
    [0, "date", "June 3", "no"],
    [1, "Michael", "come over", "no"],
    [0, "Joshua", "is everything okay?", "no"],
    [1, "Michael", "fuck me", "no"],
    [0, "Joshua", "on my way.", "no"],
    [0, "date", "June 10", "no"],
    [1, "Michael", "k i got drinks", "no"],
    [1, "Michael", "keeping them in fridge good?", "no"],
    [0, "Joshua", "yes. please put them in cooler on Friday!", "no"],
    [1, "Michael", "k", "no"],
    [0, "date", "June 15", "no"],
    [0, "Joshua", "wake up, michael.", "no"],
    [1, "Michael", "coming down now", "no"],
    [1, "Michael", "i was awake already fyi", "no"],
]

default jamesConvo = [
    [0, "date", "May 28", "no"],
    [0, "Joshua", "when you come back to NB, do you want to go camping?", "no"],
    [1, "James", "Oh that sounds really fun", "no"],
    [1, "James", "Where to", "no"],
    [0, "Joshua", "what about grundy lake?", "no"],
    [0, "Joshua", "when is your semester over?", "no"],
    [1, "James", "Ok thats pretty cool", "no"],
    [1, "James", "May 31 is last final and party on June 2 lmao", "no"],
    [0, "Joshua", "are your parents getting you?", "no"],
    [1, "James", "No they told me you were getting me lol", "no"],
    [0, "Joshua", "yes, i talked to them about it last week. what day should i come?", "no"],
    [1, "James", "June 3", "no"],
    [0, "Joshua", "sounds good", "no"],
    [0, "date", "June 3", "no"],
    [0, "Joshua", "when should i be there?", "no"],
    [1, "James", "Can you come at like 2", "no"],
    [1, "hm", "m̷̡̗̬̳͚̆̐̈́͂̎̚e̶̩̺̩̰͋͆͋̈́͂͘͠l̵͍͈̪͔͚̰̪͚̀͛̍̊i̸̺͆͂̽̌̃͝s̴̗̺͙̳̲̩̄s̸̛̽̅̇̈́̐̕ͅp̴̤̖̦͂͊̌͐̑͒̉̇m̸̰̺̞̻̺͖̭̺̌̉̎̇́̂͘l̷̗̫̓͑͂̍̒ņ̵̛̮̪̭͈̰͈̽̕q̸̹̥̪͓͖̘̮̟͐̌͑̀͘c̴̲̝͂̑͒?̷̭͍̖̝͙̼̟̔̚͝ͅ", "no"],
    [0, "Joshua", "sure, leaving now!", "no"],
    [0, "Joshua", "i'm outside your dorm building", "no"],
    [1, "James", "Omw down", "no"],
    [0, "date", "June 11", "no"],
    [1, "James", "I didn't know we had to bring stuff sorry", "no"],
    [1, "James", "What are we still missing I'll get it", "no"],
    [0, "Joshua", "just bring your bluetooth speaker", "no"],
    [1, "James", "Are you sure thats it? I can get some snacks or smth", "no"],
    [0, "Joshua", "don't worry we have enough!", "no"],
    [1, "James", "Okay", "no"],
]

default hmConvo = [
    [0, "date", "May 28", "no"],
    [0, "Joshua", "when you come back to NB, do you want to go camping?", "no"],
    [1, "James", "Oh that sounds really fun", "no"],
    [1, "James", "Where to", "no"],
    [0, "Joshua", "what about grundy lake?", "no"],
    [0, "Joshua", "when is your semester over?", "no"],
    [1, "James", "Ok thats pretty cool", "no"],
    [1, "James", "May 31 is last final and party on June 2 lmao", "no"],
    [0, "Joshua", "are your parents getting you?", "no"],
    [1, "James", "No they told me you were getting me lol", "no"],
    [0, "Joshua", "yes, i talked to them about it last week. what day should i come?", "no"],
    [1, "James", "June 3", "no"],
    [0, "Joshua", "sounds good", "no"],
    [0, "date", "June 3", "no"],
    [0, "Joshua", "when should i be there?", "no"],
    [1, "James", "Can you come at like 2", "no"],
    [0, "Joshua", "sure, leaving now!", "no"],
    [0, "Joshua", "i'm outside your dorm building", "no"],
    [1, "James", "Omw down", "no"],
    [0, "date", "June 11", "no"],
    [1, "James", "I didn't know we had to bring stuff sorry", "no"],
    [1, "James", "What are we still missing I'll get it", "no"],
    [0, "Joshua", "just bring your bluetooth speaker", "no"],
    [1, "James", "Are you sure thats it? I can get some snacks or smth", "no"],
    [0, "Joshua", "don't worry we have enough!", "no"],
    [1, "James", "Okay", "no"],
]

default tylerConvo = [
    [0, "date", "May 28", "no"],
    [0, "Joshua", "do you want to go camping?", "no"],
    [1, "Tyler", "oh that sounds really fun!! where to owo", "no"],
    [0, "Joshua", "grundy lake", "no"],
    [1, "Tyler", "oooh never been there before, exciting! XD", "no"],
    [1, "Tyler", "when?", "no"],
    [0, "Joshua", "not sure when is good for everyone. was thinking june 9-10?", "no"],
    [1, "Tyler", "noooo im busy that weekend! TmT", "no"],
    [0, "Joshua", "no worries, what about the next weekend? 16-17", "no"],
    [1, "Tyler", "looks free 2 me! cant wait lol", "no"],
    [0, "date", "June 2", "no"],
    [0, "Joshua", "actually can you do june 15-16 for the camping trip?", "no"],
    [1, "Tyler", "yeeeep", "no"],
    [0, "Joshua", "okay thank you", "no"],
    [1, "Tyler", "yq", "no"],
    [1, "Tyler", "*yw lol", "no"],
    [0, "date", "June 9", "no"],
    [0, "Joshua", "do you mind lending me some of your tupperware?", "no"],
    [1, "Tyler", "ummm is it for the camping thing? sure haha", "no"],
    [0, "Joshua", "yeah, i'll come by to get them later", "no"],
    [1, "Tyler", "wait actually im going that side of town in a bit :3", "no"],
    [1, "Tyler", "ill just go 2 your house first! XD", "no"],
    [0, "Joshua", "okay see you soon.", "no"],
    [0, "date", "June 15", "no"],
    [1, "Tyler", "brett and me r at the park! :3", "no"],
    [0, "Joshua", "here.", "no"],
]

default brettConvo = [
    [0, "date", "May 28", "no"],
    [0, "Joshua", "by the way do you want to go camping?", "no"],
    [1, "Brett", "bet when dude?", "no"],
    [0, "Joshua", "i'm thinking june 9-10? are you free then?", "no"],
    [1, "Brett", "probs, lemme check", "no"],
    [1, "Brett", "lmaooo jkjk im obvi free", "no"],
    [0, "Joshua", "actually tyler just texted he can't, what about the next weekend", "no"],
    [1, "Brett", "u already know im free lmao", "no"],
    [1, "Brett", "wait shit i actually have a dentist apt that sunday", "no"],
    [1, "Brett", "imma try to move it, hold up", "no"],
    [0, "date", "June 2", "no"],
    [0, "Joshua", "so were you able to move your dentist appointment?", "no"],
    [1, "Brett", "shit sorry for not responding, nah i couldnt", "no"],
    [1, "Brett", "i could take the friday off work tho, Maki can cover me", "no"],
    [0, "Joshua", "are you sure? ill check with everyone", "no"],
    [1, "Brett", "he owes me 1, he gotta. mans code and stufff", "no"],
    [0, "Joshua", "we're good for 15-16.", "no"],
    [1, "Brett", "sick", "no"],
    [0, "date", "June 9", "no"],
    [0, "Joshua", "hey can you get some meats from the market?", "no"],
    [1, "Brett", "uhh i guess? what do you need", "no"],
    [0, "Joshua", "i have a list, are you working now?", "no"],
    [1, "Brett", "ye", "no"],
    [0, "Joshua", "i'll come to the store", "no"],
    [0, "date", "June 13", "no"],
    [1, "Brett", "yo got the shit lol", "no"],
    [1, "Brett", "does james eat meat? das a lot of meat", "no"],
    [0, "Joshua", "pretty sure he does, he eats burgers like every week if i remember right.", "no"],
    [1, "Brett", "truuuu tho anywyays walkin to ur house now", "no"],
    [0, "Joshua", "let me pick you up! wait there.", "no"],
    [1, "Brett", "wait so are you cooking all that today", "no"],
    [0, "Joshua", "no, just seasoning. we'll cook the meat at the campfire", "no"],
    [1, "Brett", "holy shit cant wait", "no"],
    [0, "date", "June 15", "no"],
    [1, "Brett", "you picking us up or what", "no"],
    [0, "Joshua", "actually can you and tyler go to the park? meet you there", "no"],
    [1, "Brett", "ya got it boss", "no"],
]

default andyConvo = [
    [0, "date", "May 20", "no"],
    [0, "Joshua", "are you in Sudbury?", "no"],
    [1, "Andy", "yea rich client, you know how it is", "no"],
    [0, "Joshua", "yea.", "no"],
    [0, "Joshua", "you coming over tomorrow?", "no"],
    [1, "Andy", "uh huh, should be fun ;)", "no"],
    [0, "Joshua", "see you tomorrow.", "no"],
    [1, "Andy", "cya", "no"],
]

default bossConvo = [
    [0, "date", "May 23", "no"],
    [1, "Boss", "are you coming in tomorrow?", "no"],
    [1, "Boss", "big event", "no"],
    [0, "Joshua", "yea.", "no"],
    [0, "date", "June 2", "no"],
    [0, "Joshua", "can i take friday the 15th off?", "no"],
    [1, "Boss", "got something going on that day?", "no"],
    [0, "Joshua", "camping trip with some friends", "no"],
    [1, "Boss", "you know people usually find a legitimate excuse to skip work", "no"],
    [0, "Joshua", "but i'm your favorite", "no"],
    [1, "Boss", "you get bigger and bigger balls everyday huh hahaha", "no"],
    [0, "Joshua", "sorry, you know i don't miss work if it isn't important", "no"],
    [1, "Boss", "im kidding im kidding~ you can go if i can find someone to cover for you", "no"],
    [1, "Boss", "okay you're good", "no"],
    [0, "Joshua", "thank you, i'll make it up to you!", "no"],
    [1, "Boss", "no need. take care", "no"],
    [0, "Joshua", "thank you, really.", "no"],
]


#variable for preview for the text
default michaelTextPreview = "i was awake already fyi"
default michaelTextDate = "Today 9:28 AM"
default jamesTextPreview = "Okay"
default jamesTextDate = "June 11"
default tylerTextPreview = "here."
default tylerTextDate = "Today 10:03 AM"
default brettTextPreview = "ya got it boss"
default brettTextDate = "Today 8:45 AM"
default andyTextPreview = "cya"
default andyTextDate = "May 20"
default bossTextPreview = "thank you, really."
default bossTextDate = "June 2"

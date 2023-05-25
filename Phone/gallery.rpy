##The gallery app on the phone has its own .rpy file because of the number of
##pics Jackie will have throughout the story. each pic is its own screen.

################################################################################

#You have to turn on (aka set true) each variable to get a new picture. Yea it's
#tedious to code but idk how else to do it.
default shopPic = False
default persistent.kissPic = False
default persistent.passionPic = False

screen galleryMenu:
    add "BGs/bg black.png"
    text "Gallery" xpos 50 ypos 25 size 50 color "#ffffff"
    hbox:
        area (1400, 100, 400, 600)
        text "Click on a text button to see the image. With the image open, use the buttons at the left and right of the game screen to change pictures. Use the X button at the bottom to exit."

    imagebutton:
        xalign 0.98 yalign 0.02
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("galleryMenu"), Function(renpy.transition, dissolve)]

    grid 1 9:
        xpos 50
        ypos 100

        textbutton "Main Menu Screen" action [ShowMenu('menuGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Bonfire" action [ShowMenu('bonfireGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Campground-Day" action [ShowMenu('campDayGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Campground-Sunset" action [ShowMenu('campSunsetGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Campground-Night" action [ShowMenu('campNightGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Trunk" action [ShowMenu('trunkGallery'), Function(renpy.transition, dissolve)]

        textbutton "BG Road" action [ShowMenu('roadGallery'), Function(renpy.transition, dissolve)]

        textbutton "CG Kiss" action [ShowMenu('kissGallery'), Function(renpy.transition, dissolve)]

        textbutton "CG Passion" action [ShowMenu('passionGallery'), Function(renpy.transition, dissolve)]

screen menuGallery:
    add "BGs/bg campfire.png"

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('bonfireGallery'), Hide("menuGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("menuGallery"), Function(renpy.transition, dissolve)]

screen bonfireGallery:
    add "BGs/bg bonfire.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('menuGallery'), Hide("bonfireGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('campDayGallery'), Hide("bonfireGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("bonfireGallery"), Function(renpy.transition, dissolve)]

screen campDayGallery:
    add "BGs/bg campground-day.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('bonfireGallery'), Hide("campDayGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('campSunsetGallery'), Hide("campDayGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("campDayGallery"), Function(renpy.transition, dissolve)]

screen campSunsetGallery:
    add "BGs/bg campground-sunset.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('campDayGallery'), Hide("campSunsetGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('campNightGallery'), Hide("campSunsetGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("campSunsetGallery"), Function(renpy.transition, dissolve)]

screen campNightGallery:
    add "BGs/bg campground-night.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('campSunsetGallery'), Hide("campNightGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('trunkGallery'), Hide("campNightGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("campNightGallery"), Function(renpy.transition, dissolve)]

screen trunkGallery:
    add "BGs/bg trunk.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('campNightGallery'), Hide("trunkGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('roadGallery'), Hide("trunkGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("trunkGallery"), Function(renpy.transition, dissolve)]

screen roadGallery:
    add "BGs/bg road.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('trunkGallery'), Hide("roadGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('kissGallery'), Hide("roadGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("roadGallery"), Function(renpy.transition, dissolve)]

screen kissGallery:
    add "CGs/cg campfire-kiss.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('roadGallery'), Hide("kissGallery")]

    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('passionGallery'), Hide("kissGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("kissGallery"), Function(renpy.transition, dissolve)]

screen passionGallery:
    add "CGs/cg campfire-hm.png"

    imagebutton:
        xalign 0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('kissGallery'), Hide("passionGallery")]

    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("passionGallery"), Function(renpy.transition, dissolve)]

################################################################################

#this is the first picture in the gallery. do not delete this block, just edit
#it to fit whatever the first picture is
screen shopPicture:

    modal True
    add "BGs/bg store.png" #this is where the image is located
    layer 'gallery' #the gallery layer is on top of everything else

    #there is no button to go to the left pic because this is the first picture
    #but it would be virtually the same as the one for the right except xalign 0

    #to go to the right pic
    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/right pic button empty.png"
        hover "phoneMenu/gallery/right pic button.png"
        action [Show('kissPicture'), Hide("shopPicture")]

    #to exit, make sure this block is written last so it is on top of everything
    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("shopPicture"), Function(renpy.transition, dissolve)]

################################################################################

#Pic 2
#do not delete this block, just edit it to fit whatever the first picture is
screen kissPicture:

    modal True
    add "CGs/cg campfire-kiss.png" #this is where the image is located
    layer 'gallery' #the gallery layer is on top of everything else

    #to go to the right pic
    if persistent.passionPic:
        imagebutton:
            xalign 1.0
            idle "phoneMenu/gallery/right pic button empty.png"
            hover "phoneMenu/gallery/right pic button.png"
            action [ShowMenu('passionPicture'), Hide("kissPicture")]

    #to exit, make sure this block is written last so it is on top of everything
    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("kissPicture"), Function(renpy.transition, dissolve)]

################################################################################

#Pic 3
#do not delete this block, just edit it to fit whatever the first picture is
screen passionPicture:

    modal True
    #add "CGs/campfire-passion.png" #use the imagemap instead for the hm
    imagemap:
        idle "CGs/cg campfire-passion.png"
        hover "CGs/cg campfire-passion.png"
        ground "CGs/cg campfire-passion.png"
        if hm1 == True:
            if hm2 == True:
                hotspot (36, 114, 52, 92) action [Jump('hmmm'), Hide('gallery'), Hide('phoneMenu')]
            else:
                hotspot (36, 114, 52, 92) action [Show("hmPicture", transition=Dissolve(3.0)), SetVariable('hm3', True)]
        else:
            hotspot (36, 114, 52, 92) action [Show("hmPicture", transition=Dissolve(3.0)), SetVariable('hm3', True)]
    layer 'gallery' #the gallery layer is on top of everything else

    #to go to the left pic
    if persistent.kissPic:
        imagebutton:
            xalign 0
            idle "phoneMenu/gallery/left pic button empty.png"
            hover "phoneMenu/gallery/left pic button.png"
            action [Show('kissPicture'), Hide("passionPicture")]

    #to go to the right pic
    #imagebutton:
        #xalign 1.0
        #idle "gallery/right pic button empty.png"
        #hover "gallery/right pic button.png"
        #action ShowMenu('passionPicture')
        #action Hide("kissPicture")

    #to exit, make sure this block is written last so it is on top of everything
    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("passionPicture"), Function(renpy.transition, dissolve)]

screen hmPicture:

    modal True
    add "CGs/cg campfire-passion.png" #use the imagemap instead for the hm
    layer 'gallery' #the gallery layer is on top of everything else

    #to go to the left pic
    imagebutton:
        xalign 1.0
        idle "phoneMenu/gallery/left pic button empty.png"
        hover "phoneMenu/gallery/left pic button.png"
        action [Show('kissPicture'), Hide("passionPicture")]

    #to go to the right pic
    #imagebutton:
        #xalign 1.0
        #idle "gallery/right pic button empty.png"
        #hover "gallery/right pic button.png"
        #action ShowMenu('passionPicture')
        #action Hide("kissPicture")

    #to exit, make sure this block is written last so it is on top of everything
    imagebutton:
        xalign 0.5 yalign 0.98
        idle "phoneMenu/gallery/gallery exit button half invis.png"
        hover "phoneMenu/gallery/gallery exit button.png"
        action [Hide("passionPicture"), Function(renpy.transition, dissolve)]

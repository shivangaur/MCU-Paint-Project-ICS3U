#MCUPaintProject--ShivanGaur.py
from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter import filedialog
#Importing Modules
#--------------------------------------------------------------------------
root=Tk()
root.withdraw()
init()
size=width,height=1024,768
screen=display.set_mode(size)
#--------------------------------------------------------------------------
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
#Setting variables to basic colours
#--------------------------------------------------------------------------
#####initislize ALL variables
col=BLACK#The default starting colour for the paint program
colPrev=WHITE#The default canvas colour. This is the colour used on the
#background preview screen for coloured backgrounds
thick='select a tool'#The default starting thickness
oldThick=thick
mult=1#The multiplier for the size tool of the stamps
count=0
pos=0
deg=0
flipPos=0#Variable for position of the flip tool for the stamps
fillPos=0#Varaivle for the position of the different canvas filters
#--------------------------------------------------------------------------
###Defining thicknesses
rectThick=1
penThick=1#The thickness for the pencil starting at 1
brushThick=lineThick=circleThick=polyThick=arcThick=recThick=eraserThick=sprayThick=crayThick=highThick=10
#--------------------------------------------------------------------------
####Restrictive Variables
tool="no tool"#The default tool setting on start up
stamps='not active'#The default setting for the hero stamps since they are not active
villStamps='not active'#The default setting for the villian stamps since they are not active
cond='not done'
reset='on'#Variable which resets the screen back to starting position. Since nothing
#has been loaded yet it needs to be on.
refresh='off'#Variable to refresh the stamp menu so when a stamp is selected
#it does not stay selected when the mouse moves
villRefresh='off'#Villian stamps are different than hero stamps so it has a
#different refresh variable
fill='none'
locked=2
shape='not made'
release='off'
paste='off'#Variable for the paste tool
passed='off'
go='off'
lock='off'
mus='on'
cl='off'
selected='off'#Variable for the select tool which is used in all tools which
#require select (cut,copy,paste,crop)
prev='none'#Variable for when the cut tool is used and then paste is used.
#When cut is used prev becomes prev='cut'
backCol='off'
colChose='off'
first='on'
bType='Coloured'#Variable for what the background type is. It starts as white
#so it is coloured
circ='not done'
drop='not dropped'
beg='on'
rotFirst='on'
stampCond='not done'
takeShot='off'
szShot='not done'
act='not now'
canv='off'
special='off'
picOn='none'
rotr='done'
flipType='none'
stop='off'
d3='off'
colTake='off'
undoTake='off'
line1='No tool selected'#Text for each tool. Since no tool is selected at the
line2=line3=line4=''#beginning the default is 'No tool selected'
#--------------------------------------------------------------------------
#####Empty Lists
undoShots=[]#Empty list for undo screenshots
redoShots=[]#empty list for redo screenshots
stampShots=[]#List for when the stamp menu is opened up. After the user selects
#a stamp or selects X, they should return to the exact same screen they left.
#If a list is not used, then since the program runs very fast when the mouse
#is clicked even once the program runs through the loop several times and updates
#the stampShot variable. So a list is used
polyShots=[]#Same reasoning behind this empty list.Used for the screenshots of
#the polygon tool
polyMadeShots=[]
screenShots=[]
shots=[]#
befShots=[]#List for screenshot of the canvas before the select tool was used on it
points=[]#List for the polygon tool to append all the points of the polygon
eyeShots=[]#List for the eye dropper tool
rotShots=[]
stampPoints=[]
sizeBackShots=[]
crayPoints=[]
queue=[]
checkPoints=[]
checkedPoints=[]
rList=[]#Lists for the rgb values of each pixel when the filters are used
gList=[]
bList=[]

#--------------------------------------------------------------------------
######load ALL images BEFORE the 'while running' loop

##Thumbnail Images
mcuLogo=image.load('images/mcuLogo.png')
palPic=image.load('images/colPal.png')
background=image.load('images/background.jpg')
pencilPic=image.load('images/pencilPic.jpg')
eraserPic=image.load('images/eraserPic.jpg')
circlePic=image.load('images/circle.jpg')
clearAll=image.load('images/clearAll.jpg')
whitePic=image.load('images/white.png')
rectangle=image.load('images/rectangle.png')
line=image.load('images/line.png')
sprayPaintPic=image.load('images/sprayPaintPic.jpg')
avengersLogo=image.load('images/avengerslogo.jpg')
villiansLogo=image.load('images/villiansLogo.png')
cross=image.load('images/cross.png')
undo=image.load('images/undo.png')
redo=image.load('images/redo.png')
filledPic=image.load('images/filledPic.png')
unfilledPic=image.load('images/unfilledPic.jpg')
ellipsePic=image.load('images/ellipsePic.png')
copyPic=image.load('images/copyPic.png')
pastePic=image.load('images/pastePic.jpg')
cutPic=image.load('images/cutPic.jpg')
cropPic=image.load('images/cropPic.png')
highlighterPic=image.load('images/highlighterPic.png')
textPic=image.load('images/textPic.jpg')
polygonPic=image.load('images/polygonPic.png')
brushPic=image.load('images/brushPic.jpg')
selPic=image.load('images/selPic.png')
eyeDropperPic=image.load('images/eyeDropperPic.png')
eyeDropperIcon=image.load('images/eyeDropperIcon.png')
rotatePic=image.load('images/rotate.png')
flipPic=image.load('images/flip.jpg')
savePic=image.load('images/savePic.png')
loadPic=image.load('images/loadPic.png')
crayonPic=image.load('images/crayonPic.jpg')
floodPic=image.load('images/floodPic.png')
pic3d=image.load('images/3dPic.jpg')
buttonsPic=image.load('images/buttonsPic.jpg')
titlePic=image.load('images/titlePic.png')
#--------------------------------------------------------------------------
#####Stamp Image
stampsImages=[('images/antMan.png'),('images/spiderMan.png'),('images/blackPanther.png'),('images/cap.png'),('images/gamora.png'),('images/groot.png'),('images/rocket Racoon.png'),('images/scarletWitch.png'),('images/thor.png'),('images/falcon.png'),('images/starLord.png'),('images/winterSoldier.png'),('images/vision.png'),('images/drStrange.png'),('images/hawkeye.png'),('images/drax.png'),('images/nickFury.png'),('images/hulk.png'),('images/captainMarvel.png'),('images/blackWidow.png'),('images/wasp.png'),('images/nebula.png'),('images/ironMan.png'),('images/warMachine.png')]
#A list of all the hero stamps and then a for loop to shorten the amount of lines
stampsList=[]
for i in stampsImages:
    j=image.load(i)
    stampsList.append(j)
    #Appending each loading image into the list of stamps
    
##Same process except with the villian stamps
villImages=[('images/thanos.png'),('images/cullObsidian.png'),('images/corvusGlaive.png'),('images/ironMonger.png'),('images/proximaMidnight.png'),('images/ebonyMaw.png'),('images/whiplash.png'),('images/mandarin.png'),('images/killmonger.png'),('images/loki.png'),('images/malekith.png'),('images/hela.png'),('images/mordo.png'),('images/dormammu.png'),('images/ronan.png'),('images/redSkull.png'),('images/crossbones.png'),('images/ultron.png'),('images/yellowJacket.png'),('images/vulture.png'),('images/abomination.png'),('images/skrull.png'),('images/ghost.png'),('images/baron zemo.png')] 
villStampsList=[]
for i in villImages:
    x=image.load(i)
    villStampsList.append(x)
    
####Backgrouds
    ##Same process as before except with the different backgrounds
backgroundsList=['backgrounds/avengersWall.jpg','backgrounds/gotgWall.jpeg','backgrounds/blackOrderWall.jpg','backgrounds/blackPantherWall.jpg','backgrounds/capMarvelWall.jpg','backgrounds/civilWarWall.jpg','backgrounds/falconWall.jpg','backgrounds/heroesVsVilliansWall.jpg','backgrounds/hulkWall.jpg','backgrounds/infinityWarWall.jpg','backgrounds/ironManWall.jpg','backgrounds/killMongerWall.jpg','backgrounds/lokiWall.jpg','backgrounds/lordOfThunder.jpg','backgrounds/mandarinWall.jpg','backgrounds/spiderManIronManWall.jpg','backgrounds/strangeWall.jpg','backgrounds/studiosWall.jpg','backgrounds/ultronBotsWall.jpg','backgrounds/ultronWall.jpg','backgrounds/unbreakableShield.jpg','backgrounds/villiansWall.jpg','backgrounds/capFlagWall.png','backgrounds/capWall.png','backgrounds/hammerWall.png','backgrounds/shieldWall.png','backgrounds/spiderWall.png']
textures=[]
for b in backgroundsList:
    preview=image.load(b)
    textures.append(preview)


    
#--------------------------------------------------------------------------             
#####loading music
#The default starting music is always the avengers theme
mixer.music.load('Music/theAvengers.mp3')
#List of all the music themes for each hero and villian stamp
music=['Music/antManTheme.mp3','Music/spiderManTheme.mp3','Music/blackPantherTheme.mp3','Music/capTheme.mp3','Music/gotgTheme.mp3','Music/gotgTheme.mp3', 'Music/gotgTheme.mp3','Music/scarletWitchTheme.mp3','Music/thorTheme.mp3','Music/falconTheme.mp3','Music/gotgTheme.mp3','Music/winterSoldierTheme.mp3','Music/visionTheme.mp3','Music/drStrangeTheme.mp3','Music/hawkeyeTheme.mp3','Music/gotgTheme.mp3','Music/agentsOfShieldTheme.mp3','Music/hulkTheme.mp3','Music/captainMarvelTheme.mp3','Music/blackWidowTheme.mp3','Music/waspTheme.mp3','Music/nebulaTheme.mp3','Music/ironManTheme.mp3','Music/warMachineTheme.mp3']                         
villMusic=[('Music/thanosTheme.mp3'),('Music/thanosTheme.mp3'),('Music/thanosTheme.mp3'),('Music/ironMongerTheme.mp3'),('Music/thanosTheme.mp3'),('Music/thanosTheme.mp3'),('Music/whiplashTheme.mp3'),('Music/mandarinTheme.mp3'),('Music/killmongerTheme.mp3'),('Music/lokiTheme.mp3'),('Music/malekithTheme.mp3'),('Music/helaTheme.mp3'),('Music/mordoTheme.mp3'),('Music/dormammuTheme.mp3'),('Music/ronanTheme.mp3'),('Music/redSkullTheme.mp3'),('Music/crossbonesTheme.mp3'),('Music/ultronTheme.mp3'),('Music/yellowJacketTheme.mp3'),('Music/vultureTheme.mp3'),('Music/vultureTheme.mp3'),('Music/vultureTheme.mp3'),('Music/ghostTheme.mp3'),('Music/ghostTheme.mp3')]
#List of all background music besides the hero and villian stamps
backgroundMusic=['Music/theAvengers.mp3','Music/theme1.mp3','Music/theme2.mp3', 'Music/theme3.mp3', 'Music/theme4.mp3', 'Music/theme5.mp3', 'Music/theme6.mp3', 'Music/theme7.mp3', 'Music/theme8.mp3', 'Music/theme9.mp3',]
cop1=music[:]
cop2=villMusic[:]
cop3=backgroundMusic[:]
#Copying all 3 music lists and adding them to a final playlist which music will
#be played from once the avengers theme stops
playList=cop3+cop2+cop1
musPos=0
#--------------------------------------------------------------------------
#####defining all RECTS
colPalRect=Rect(808,280,220,30)
pencilRect=Rect(20,80,40,40)
eraserRect=Rect(80,80,40,40)
brushRect=Rect(20,130,40,40)
eyeDropperRect=Rect(80,130,40,40)
somethingRect=Rect(80,130,40,40)
circleRect=Rect(20,180,40,40)
ellipseRect=Rect(80,180,40,40)
linesRect=Rect(20,230,40,40)
eraseAllRect=Rect(20,280,40,40)
stampsRect=Rect(20,330,40,40)
rectRect=Rect(80,230,40,40)
crossRect=Rect(950,113,35,35)
undoRect=Rect(0,0,48,48)
redoRect=Rect(48,0,48,48)
unfilledRect=Rect(45,600,60,60)
filledRect=Rect(45,670,60,60)
sprayPaintRect=Rect(80,280,40,40)
selRect=Rect(80,330,40,40)
copyRect=Rect(80,380,40,40)
pasteRect=Rect(80,430,40,40)
villStampsRect=Rect(20,380,40,40)
highlighterRect=Rect(20,430,40,40)
polygonRect=Rect(135,670,60,60)
cropRect=Rect(20,480,40,40)
cutRect=Rect(80,480,40,40)
backgroundPreview=Rect(808,350,65,65)
colourPreview=Rect(880,350,65,65)
filterRect=Rect(955,350,65,65)
specialTools=Rect(230,620,560,130)
rotateRect=Rect(255,645,70,70)
flipRect=Rect(360,645,70,70)
sizeRect=Rect(445,702,335,16)
infoRect=Rect(795,450,227,310)
loadRect=Rect(850,10,60,60)
saveRect=Rect(950,10,60,60)
crayonRect=Rect(20,530,40,40)
floodFill=Rect(80,530,40,40)
rect3d=Rect(135,600,60,60)
pauseRect=Rect(800,715,40,40)
stopRect=Rect(845,715,40,40)
playRect=Rect(890,715,40,40)
nextRect=Rect(935,715,40,40)
preRect=Rect(980,715,40,40)
buttonsRect=Rect(798,715,222,43)

canvasRect=Rect(135,80,655,500)
palRect=Rect(808,75,220,206)
stampRect=Rect(90,120,880,500)

#A list of 24 rects which the hero or villian stamps will be set on to
picRects=[    
Rect(90,120,127,163),
Rect(212,120,109,163),
Rect(316,120,109,163),
Rect(419,120,130,163),
Rect(550,120,100,163),
Rect(645,120,78,163),
Rect(718,120,132,163),
Rect(845,120,127,163),

Rect(90,283,127,167),
Rect(212,283,109,167),
Rect(316,283,109,167),
Rect(419,283,130,167),
Rect(550,283,100,167),
Rect(645,283,78,167),
Rect(715,283,137,167),
Rect(845,283,127,167),

Rect(90,450,127,170),
Rect(212,450,109,170),
Rect(316,450,109,170),
Rect(419,450,130,170),
Rect(550,450,100,170),
Rect(645,450,78,170),
Rect(715,450,137,170),
Rect(845,450,127,170)]
#--------------------------------------------------------------------------
###Tool names for stamp tools
toolStampNames=['ant man stamp','spider man stamp','black panther stamp','cap stamp','gamora stamp','groot stamp','rocket raccoon stamp','scarlet witch stamp','thor stamp','falcon stamp','star lord stamp','winter soldier stamp','vision stamp','dr strange stamp','hawkeye stamp','drax stamp','nick fury stamp','hulk stamp','captain marvel stamp','black widow stamp','wasp stamp','nebula stamp','iron man stamp','war machine stamp']
villToolStampNames=['thanos stamp','cull obsidian stamp','corvus glaive stamp','iron monger stamp','proxima midnight stamp','ebony maw stamp','whiplash stamp','mandarin stamp','killmonger stamp','loki stamp','malekith stamp','hela stamp','mordo stamp','dormammu stamp','ronan stamp','red skull stamp','crossbones stamp','ultron stamp','yellow jacket stamp','vulture stamp','abomination stamp','skrull','ghost stamp','baron zemo stamp'] 

###Stamp 'blit' coordiantes for stamp menu
stampBlits=[(90,120),(210,125),(310,125),(425,130),(550,130),(645,130),(725,130),(850,125),(90,295),(219,295),(325,295),(430,295),(535,293),(625,290),(725,295),(850,295),(100,460),(220,460),(340,460),(404,460),(550,460),(660,460),(725,460),(835,460)]
villStampBlits=[(105,123),(215,123),(315,120),(420,127),(550,123),(650,123),(715,120),(855,124),(100,290),(210,290),(330,290),(435,290),(545,290),(645,290),(725,290),(850,290),(100,465),(200,465),(315,460),(420,465),(550,460),(650,470),(725,460),(835,460)]  
#--------------------------------------------------------------------------
#Fonts
font.init()
comicFont=font.SysFont("Comic Sans MS",16)
##timesFont=font.SysFont("Times New Roman",40)
##calibriFont=font.SysFont("Calibri",40)
##arialFont=font.SysFont("Arial",40)
##helvFont=font.SysFont("Helvetica",40)
##courierFont=font.SysFont('Courier',40)
##verdanaFont=font.SysFont('Verdana',40)
##tahomaFont=font.SysFont('Tahoma',40)
#--------------------------------------------------------------------------
#Flip Pic list
flipPics=[(True,False),(False,True),(True,True)]
#--------------------------------------------------------------------------
###Beginning of the while running loop 

running=True
while running:
    click=False#When the mouse is held down no other tool can be selected
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            
            
            
        
            #if not undoRect.collidepoint(mx,my) and not redoRect.collidepoint(mx,my):
                #screenShot=screen.copy()
                #undoShots.append(screenShot)
            if evt.button==1:
                un='off'
                click=True
                if colourPreview.collidepoint(mx,my):
                    screenShot=screen.copy()
                    undoShots.append(screenShot)  
                if backgroundPreview.collidepoint(mx,my):
                    screenShot=screen.copy()
                    undoShots.append(screenShot)
                    backTake='on'
                if canvasRect.collidepoint(mx,my):
                    sx,sy=mouse.get_pos()
                    screenShot=screen.copy()
                    if not (stamps=='active' or villStamps=='active'):
                        canvasShot=screen.subsurface(canvasRect).copy()
                        undoShots.append(screenShot)
                        undoTake='on'
                    else:
                        canvasShot=screen.subsurface(0,0,0,0).copy()
                if preRect.collidepoint(mx,my):
                    if musPos>=1:
                        musPos-=1
                if nextRect.collidepoint(mx,my):
                    if musPos<=58:
                        musPos+=1
                if len(undoShots)>1:
                    if undoRect.collidepoint(mx,my):
                        tool='no tool'
                        screen.blit(undoShots[-2],(0,0))
                        u=undoShots.pop()
                        redoShots.append(u)
                        #redoShots.append(undoShots[-1])
                        #del undoShots[-1]
                        print("u",len(undoShots),len(redoShots))
                if len(redoShots)>0:
                    if redoRect.collidepoint(mx,my):
                        tool='no tool'
                        screen.blit(redoShots[-1],(0,0))
                        u=redoShots.pop()
                        undoShots.append(u)
                        #undoShots.append(redoShots[-1])
                        #del redoShots[-1]
                        print('r',len(undoShots),len(redoShots))
            if evt.button==4:
                if filterRect.collidepoint(mx,my):
                    fillPos=(fillPos+1)%9
                if flipRect.collidepoint(mx,my):
                    flipPos=(flipPos+1)%3
                if rotateRect.collidepoint(mx,my) and deg<360:
                    deg+=5
                    #canvasShot=screen.subsurface(canvasRect).copy()
                if backgroundPreview.collidepoint(mx,my):
                    pos=(pos+1)%27
                
                if canvasRect.collidepoint(mx,my) and thick<50:
                    #changing thicknesses for diffent tools
                    if tool=='pencil':
                        if penThick<5:
                            penThick+=1
                    elif tool=='eraser':
                        if eraserThick<50:
                            eraserThick+=1
                    elif tool=='brush':
                        if brushThick<50:
                            brushThick+=1
                    elif tool=='circle':
                        if circleThick<50:
                            circleThick+=1
                    elif tool=='ellipse':
                    
                        if arcThick<50:
                            arcThick+=1
                    elif tool=='lines':
                        if lineThick<50:
                            lineThick+=1
                    elif tool=='rectangle':
                        if recThick<50:
                            recThick+=1
                    elif tool=='spray paint':
                        if sprayThick<50:
                            sprayThick+=1
                    elif tool=='highlighter':
                        if highThick<45:
                            highThick+=1
                    elif tool=='crayon':
                        if crayThick<40:
                            crayThick+=1
                    #thick+=1
                    #brushThick+=1
            if evt.button==5:
                if filterRect.collidepoint(mx,my):
                    fillPos=(fillPos-1)%9
                if flipRect.collidepoint(mx,my):
                    flipPos=(flipPos-1)%3
                if rotateRect.collidepoint(mx,my) and deg>0:
                    deg-=5
                    #canvasShot=screen.subsurface(canvasRect).copy()
                if backgroundPreview.collidepoint(mx,my):
                    pos=(pos-1)%27
                if canvasRect.collidepoint(mx,my):
                    if tool=='pencil':
                        if penThick>1:
                            penThick-=1
                    elif tool=='eraser':
                        if eraserThick>1:
                            eraserThick-=1
                    elif tool=='brush':
                        if brushThick>1:
                            brushThick-=1
                    elif tool=='circle':
                        if circleThick>1:
                            circleThick-=1
                    elif tool=='ellipse':
                        if arcThick>1:
                            arcThick-=1
                    elif tool=='lines':
                        if lineThick>1:
                            lineThick-=1
                    elif tool=='rectangle':
                        if recThick>1:
                            recThick-=1
                    elif tool=='spray paint':
                        if sprayThick>1:
                            sprayThick-=1
                    elif tool=='highlighter':
                        if highThick>1:
                            highThick-=1
                    elif tool=='crayon':
                        if crayThick>1:
                            crayThick-=1
        if evt.type==MOUSEBUTTONUP:
            '''
            if backgroundPreview.collidepoint(mx,my):
                if undoTake=='on':
                    screenShot=screen.copy()
                    undoShots.append(screenShot)
                    undoTake='off'
            '''
            if undoTake=='on':
                screenShot=screen.copy()
                if len(undoShots)>1:
                    del undoShots[-1]
                    
                undoShots.append(screenShot)
                undoTake='off'
    mx,my=mouse.get_pos()#Mouse position
    if canvasRect.collidepoint(mx,my):
        mz=(mx,my)#1 variable for both mouse coordinates for the info text box
    else:
        mz='Not on canvas'
    mb=mouse.get_pressed()#mouse getting pressed
    #screen reset
    if reset=='on':#Resets the entire screen whenever reset=='on'
        screen.blit(background,(0,0))
        screen.blit(palPic,(808,75))
        screen.blit(pencilPic,(22,80))
        screen.blit(eraserPic,(80,80))
        screen.blit(circlePic,(20,180))
        screen.blit(clearAll,(20,280))
        screen.blit(pic3d,(135,600))
        screen.blit(rectangle,(80,230))

        screen.blit(line,(20,230))
        screen.blit(titlePic,(230,3))
        screen.blit(sprayPaintPic,(80,280))
        screen.blit(avengersLogo,(20,330))
        screen.blit(avengersLogo,(20,380))
        screen.blit(villiansLogo,(20,380))
        screen.blit(undo,(0,0))
        screen.blit(redo,(48,0))
        #screen.blit(mcuLogo,(500,0))
        screen.blit(filledPic,(45,670))
        screen.blit(unfilledPic,(45,600))
        screen.blit(ellipsePic,(80,180))
        screen.blit(copyPic,(80,380))
        screen.blit(whitePic,(80,430))
        screen.blit(pastePic,(87,432))
        screen.blit(cutPic,(80,480))
        screen.blit(savePic,(950,10))
        screen.blit(loadPic,(850,10))
        screen.blit(cropPic,(20,480))
        screen.blit(highlighterPic,(20,430))
        screen.blit(brushPic,(20,130))
        screen.blit(polygonPic,(135,670))
        screen.blit(selPic,(80,330))
        screen.blit(eyeDropperPic,(80,130))
        screen.blit(crayonPic,(20,530))
        screen.blit(floodPic,(80,530))
        #blitting the thumnails at the beginning 
        draw.rect(screen,colPrev,canvasRect)
        specialShot=screen.subsurface(225,615,570,140).copy()
        if len(sizeBackShots)<1:
            sizeBackShots.append(specialShot)
        if bType=='image':
            subBack=transform.scale(textures[bPos],(655,500))
            screen.blit(subBack,(135,80))
        draw.rect(screen,BLACK,(132,76,661,507),5)
        if mus=='off' and cl=='off':
            screen.blit(stampShots[0],(135,80))
            stampShots=[]
        cl='off'
        beg='on'
        mixer.music.stop()#stopping any music which was orginally playing
        stampPoints=[]
        shape='not made'
        points=[]
        reset='off'
        stamps='not active'
        special='off'
        canvasShot=screen.subsurface(canvasRect).copy()
    if mus=='on':#If mus=='on' then he program is opening for the first time
        mixer.music.load('Music/theAvengers.mp3')#so the avengers theme must
        mixer.music.play(1)#play once
        mus='off'
    
    
        
                        
#####Background preview screen
    sub=transform.scale(textures[pos],(65,65))#taking the position of the textures
    #list and scaling whichever background that is to 65 by 65 anf blitting it on
    #the preview screen
    screen.blit(sub,(808,350))
    
    draw.rect(screen,colPrev,colourPreview)#drawing the colour of the COLOURED
    #background preview screen 
    
    #changing the background
    if not colourPreview.collidepoint(mx,my):
        first='on'
        
    if backgroundPreview.collidepoint(mx,my):#
        if mb[0]==1 and click:
            subBack=transform.scale(textures[pos],(655,500))#scale the image
            #to be the same size as the canvas and blits it on the canvas
            screen.blit(subBack,(135,80))
            if backTake=='on':
                screenShot=screen.copy()
                undoShots.append(screenShot)
                backTake='off'
            tool='no tool'#reseting the tool to no tool
            bPos=pos#making another position variable used later in the copy
            #and paste tool
            bType='image'#changing the background type to image
    if colourPreview.collidepoint(mx,my) and first=='on':
        if mb[0]==1:
            backCol='on'
            
    
    ###draw ALL rects
    draw.rect(screen,col,colPalRect)
    draw.rect(screen,BLACK,colPalRect,2)
    
    draw.rect(screen,BLACK,pencilRect,2)
    draw.rect(screen,BLACK,eraserRect,2)
    draw.rect(screen,BLACK,circleRect,2)
    draw.rect(screen,BLACK,rectRect,2)
    draw.rect(screen,BLACK,linesRect,2)
    draw.rect(screen,BLACK,stampsRect,2)
    draw.rect(screen,BLACK,eraseAllRect,2)
    draw.rect(screen,BLACK,linesRect,2)
    draw.rect(screen,BLACK,ellipseRect,2)
    draw.rect(screen,BLACK,villStampsRect,2)
    draw.rect(screen,BLACK,sprayPaintRect,2)
    draw.rect(screen,BLACK,undoRect,2)
    draw.rect(screen,BLACK,redoRect,2)
    draw.rect(screen,BLACK,unfilledRect,2)
    draw.rect(screen,BLACK,filledRect,2)
    draw.rect(screen,BLACK,copyRect,locked)
    draw.rect(screen,BLACK,pasteRect,locked)
    draw.rect(screen,BLACK,cutRect,locked)
    draw.rect(screen,BLACK,cropRect,locked)
    draw.rect(screen,BLACK,highlighterRect,2)
    draw.rect(screen,BLACK,selRect,2)
    draw.rect(screen,BLACK,polygonRect,2)
    draw.rect(screen,BLACK,brushRect,2)
    draw.rect(screen,BLACK,eyeDropperRect,2)
    draw.rect(screen,BLACK,backgroundPreview,2)
    draw.rect(screen,BLACK,colourPreview,2)
    draw.rect(screen,(113,187,255),infoRect)
    draw.rect(screen,BLACK,infoRect,4)
    draw.rect(screen,BLACK,loadRect,2)
    draw.rect(screen,BLACK,saveRect,2)
    draw.rect(screen,BLACK,crayonRect,2)
    draw.rect(screen,BLACK,floodFill,2)
    draw.rect(screen,RED,filterRect,2)
    draw.rect(screen,BLACK,filterRect)
    
    draw.rect(screen,BLACK,rect3d,2)
    ####Information box
    txtTool=comicFont.render('Tool: '+tool,True,BLACK)#Displaying which tool
    #is being used currently
    screen.blit(txtTool,(802,450))
    txtCol=comicFont.render('Colour: '+str(col[:-1]),True,BLACK)#Displaying the
    #current rgb colour value 
    screen.blit(txtCol,(802,472))
    txtBackground=comicFont.render('Background: '+bType,True,BLACK)#Displaying
    #the background type(image or coloured)
    screen.blit(txtBackground,(802,495))
    txtThick=comicFont.render('Thickness: '+str(thick),True,BLACK)#displaying
    #the thickness
    screen.blit(txtThick,(802,518))
    txtSize=comicFont.render('Image Size: x'+str(round(mult,2)),True,BLACK)
    #displaying the image multiplier of the size tool
    txtDeg=comicFont.render('Rotation: '+str(deg)+'°',True,BLACK)#displaying
    #the degrees of rotation of the rotate tool
    txtFlip=comicFont.render('Flip :'+flipType,True,BLACK)#displaying the type
    #of reflection
    txtMouse=comicFont.render('Mouse Position: '+str(mz),True,BLACK)
    #displaying the mouse position if it is on the canvas
    screen.blit(txtMouse,(802,540))
    txtDetails=comicFont.render('Tool Description:',True,BLACK)
    screen.blit(txtDetails,(802,565))
    txtLine1=comicFont.render(line1,True,RED)#the tool descriptions for each
    txtLine2=comicFont.render(line2,True,RED)#tool
    txtLine3=comicFont.render(line3,True,RED)
    txtLine4=comicFont.render(line4,True,RED)
    screen.blit(txtLine1,(802,590))#blitting the tool descriptions on the info
    screen.blit(txtLine2,(802,615))#box
    screen.blit(txtLine3,(802,640))
    screen.blit(txtLine4,(802,665))
    ####Music Controls
    screen.blit(buttonsPic,(800,715))
    draw.rect(screen,BLACK,buttonsRect,2)
    if mb[0]==1:
        if pauseRect.collidepoint(mx,my):
            mixer.music.pause()#Pausing the music being played
        if playRect.collidepoint(mx,my):
            mixer.music.play()#playing the music
        if stopRect.collidepoint(mx,my):
            mixer.music.stop()#stopping the music
        if nextRect.collidepoint(mx,my):
            mixer.music.stop()#stopping the music and then skipping to the next 
            mixer.music.load(playList[musPos])#song in the playlist 
            mixer.music.play(-1)#playing that song until the user changes it
        if preRect.collidepoint(mx,my):
            mixer.music.stop()#stopping the music and skipping to the previous
            mixer.music.load(playList[musPos])#song in the playlist
            mixer.music.play(-1)
    ####selecting the tool and changing thick variable to tool thickness
    if mb[0]==1 and click:
         if pencilRect.collidepoint(mx,my):
            tool="pencil"
            thick=penThick
         elif eraserRect.collidepoint(mx,my):
             tool="eraser"
             thick=eraserThick
         elif rectRect.collidepoint(mx,my):
             tool='rectangle'
             thick=recThick
         elif linesRect.collidepoint(mx,my):
             tool='lines'
             thick=lineThick
         elif circleRect.collidepoint(mx,my):
             tool='circle'
             thick=circleThick
         elif eraseAllRect.collidepoint(mx,my):
             tool='erase all'
         elif ellipseRect.collidepoint(mx,my):
             tool='ellipse'
             thick=arcThick
         elif sprayPaintRect.collidepoint(mx,my):
             tool='spray paint'
             thick=sprayThick
         elif filledRect.collidepoint(mx,my):
             fill='filled'
             
         elif unfilledRect.collidepoint(mx,my):
             fill='unfilled'
             
         elif copyRect.collidepoint(mx,my):
             tool='copy'
             paste='off'
             
         elif cutRect.collidepoint(mx,my):
             tool='cut'
             
         elif polygonRect.collidepoint(mx,my):
             polyShots=[]#empyting the polygon screenshots when the tool
             #is selected 
             points=[]#emptying the list of previous points
             thick=polyThick
             tool='polygon'
             
         elif selRect.collidepoint(mx,my):
             tool='select'
             
         elif highlighterRect.collidepoint(mx,my):
             tool='highlighter'
             thick=highThick
         elif cropRect.collidepoint(mx,my):
             tool='crop'
            
         elif brushRect.collidepoint(mx,my):
             tool='brush'
             thick=brushThick
         elif eyeDropperRect.collidepoint(mx,my):
             tool='eye dropper'
             eyeShots=[]#clearing the list
             eShot=screen.subsurface(canvasRect).copy()
             if len(eyeShots)<1:#making sure there is only one screenShot
                 #in the list
                 eyeShots.append(eShot)
             
         elif stampsRect.collidepoint(mx,my):
             tool='stamps'
         elif villStampsRect.collidepoint(mx,my):
             tool='vill stamps'
         elif crayonRect.collidepoint(mx,my):
             tool='crayon'
             thick=crayThick
         elif floodFill.collidepoint(mx,my):
             tool='flood fill'
#####Changing thickness for tools
    if tool=='pencil':
        thick=penThick
    if tool=='eraser':
        thick=eraserThick
    if tool=='rectangle':
        thick=recThick
    if tool=='lines':
        thick=lineThick
    if tool=='circle':
        thick=circleThick
    if tool=='ellipse':
        thick=arcThick
    if tool=='spray paint':
        thick=sprayThick
    if tool=='polygon':
        thick=polyThick
    if tool=='highlighter':
        thick=highThick
    if tool=='brush':
        thick=brushThick
    if tool=='crayon':
        thick=crayThick
########using the tool
    
    ##Tools which are not used on canvas
    if mb[0]==1 and rect3d.collidepoint(mx,my):
        d3='on'#3D tool
        fill='none'
    if mb[0]==1 and filterRect.collidepoint(mx,my) and click:
        #using the filter tool to change the rgb value of every pixel on the
        #canvas depending on which filter the user chooses
        for x in range(135,canvasRect[2]+135):#the area of the canvas
            for y in range(80,canvasRect[3]+80):
                r,g,b,a=screen.get_at((x,y))
                rList=[(min(255,int(0.393*r+0.769*g+0.189*b))),(min(255,int(0.21*r + 0.72*g + 0.07*b))),(255-r),(min(255,int(0.4592*r + 0.8394739*g + 0.65*b))),b,b,g,g,(screen.get_at((x-1,y))[0]+screen.get_at((x+1,y))[0]+screen.get_at((x,y-1))[0]+screen.get_at((x,y+1))[0])//4]
                #list of r values for filters
                gList=[(min(255,int(0.349*r+0.686*g+0.168*b))),(min(255,int(0.21*r + 0.72*g + 0.07*b))),(255-g),(min(255,int(0.1442*r + 0.79434*g + 0.0432424*b))),r,g,b,r,(screen.get_at((x-1,y))[1]+screen.get_at((x+1,y))[1]+screen.get_at((x,y-1))[1]+screen.get_at((x,y+1))[1])//4] 
                #list of g values for filters
                bList=[(min(255,int(0.272*r+0.534*g+0.131*b))),(min(255,int(0.21*r + 0.72*g + 0.07*b))),(255-b),(min(255,int(0.31*r + 0.22*g + 0.17*b))),g,r,r,b,(screen.get_at((x-1,y))[2]+screen.get_at((x+1,y))[2]+screen.get_at((x,y-1))[2]+screen.get_at((x,y+1))[2])//4]                 
                #list of b values for filters
                r2=rList[fillPos]#the filter which was chosen has the rgb values
                #of that position
                g2=gList[fillPos]
                b2=bList[fillPos]                
              
                screen.set_at((x,y),(r2,g2,b2))#setting the 
    if loadRect.collidepoint(mx,my) and mb[0]==1 and click:
        #loading an image on to the canvas
        try:
            fname=filedialog.askopenfilename()#getting the filename of
            #the image
            if fname!='':#if the user clicks cancel then the file name is
                #an empty string 
                file=image.load(fname)#loading the actual image with
                #the file name
                newFile=transform.scale(file,(655,500))#scaling the image to be
                #the size of the canvas
                screen.blit(newFile,(135,80))#bliting the image on to the canvas       
        except:
            print('loading error')
    if saveRect.collidepoint(mx,my) and mb[0]==1 and click:
        #saving the canvas image onto your computer
        try:
            f=filedialog.asksaveasfilename(defaultextension='.png')#making a file
            #path with the default extension of png
            if f!='':#if the user clicks cancel the file path is an empty string
                image.save(screen.subsurface(canvasRect),f)#saving the image
                #to a place on the users computer
        except:
            print('saving error') 
            
    if tool not in toolStampNames and tool not in villToolStampNames:
        screen.blit(specialShot,(225,615))#blitting the section of the window
        #where the special stamp tools menu is when it is not being used 
        special='off'#turning off the special tools variable
    if tool=='erase all':
        cl='on'
        reset='on'#reseting the screen
        
        tool='no tool'#reseting the tool
        
    if fill=='unfilled':
        d3='off'
        draw.rect(screen,RED,unfilledRect,2)
        rectThick=1
    elif fill=='filled':
        d3='off'
        draw.rect(screen,RED,filledRect,2)
        circleThick=0
        polyThick=0
        rectThick=0
        #the shape tools get filled by having their thicknesses turn to 0
    if tool=='select' and release=='on':
        draw.rect(screen,BLUE,selectRect,3)
        release='off'
        #when the mouse is released the select rect turns blue to indicate
        #the area has been selected
    if pasteRect.collidepoint(mx,my) and mb[0]==1 and click:
        if tool!='copy':
            prev='cut'
            #when the paste tool is clicked right away, copy and paste get turned
            #on
        paste='on'
        tool='copy'

        
    if tool!='copy':#when the tool is not copy paste gets turned off
        paste='off'
        
    #when eye dropper is on canvas it changes the mouse to eye dropper
    if tool=='eye dropper' and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        eyeShot=screen.subsurface(canvasRect).copy()
        if len(eyeShots)<2:
            eyeShots.append(eyeShot)
        screen.blit(eyeShots[0],(135,80))
        screen.blit(eyeDropperIcon,(mx,my))
        mouse.set_visible(False)
        screen.set_clip(None)
        drop='dropped'
    if tool=='eye dropper' and not canvasRect.collidepoint(mx,my) and drop=='dropped':
        screen.blit(eyeShots[1],(135,80))#when the eyedropper isnt on the canvas then
        #the mouse turns back to a cursor
        drop='not dropped'
        mouse.set_visible(True)          
    if tool=='cut':
                if selected=='on':
                    draw.rect(screen,colPrev,selectRect,3)
                    copyShot=screen.subsurface(selectRect).copy()
                    if len(shots)<1:
                        shots.append(copyShot)
                    w=copyShot.get_width()
                    h=copyShot.get_height()
                    if bType=='Coloured':
                        draw.rect(screen,colPrev,selectRect)#replacing the cut
                        #area with a rect the same col as the background
                    else:
                        b=subBack.subsurface(selectRect[0]-138,selectRect[1]-88,selectRect[2]+6,selectRect[3]+9)
                        screen.blit(b,(selectRect[0]-3,selectRect[1]-8))
                        #replace the cut surface with the background
                    prev='cut'
    if tool=='crop':
                screen.set_clip(canvasRect)
                if selected=='on':
                    draw.rect(screen,colPrev,selectRect,3)
                    cropShot=screen.subsurface(selectRect[0]+4,selectRect[1]+4,selectRect[2]-8,selectRect[3]-8).copy()
                    if bType=='image':
                        screen.blit(subBack,(135,80))
                    
                    else:
                        draw.rect(screen,colPrev,canvasRect)
                    screen.blit(cropShot,(selectRect[0]+4,selectRect[1]+4))
                    #clearing everything except the selected area on the canvas
                    tool='no tool'
                screen.set_clip(None)
    if (tool in toolStampNames or tool in villToolStampNames) and special=='on':
        #if the special tools are on
        if rotFirst=='on':
            if tool in toolStampNames:
                q=toolStampNames.index(tool)
                curStamp=stampsList[q]#defining curstamp for every special
                #tool
            else:
                q=villToolStampNames.index(tool)
                curStamp=villStampsList[q]
            rotFirst=='off'
        
        if beg=='on':#these tools only get blitted once
            draw.rect(screen,WHITE,specialTools)
            draw.line(screen,BLACK,(445,710),(780,710),4)
            sizeShot=screen.subsurface(sizeRect).copy()
            draw.circle(screen,RED,(613,710),8)
            draw.rect(screen,BLACK,specialTools,4)
            screen.blit(rotatePic,(255,645))
            screen.blit(flipPic,(360,645))
            beg='off'
        draw.rect(screen,BLACK,rotateRect,2)
        draw.rect(screen,BLACK,flipRect,2)
        #drawing the rects for the special tools   
        draw.rect(screen,WHITE,(550,650,150,30))
        draw.rect(screen,WHITE,(240,720,370,25))
        screen.blit(txtSize,(550,650))
        screen.blit(txtDeg,(240,720))
        screen.blit(txtFlip,(370,720))
        screen.set_clip(canvasRect)
        
        if rotateRect.collidepoint(mx,my):
            draw.rect(screen,RED,rotateRect,2)
            screen.blit(canvasShot,(135,80))
            rotPic=transform.rotate(curStamp,deg)#rotating the stamp by however
            #many deg is equal to
            screen.blit(rotPic,(sx-w//2,sy))
            curStamp=rotPic
         #changing the flip position           
        if flipPos==0:
            flipType='Horizontal'
        elif flipPos==1:
            flipType='Vertical'
        elif flipPos==2:
            flipType='Horizontal & Vertical'
        
        if flipRect.collidepoint(mx,my):
            draw.rect(screen,RED,flipRect,2)
            if mb[0]==1:
                screen.blit(canvasShot,(135,80))
                fPic=transform.flip(curStamp,flipPics[flipPos][0],flipPics[flipPos][1])
                #flipping the stamp at the position of the flip list
                screen.blit(fPic,(sx,sy))
                curStamp=fPic
        screen.set_clip(None)      
        if sizeRect.collidepoint(mx,my):
            if mb[0]==1:
                screen.set_clip(sizeRect)
                screen.blit(sizeShot,(445,702))
                draw.circle(screen,RED,(mx,710),8)
                screen.set_clip(canvasRect)
                mult=(mx-613)//5#multiplier of how many times you increase image
                #size by
                if mult<0:
                    mult=1/abs(mult)#if mult is less than zero then you take the
                    #reciprical and abs value the denominator to get the image
                    #smaller
                if mult==0:
                    mult=1
                scaledPic=transform.scale(curStamp,(int(w*mult),int(h*mult)))
                screen.blit(canvasShot,(135,80))
                screen.blit(scaledPic,(sx-w//2,sy))
                curStamp=scaledPic

        
    if evt.type==MOUSEBUTTONUP:
        if stampCond=='done':
            if (mx-w//2,my-h//2) not in stampPoints and canvasRect.collidepoint(mx,my):
                stampPoints.append((mx-w//2,my-h//2))
                stampCond='not done'
                if len(stampPoints)>1:
                    special='on'
                    stampPoints=[]
        rotr='done'
    if tool=='polygon' and mb[2]==1:
        tool='no tool'
    ##Tools which are used on canvas
    if mb[0]==1:
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)#only the canvas can be 'updated'
            if tool=='pencil':
                draw.line(screen,col,(omx,omy),(mx,my),penThick)
                #drawing lines from previous mouse position to the new one so
                #it looks like a pencil tool
            if tool=='brush':
                dx=mx-omx#change in x
                dy=my-omy#change in y
                dist=int(sqrt(dx**2+dy**2))#distance from old mouse pos to new
                for i in range(1,dist+1):
                    dotX=int(omx+i*dx/dist)#every x cooridnate from old mouse pos
                    #to new mouse pos
                    dotY=int(omy+i*dy/dist)#every y coordinate from old mouse
                    #pos to new mouse pos
                    draw.circle(screen,col,(dotX,dotY),brushThick)#drawing circles
                    #to fill the entire distance covered
            if tool=='eraser':
                if bType=='image':#if the background is an image
                    try:
                        dx=mx-omx
                        dy=my-omy
                        dist=int(sqrt(dx**2+dy**2))#distance formula
                        for i in range(1,dist+1):
                            dotX=int(omx+i*dx/dist)
                            dotY=int(omy+i*dy/dist)
                            screen.set_clip(dotX-eraserThick,dotY-eraserThick,2*eraserThick,2*eraserThick)
#making it so that only the eraser rect can be changed
                            #sample=subBack.subsurface((dotX-130,dotY-85,thick,thick))
                            #sample=subBack.subsurface((mx-150,my-95,thick,thick))
                            screen.blit(subBack,(135,80))#blitting the background
                            #but only the eraser rect changes to it erases everything
                            #leaving only the background
                    except:
                        pass
                else:#if the background is coloured
                    dx=mx-omx
                    dy=my-omy
                    dist=int(sqrt(dx**2+dy**2))
                    for i in range(1,dist+1):
                        dotX=int(omx+i*dx/dist)
                        dotY=int(omy+i*dy/dist)
                        draw.rect(screen,colPrev,(dotX,dotY,eraserThick,eraserThick))
   #drawing a rectangle the same colour as the background
            if tool=='rectangle':
                screen.blit(screenShot,(0,0))#only one rectangle can be drawn
                try:
                    w=mx-sx#width of rect
                    h=my-sy#height of rect
                    cx=sx #left corner x coordinate
                    cy=sy#left corner y coordinate
                    rectr=Rect(cx,cy,w,h)#rect which is being drawn
                    draw.rect(screen,col,rectr,rectThick)
                    for i in range(1,recThick+1):
                        w=mx-sx+i*2
                        h=my-sy+i*2
                        cx=sx-i
                        cy=sy-i
                        if w<0 and h>=0:
                            cx=sx+i
                            w=mx-sx-i*2
                        if h<0 and w>=0 :
                            h=my-sy-i*2
                            cy=sy+i
                        rectr=Rect(cx,cy,w,h)
                        draw.rect(screen,col,rectr,1)
                        if d3=='on':
                            secRect=Rect(cx+60,cy-60,w,h)
                            draw.rect(screen,col,secRect,1)
                            
                    if d3=='on':#if 3d rect is on 
                        shift=thick//2
                        draw.line(screen,col,(cx+shift,cy),(cx+60+shift,cy-60),thick)
                        draw.line(screen,col,(cx+w-shift,cy+h-shift),(cx+60+w-shift,cy-60+h),thick)
                        draw.line(screen,col,(cx+w-shift,cy),(cx+60+w-shift,cy-60),thick)
                        draw.line(screen,col,(cx+shift,cy+h-shift),(cx+60+shift,cy-60+h-shift),thick)
                except:
                    pass
            if tool=='lines':
                try:
                    screen.blit(screenShot,(0,0))
                    draw.line(screen,col,(sx,sy),(mx,my),lineThick,)
                except:
                    pass
            if tool=='circle':
                
                screen.blit(screenShot,(0,0))
                try:
                    d=int(sqrt((sx-mx)**2+(sy-my)**2))
                    
                    for i in range(4):#drawing circles at 4 different positions
                        #so the circle doesn't have missing pixels
                        for j in range(4):
                            xx,yy=sx,sy
                            if j%4==0:
                                xx=sx-j
                            elif j%4==1:
                                xx=sx+j
                            elif j%4==2:
                                yy=sy-j
                            elif j%4==3:
                                yy=sy+j
                            if 0<thick<10:
                                thick=10
                            draw.circle(screen,col,(xx,yy),d+thick+j,circleThick)
                except:
                    pass

            if tool=='ellipse':
                screen.blit(screenShot,(0,0))
                

                try:
                    w=abs(mx-sx)
                    h=abs(my-sy)
                    if mx>sx and my>sy:
                        ellRect=Rect(sx,sy,w,h)
                    if mx<sx and my<sy:
                        ellRect=Rect(mx,my,w,h)
                    if mx>sx and my<sy:
                        ellRect=Rect(sx,my,w,h)
                    if mx<sx and my>sy:
                        ellRect=Rect(mx,sy,w,h)
                    secRect=Rect(ellRect[0]+60,ellRect[1]-60,w,h)
                    ellRect.normalize()
                    draw.arc(screen,col,ellRect,0,360,arcThick)
                    #layering the ellipse so it goes around multiple times
                    #this way there aren't any missing pixels
                    draw.ellipse(screen,col,ellRect,rectThick)  
                except:
                    pass

                
                
            if tool=='spray paint':
                for i in range(10):
                    x=randint(-sprayThick,sprayThick)
                    y=randint(-sprayThick,sprayThick)
                    #random points from negative thicknesss to positive thickness
                    dis=sqrt((mx-(mx+x))**2+(my-(my+y))**2)#distance from mx,my to point
                    if dis<=sprayThick:#if its within the distance then it draws the point
                        draw.circle(screen,col,(mx+x,my+y),0)
            if tool=='polygon'and click:
                polyShot=screen.subsurface(canvasRect).copy()#taking a screenshot
                if len(polyShots)<1:
                    polyShots.append(polyShot)#making sure there is only one screenshot
                    #in polyShots
                if (mx,my) not in points:
                    points.append((mx,my))
                    draw.circle(screen,RED,(mx,my),thick)
                    #append the point to the points list if it's not in it 
                if len(points)>=2:
                    draw.rect(screen,WHITE,canvasRect)
                    screen.blit(polyShots[0],(135,80))
                    draw.polygon(screen,col,points,thick)
                    for i in points:#drawing circles at the verticies 
                        draw.circle(screen,RED,i,polyThick)
            if tool=='select':
                paste='off'
                shots=[]
                w,h=mx-sx,my-sy
                selectRect=Rect(mx,my,w,h)
                if mx>sx and my>sy:
                    selectRect=Rect(sx,sy,abs(w),abs(h))
                if mx<sx and my<sy:
                    selectRect=Rect(mx,my,abs(w),abs(h))
                if mx>sx and my<sy:
                    selectRect=Rect(sx,my,abs(w),abs(h))
                if mx<sx and my>sy:
                    selectRect=Rect(mx,sy,abs(w),abs(h))
                #selectRect.normalize()
                print(selectRect)
                befShot=screen.subsurface(canvasRect).copy()#screenshot before
                #the select tool is used
                if len(befShots)<1:
                    befShots.append(befShot)
                screen.blit(canvasShot,(135,80))
                draw.rect(screen,BLACK,selectRect,1)
                release='on'
                selected='on'
            if tool=='copy':
                if selected=='on':
                    draw.rect(screen,colPrev,selectRect,3)
                    copyShot=screen.subsurface(selectRect).copy()#shot of the copied
                    #rect
                    if len(shots)<1:
                        shots.append(copyShot)
                    draw.rect(screen,BLUE,selectRect,3)
                    w=copyShot.get_width()
                    h=copyShot.get_height()
                    if paste=='on':
                        if prev=='cut':#if the previous tool was cut instead of copy
                            screen.blit(canvasShot,(135,80))
                            screen.blit(shots[0],(mx-w//2,my-h//2))
                            newShot=screen.subsurface(canvasRect).copy()#the canvas
                            #after the thing has been pasted
                            befShots=[]#clearing befshots
                            befShots.append(newShot)
                            prev='none'
                            
                        else:
                            screen.blit(befShots[0],(135,80))
                            screen.blit(shots[0],(mx-w//2,my-h//2))
                            if click:
                                newShot=screen.subsurface(canvasRect).copy()
                                befShots=[]
                                befShots.append(newShot)
                            
                

            if tool=='highlighter':
                marker=Surface((highThick,highThick),SRCALPHA)#surface with transparency
                draw.circle(marker,(col[0],col[1],col[2],10),(highThick//2,highThick//2),highThick//2)
                dx=mx-omx
                dy=my-omy
                dist=int(sqrt(dx**2+dy**2))
                for i in range(1,dist+1):
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                    screen.blit(marker,(dotX,dotY))
                
                    
                
            if tool=='crayon':
                if omx!=mx and omy!=my:#if the coordinates are different 
                    dx=mx-omx
                    dy=my-omy
                    dist=int(sqrt(dx**2+dy**2))
                    for i in range(1,dist+1):
                        dotX=int(omx+i*dx/dist)
                        dotY=int(omy+i*dy/dist)
                        for i in range(2*crayThick):#using the spray paint algorithim 
                            marker=Surface((6,6),SRCALPHA)
                            x=randint(-crayThick,crayThick)
                            y=randint(-crayThick,crayThick)
                            dis=sqrt((mx-(mx+x))**2+(my-(my+y))**2)
                            surf=Surface((2*crayThick,2*crayThick),SRCALPHA)
                            if dis<=crayThick:
                                if dis>crayThick//2: 
                                    draw.circle(marker,(col[0],col[1],col[2],randint(0,70)),(3,3),3)
                                    surf.blit(marker,(crayThick+x,crayThick+y))
                                elif dis<crayThick//2:
                                    draw.circle(marker,(col[0],col[1],col[2],randint(100,190)),(3,3),3)
                                    surf.blit(marker,(crayThick+x,crayThick+y))
                            
                            
                            
                            screen.blit(surf,(dotX,dotY))
                
            if tool=='flood fill':
                try:
                    c=screen.get_at((mx,my))#getting the col of the current pixel
                    if c!=col:#if pixel colour isn't equal to current col
                        checkPoints.append((mx,my))#add it to checkpoints
                        while len(checkPoints)>0:#when checkpoints isnt empty
                            pixel=checkPoints.pop()
                            px,py=pixel[0],pixel[1]
                            if -1<py<600 and 5<py<700:
                                if screen.get_at(pixel)==c:
                                    screen.set_at(pixel,col)
                                    #appending nearly pixels to be checked
                                    checkPoints.append((px+1,py))
                                    checkPoints.append((px-1,py))
                                    checkPoints.append((px,py+1))
                                    checkPoints.append((px,py-1))
                except:
                    pass
                
            if tool=='eye dropper':
                screen.blit(eyeShots[1],(135,80))#blit the screen without
                #the eyedropper
                col=screen.get_at((mx,my))#changing col
                
            #hero stamp tools
            for i in range(24):#going into the list of heroes
                w=stampsList[i].get_width()
                h=stampsList[i].get_width()
                if tool==toolStampNames[i]:

                    screen.blit(canvasShot,(135,80))
                    screen.blit(stampsList[i],(mx-w//2,my-h//2))#bliting the stamp
                    
                    
                    if mixer.music.get_busy()==False:#playing the characters
                        #music only once
                        mixer.music.load(music[i])
                        mixer.music.play(-1,0.0)
                    stampCond='done'
                
                        
                    
            #villian stamp tools
            ###same thing
            for i in range(24):
                w=stampsList[i].get_width()
                h=stampsList[i].get_width()
                if tool==villToolStampNames[i]:
                    screen.blit(canvasShot,(135,80))
                    screen.blit(villStampsList[i],(mx-w//2,my-h//2))
                    if mixer.music.get_busy()==False:
                        mixer.music.load(villMusic[i])
                        mixer.music.play(-1,0.0)
                    stampCond='done'
                
    if mixer.music.get_busy()==False:
        musPos=randint(1,58)
        try:
            mixer.music.load(playList[musPos])
            mixer.music.play(-1)
            #if no song is playing then a song strats at a random positition in the
            #playlist
        except:
            pass
    

        
                
    #####back ton 'normal' mode
    screen.set_clip(None)##the entire screen can 
    #####change the colour
    if mb[0]==1 and click:
        if palRect.collidepoint(mx,my):
            col=screen.get_at((mx,my))
        if backCol=='on':
            if palRect.collidepoint(mx,my):
                colPrev=screen.get_at((mx,my))
                colChose='on'
            if colChose=='on':
                if colourPreview.collidepoint(mx,my):
                    draw.rect(screen,colPrev,canvasRect)
                    points=[]
                    polyShots=[]
                    backCol='off'
                    colTake='on'
                    colChose='off'
                    first='off'
                    bType='Coloured'
    if evt.type==MOUSEBUTTONDOWN:
         if evt.button==1:
             if colTake=='on':
                 screenShot=screen.copy()
                 undoShots.append(screenShot)
                 colTake='off'
    ####Icon hover
    if pencilRect.collidepoint(mx,my) or tool=='pencil':
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my) or tool=='eraser':
        draw.rect(screen,RED,eraserRect,2)
    if circleRect.collidepoint(mx,my) or tool=='circle':
        draw.rect(screen,RED,circleRect,2)
    if rectRect.collidepoint(mx,my) or tool=='rectangle':
        draw.rect(screen,RED,rectRect,2)
    if stampsRect.collidepoint(mx,my):
        draw.rect(screen,RED,stampsRect,2)
    if linesRect.collidepoint(mx,my) or tool=='lines':
        draw.rect(screen,RED,linesRect,2)
    if eraseAllRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraseAllRect,2)
    if ellipseRect.collidepoint(mx,my) or tool=='ellipse':
        draw.rect(screen,RED,ellipseRect,2)
    if villStampsRect.collidepoint(mx,my):
        draw.rect(screen,RED,villStampsRect,2)
    if sprayPaintRect.collidepoint(mx,my) or tool=='spray paint':
        draw.rect(screen,RED,sprayPaintRect,2)
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
    if copyRect.collidepoint(mx,my) or (tool=='copy' and paste=='off') :
        draw.rect(screen,RED,copyRect,2)
    if pasteRect.collidepoint(mx,my) or paste=='on':
        draw.rect(screen,RED,pasteRect,2)
    if cutRect.collidepoint(mx,my) or tool=='cut':
        draw.rect(screen,RED,cutRect,2)
    if cropRect.collidepoint(mx,my):
        draw.rect(screen,RED,cropRect,2)
    if highlighterRect.collidepoint(mx,my) or tool=='highlighter':
        draw.rect(screen,RED,highlighterRect,2)
    if selRect.collidepoint(mx,my) or tool=='select':
        draw.rect(screen,RED,selRect,2)
    if polygonRect.collidepoint(mx,my) or tool=='polygon':
        draw.rect(screen,RED,polygonRect,2)
    if brushRect.collidepoint(mx,my) or tool=='brush':
        draw.rect(screen,RED,brushRect,2)
    if eyeDropperRect.collidepoint(mx,my) or tool=='eye dropper':
        draw.rect(screen,RED,eyeDropperRect,2)
    if backgroundPreview.collidepoint(mx,my):
        draw.rect(screen,RED,backgroundPreview,2)
    if colourPreview.collidepoint(mx,my):
        draw.rect(screen,RED,colourPreview,2)
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,RED,loadRect,2)
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
    if crayonRect.collidepoint(mx,my)or tool=='crayon':
        draw.rect(screen,RED,crayonRect,2)
    if floodFill.collidepoint(mx,my) or tool=='flood fill':
        draw.rect(screen,RED,floodFill,2)
    if rect3d.collidepoint(mx,my) or d3=='on':
        draw.rect(screen,RED,rect3d,2)
#####Tool Descriptions
    if pencilRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='and drag to use the pencil'
        line3='Thickness is limited to 5'
        line4=''
    if eraserRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='and drag to use the eraser.'
        line3='It removes everything leaving'
        line4='only the background'
    if circleRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to be the centre'
        line3='of the circle. Move the mouse'
        line4='away to increase size'
    if rectRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to be the top left'
        line3='corner of the rectangle. Drag'
        line4='the mouse to form the rest.'
    if linesRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to be the start'
        line3='point. Drag the mouse to the'
        line4='end point.'
    if ellipseRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to be the top left'
        line3='corner of the ellipse. Drag'
        line4='the mouse to form the rest.'
    if sprayPaintRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to start spraying.'
        line3='Hold for more fill'
        line4=''
    if copyRect.collidepoint(mx,my) :
        line1='Select an area to copy using'
        line2='select tool and then click'
        line3='this tool to copy that area.'
        line4='Paste using the paste tool'
    if cutRect.collidepoint(mx,my):
        line1='Select an area to copy using'
        line2='select tool and then click'
        line3='this tool to cut that area.'
        line4='Paste using the paste tool'
    if cropRect.collidepoint(mx,my):
        line1='Select an area to copy using'
        line2='select tool and then click'
        line3='this tool to crop everything'
        line4='except the selected area'
    if highlighterRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='and drag to use the highlighter'
        line3='Thickness is limited to 50'
        line4=''
    if selRect.collidepoint(mx,my):
        line1='Use this tool to select an'
        line2='area so the copy, cut and '
        line3='paste tools can be used'
        line4=''
    if polygonRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='on a point to be the 1st.'
        line3='Select more points to form'
        line4='any polygon.Careful of order'
    if brushRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='and drag to use the brush'
        line3='Thickness is limited to 50'
        line4=''
    if eyeDropperRect.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='and then click on any point'
        line3='on the canvas to get the '
        line4='colour and use it'
    if backgroundPreview.collidepoint(mx,my):
        draw.rect(screen,RED,backgroundPreview,2)
        line1='Scroll the mouse to view'
        line2='different backgrounds and'
        line3='click to select one'
        line4=''
    if colourPreview.collidepoint(mx,my):
        draw.rect(screen,RED,colourPreview,2)
        line1='To change to a coloured'
        line2='background, click this,'
        line3='choose a colour, and'
        line4='click this icon again'
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,RED,loadRect,2)
        line1='Click to load an image'
        line2='from your computer'
        line3=''
        line4=''
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
        line1='Click to save the canavas'
        line2='on to your computer'
        line3=''
        line4=''
    if crayonRect.collidepoint(mx,my):
        draw.rect(screen,RED,crayonRect,2)
        line1='Click the left mouse button'
        line2='and drag to use the crayon'
        line3='Thickness is limited to 30'
        line4=''
    if floodFill.collidepoint(mx,my):
        line1='Click the left mouse button'
        line2='& then click any point on the'
        line3='canvas to change the colour of'
        line4='it and any connected pixels'
    if villStampsRect.collidepoint(mx,my):
        line1='Click to open up the stamp'
        line2='menu for the villians.'
        line3='Select a stamp or click X'
        line4='to exit'
    if stampsRect.collidepoint(mx,my):
        line1='Click to open up the stamp'
        line2='menu for the heroes.'
        line3='Select a stamp or click X'
        line4='to exit'
#######choosing stamps
    #Hero stamps 
    if tool=='stamps' or refresh=='on':
        stampShot=screen.subsurface(canvasRect).copy()#shot of canvas beofore
        if len(stampShots)<1:
            stampShots.append(stampShot)
        #the stamp menu opens up
        draw.rect(screen,BLACK,(0,0,width,height))
        draw.rect(screen,BLACK,stampRect)
        draw.rect(screen,BLUE,stampRect,4)
        draw.line(screen,BLUE,(90,283),(970,283),4)
        draw.line(screen,BLUE,(90,450),(970,450),4)
        screen.blit(cross,(950,113))
        for i in range(24):
            screen.blit(stampsList[i],stampBlits[i])
            #blitting the stamps at their coorindates
        stamps='active'#activating stamps
        cond='not done'
    if mb[0]==1 and crossRect.collidepoint(mx,my) and stamps=='active':
        reset='on'
        #restting the screen if the cross is clicked
    if  stamps=='active':
        for i in range(24):#if the stamps are hovered on then draw a red rect
            if picRects[i].collidepoint(mx,my):
                draw.rect(screen,RED,picRects[i],4)
                cond='done'
                refresh='on'
                if mb[0]==1:#if the stamp is clicked then the tool becomes
                    #that stamp
                    tool=toolStampNames[i]
                    stamps='not active'
                    reset='on'
                    refresh='off'
#######villian stamps
    #same process as hero stamps 
    if tool=='vill stamps' or villRefresh=='on':
        stampShot=screen.subsurface(canvasRect).copy()
        if len(stampShots)<1:
            stampShots.append(stampShot)
        draw.rect(screen,BLACK,(0,0,width,height))
        draw.rect(screen,BLACK,stampRect)
        draw.rect(screen,BLUE,stampRect,4)
        draw.line(screen,BLUE,(90,283),(970,283),4)
        draw.line(screen,BLUE,(90,450),(970,450),4)
        screen.blit(cross,(950,113))
        for i in range(24):
            screen.blit(villStampsList[i],villStampBlits[i])
        
        villStamps='active'
        
    if mb[0]==1 and crossRect.collidepoint(mx,my) and villStamps=='active':
        reset='on'
    #same process as hero stamps 
    if  villStamps=='active':
        for i in range(24):
            if picRects[i].collidepoint(mx,my):
                draw.rect(screen,RED,picRects[i],4)
                cond='done'
                villRefresh='on'
                if mb[0]==1:
                    tool=villToolStampNames[i]
                    villStamps='not active'
                    reset='on'
                    villRefresh='off'
        
    omx=mx#old mx and my
    omy=my
    display.flip()
    
font.quit()#deleting fonts to save memory
del comicFont    
        
quit()

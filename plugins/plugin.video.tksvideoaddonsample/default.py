########################################
####   TK's Sample Video Add-on     ####
#### We hope this helps you create  ####
####  Your own video add-on using   ####
####     This simple template       ####
#### Thanks to all the Dev's for    ####
####      All the work you do       ####
####       Thanks to Whufclee       ####
####   Thanks to Trent Bumgarner    ####
########################################

########################################
# Modules Needed
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,glob
import urllib2,urllib
import zipfile
import ntpath
########################################

########################################
# Global Variable Needed
VERSION        = "2.0.0"
ADDON          = xbmcaddon.Addon(id='plugin.program.tksvideoaddonsample')
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
PATH           = "tksapps"
base           = 'http://vampinc.com/tksapps'
HOME           = xbmc.translatePath('special://home')
ART            = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tksvideoaddonsample' + '/resources/art/'))
FANART         = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tksvideoaddonsample' + '/resources/art/' + 'fanart.jpg'))
########################################

########################################
# If you want to use your own images, please replace the images inside the resources/art folder inside this addon with your own.
# In order to save you time, make sure you wish the SAME file names as I have used in this sample. Otherwise, you will have to
# change the image names inside this file to match your new image names accordingly.
########################################


########################################
# Sample Menu 1 / Movie 1 Explained
# The first letter a,b,c,d ties the string to the correct sample menu
# m1  = a variable which could be named anything you would like. I used "m" for movie in this template. 
# mt1 = a variable which could be named anything you would like. I used "mt" for movie title in this template. 
# mi1 = a variable which could be named anything you would like. I used "mi" for movie image in this template. 
# mfa = a variable which could be named anything you would like. I used "mfa" for movie fanart in this template. 
# Each variable is followed by a number, this makes it easier when you have lots of items or in this case movies.
# You do not have to use numbers, but it can get confusing if each listing or movie has its own name.
# You do not have to keep the hashtag lines in the code, I put them here to make everything easier to read for you.
# When a hashtag (#) is used as the first character on a line, kodi will ignore the whole line.
# You could put all the movie urls together, all the titles, images, and fanart. Typically that is how I like to 
# write my addons, but for some people that can be confusing. I wrote them this way so each section so to speak
# will contain all the required information for that one movie. 
# You are NOT limited to only 5 movies per section. Just copy all four lines of a current section and paste it below the section
# you wish to add to. Make sure that you change the number to the next one in sequence. Also make sure that you add the new movie(s)
# to the correct directory below (directories starting at line 271 below), also please keep the format the same in these directories.
########################################

########################################
# Please be sure to keep your urls inside the ''
########################################

########################################
# Sample Menu A
# Movie 1
am1             = 'Movie URL Here'
amt1            = 'Movie Title A1'
ami1            = 'Icon Image URL Here'
amfa1           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu A
# Movie 2
am2             = 'Movie URL Here'
amt2            = 'Movie Title A2'
ami2            = 'Icon Image URL Here'
amfa2           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu A
# Movie 3
am3             = 'Movie URL Here'
amt3            = 'Movie Title A3'
ami3            = 'Icon Image URL Here'
amfa3           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu A
# Movie 4
am4             = 'Movie URL Here'
amt4            = 'Movie Title A4'
ami4            = 'Icon Image URL Here'
amfa4           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu A
# Movie 5
am5             = 'Movie URL Here'
amt5            = 'Movie Title A5'
ami5            = 'Icon Image URL Here'
amfa5           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu B
# Movie 1
bm1             = 'Movie URL Here'
bmt1            = 'Movie Title B1'
bmi1            = 'Icon Image URL Here'
bmfa1           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu B
# Movie 2
bm2             = 'Movie URL Here'
bmt2            = 'Movie Title B2'
bmi2            = 'Icon Image URL Here'
bmfa2           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu B
# Movie 3
bm3             = 'Movie URL Here'
bmt3            = 'Movie Title B3'
bmi3            = 'Icon Image URL Here'
bmfa3           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu B
# Movie 4
bm4             = 'Movie URL Here'
bmt4            = 'Movie Title B4'
bmi4            = 'Icon Image URL Here'
bmfa4           = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu B
# Movie 5
bm5            = 'Movie URL Here'
bmt5           = 'Movie Title B5'
bmi5           = 'Icon Image URL Here'
bmfa5          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu C
# Movie 1
cm1            = 'Movie URL Here'
cmt1           = 'Movie Title C1'
cmi1           = 'Icon Image URL Here'
cmfa1          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu C
# Movie 2
cm2            = 'Movie URL Here'
cmt2           = 'Movie Title C2'
cmi2           = 'Icon Image URL Here'
cmfa2          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu C
# Movie 3
cm3            = 'Movie URL Here'
cmt3           = 'Movie Title C3'
cmi3           = 'Icon Image URL Here'
cmfa3          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu C
# Movie 4
cm4            = 'Movie URL Here'
cmt4           = 'Movie Title C4'
cmi4           = 'Icon Image URL Here'
cmfa4          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu C
# Movie 5
cm5            = 'Movie URL Here'
cmt5           = 'Movie Title C5'
cmi5           = 'Icon Image URL Here'
cmfa5          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu D
# Movie 1
dm1            = 'Movie URL Here'
dmt1           = 'Movie Title D1'
dmi1           = 'Icon Image URL Here'
dmfa1          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu D
# Movie 2
dm2            = 'Movie URL Here'
dmt2           = 'Movie Title D2'
dmi2           = 'Icon Image URL Here'
dmfa2          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu D
# Movie 3
dm3            = 'Movie URL Here'
dmt3           = 'Movie Title D3'
dmi3           = 'Icon Image URL Here'
dmfa3          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu D
# Movie 4
dm4            = 'Movie URL Here'
dmt4           = 'Movie Title D4'
dmi4           = 'Icon Image URL Here'
dmfa4          = 'Fanart Image URL Here'
########################################

########################################
# Sample Menu D
# Movie 5
dm5            = 'Movie URL Here'
dmt5           = 'Movie Title D5'
dmi5           = 'Icon Image URL Here'
dmfa5          = 'Fanart Image URL Here'
########################################

########################################
# Initialise Directory Explained:
# tks_apps could be named anything, it is just a container variable that I created for this template.
# if you change it, please be sure to change all of them below. You will find a total of 3.
# int = interger | sys = we imported this at the top of the code and we are telling it to
# use argv. argv = will create a list which contains arguments. The [1] just tells it to
# get the first argument.
########################################

########################################
# Initialise Directory Structure
tks_apps      = int(sys.argv[1])
########################################

########################################
# Creating Menus Explained:
# You have to (def) define a label first. The INDEX (line 263) is written to be shown when the addon is loaded. I would not change the name of INDEX, but it is possible.
# Line 257 through 260 You can change Sample Menu A-D to reflect whatever you wish. The Sample Menu 1 is what will be shown inside of Kodi under your folder.
# As you can see below I have SampleMenu1 through 4. You can change the name 
# of the SAMPLEMENU, just be sure to change it at the bottom of the page as well to match the new name.
########################################
def INDEX():
    addDir('Sample Menu A',base,2,ART+'samplemenu1.png',FANART,'')
    addDir('Sample Menu B',base,3,ART+'samplemenu2.png',FANART,'') 
    addDir('Sample Menu C',base,4,ART+'samplemenu3.png',FANART,'')  
    addDir('Sample Menu D',base,6,ART+'samplemenu4.png',FANART,'')
    setView('movies', 'MAIN')

def SAMPLEMENUA():
    addDir(amt1, am1, 5, ami1, amfa1, '')
    addDir(amt2, am2, 5, ami2, amfa2, '')
    addDir(amt3, am3, 5, ami3, amfa3, '')
    addDir(amt4, am4, 5, ami4, amfa4, '')
    addDir(amt5, am5, 5, ami5, amfa5, '')
    setView('movies', 'MAIN')

def SAMPLEMENUB():
    addDir(bmt1, bm1, 5, bmi1, bmfa1, '')
    addDir(bmt2, bm2, 5, bmi2, bmfa2, '')
    addDir(bmt3, bm3, 5, bmi3, bmfa3, '')
    addDir(bmt4, bm4, 5, bmi4, bmfa4, '')
    addDir(bmt5, bm5, 5, bmi5, bmfa5, '')
    setView('movies', 'MAIN')
    
def SAMPLEMENUC():
    addDir(cmt1, cm1, 5, cmi1, cmfa1, '')
    addDir(cmt2, cm2, 5, cmi2, cmfa2, '')
    addDir(cmt3, cm3, 5, cmi3, cmfa3, '')
    addDir(cmt4, cm4, 5, cmi4, cmfa4, '')
    addDir(cmt5, cm5, 5, cmi5, cmfa5, '')
    setView('movies', 'MAIN')

def SAMPLEMENUD():
    addDir(dmt1, dm1, 5, dmi1, dmfa1, '')
    addDir(dmt2, dm2, 5, dmi2, dmfa2, '')
    addDir(dmt3, dm3, 5, dmi3, dmfa3, '')
    addDir(dmt4, dm4, 5, dmi4, dmfa4, '')
    addDir(dmt5, dm5, 5, dmi5, dmfa5, '')
    setView('movies', 'MAIN')

########################################
# Creating Function Explained:
# You do not have to create this function below, but you would have to write out the entire line for each movie if you don't.
# By writing the code like below, when you wish to add another movie you only need to write addDir(url,title,icon,fanart)
# As you can see we have (name, url, mode, iconimage, fanart, description), this is done again to make it easier to add information fast.
# What we put first = name, second = url, third = mode, fourth = iconimage, fifth = fanart, and last = description.
# By creating variables for each one makes it cleaner to read and easier to use.
# If you don't use variables then it would look something like the following:
# addDir('My Movie', http://www.yoursite.com/movie.mpg', 5, 'http://www.yoursite.com/image.jpg', 'http://www.yoursite.com/fanart.jpg', '')
# It is your addon, so it's your choice how you chose to write the code within.
########################################
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            li = xbmcgui.ListItem(name, iconImage =iconimage)
            li.setProperty("Fanart_Image", fanart)
            xbmcplugin.addDirectoryItem(handle=tks_apps, url=url, listitem=li)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok   

########################################
# Paramaters Defined:
# What we are doing here is cleaning up the information return from other sources and defining a few more variables
########################################
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

params        =get_params()
url           =None
name          =None
mode          =None
iconimage     =None
fanart        =None
description   =None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
########################################

########################################
# setView explained:
# This is added in order to tell Kodi what type of view to display our content in.
########################################

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

########################################
# If / Else If Mode Explained:
# We are using mode to inform Kodi which directory we wish to use. As you can see I have written below
# if mode is equal to none or url equals none or length url is less than 1 to display the index menu by default.
# If we tell Kodi to use a different mode 2, 3, 4, or 6 it would display the correct mode as written below.
# If you changed ANY of the SAMPLEMENU(s) above, please make sure to change them to match exactly below.
########################################

if mode==None or url==None or len(url)<1:
         INDEX()

elif mode==2:
         SAMPLEMENUA()
    
elif mode==3:
         SAMPLEMENUB()  
        
elif mode==4:
         SAMPLEMENUC()
        
elif mode==6:
         SAMPLEMENUD() 

########################################
# Close Directory Explained:
# We are using the xbmxplugin that we imported at the top and we are telling it to use endOfDirectory.
# endOfDirectory tells kodi that it is the end of the firectory listing in a module, we just have to tell it which 
# container variable.
########################################

########################################
#####  Close Directory Structure   #####
xbmcplugin.endOfDirectory(tks_apps)
########################################
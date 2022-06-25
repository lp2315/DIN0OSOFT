from app_AssetLoader import *
import pyglet as pyg
########################################

# Main Application

# endast för kopering TILL

########################################
########################################

font_addit(usr_font)

LeifRoot = pyg.window

LeifWin = LeifRoot.Window()

dt = pyg.clock.tick()

fpsmeter = pyg.window.FPSDisplay(window=LeifWin)

########################################

########################################

titletext = pyg.text.Label(
    'LEIF',
    font_name='TACKERLEN', font_size=64,
    color=(200, 217, 224, 201),
    x=LeifWin.width // 2, y=LeifWin.height // 2
)

spr_12_addit('mewalk.png')

########################################

# LeifApp

########################################


@LeifWin.event
def on_draw():
    LeifWin.clear()

    batch_1.draw()
    fpsmeter.draw()
    titletext.draw()


pyg.app.run()

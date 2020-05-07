import nuke

## labels
nuke.knobDefault('TimeClip.label', '[value first] to [value last]')
nuke.knobDefault('OCIOColorSpace.label', '<i>[value in_colorspace]</i> <b>to</b> <i>[value out_colorspace]')
nuke.knobDefault('Tracker.label', '[value transform] [value reference_frame]')

## defaults
nuke.knobDefault('Exposure.mode', 'Stops')

##custom functions

def bbob_to_b():
    [ n['bbox'].setValue('B') for n in nuke.selectedNodes() if 'bbox' in n.knobs()]

def serve_raw():
    [ n['raw'].setValue(True) for n in nuke.selectedNodes() if 'raw' in n.knobs()]

def label_dots_and_stamps():
    dotsNStamps=[]
    n=nuke.selectedNode()
    classes=['Dot', 'PostageStamp']
    while n.Class() in classes:
        dotsNStamps.append(n)
        n= n.input(0)
    colour= int(n['tile_color'].getValue()) 
    for d in dotsNStamps:
        d['label'].setValue( n['name'].getValue() )
        d['tile_color'].setValue(colour)
        


def toggle_hide():
    nh=nuke.selectedNode()['hide_input']
    toggle={True: False, False: True}
    nh.setValue(toggle[nh.getValue()] )      


##custom menu

danTools=nuke.menu("Nuke")
d=danTools.addMenu("&Danny")
d.addCommand("python/&bbox2B", "bbob_to_b()", "Shift+B")
d.addCommand("python/&Serve Raw", "serve_raw()", "Shift+R")
d.addCommand("python/&Label Dots and Stamps", "label_dots_and_stamps()", ",", shortcutContext=2)
d.addCommand("python/&Toggle Hide", "toggle_hide()", "shift+h")

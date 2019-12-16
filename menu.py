import nuke

nuke.knobDefault('TimeClip.label', '[value first] to [value last]')
nuke.knobDefault('Exposure.mode', 'Stops')
nuke.knobDefault('OCIOColorSpace.label', '<i>[value in_colorspace]</i> <b>to</b> <i>[value out_colorspace]')

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

danTools=nuke.menu("Nuke")
d=danTools.addMenu("&Danny")
bboxB=d.addCommand("python/&bbox2B", "bbob_to_b()", "Shift+B")
serveraw=d.addCommand("python/&Serve Raw", "serve_raw()", "Shift+R")
labelDotsAndStamps=d.addCommand("python/&Label Dots and Stamps", "label_dots_and_stamps()", ",")
ToggleHide=d.addCommand("python/&Toggle Hide", "toggle_hide()", "shift+h")

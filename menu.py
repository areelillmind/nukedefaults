import nuke

## Node default settings and labels


nuke.knobDefault('Exposure.mode', 'Stops')
nuke.knobDefault('MotionBlur.shutterTime', '0.5')
nuke.knobDefault('MotionBlur.shutterSamples', '10')
nuke.knobDefault('STMap.uv', 'rgb')
nuke.knobDefault('IDistort.uv', 'forward')
nuke.knobDefault('LayerContactSheet.showLayerNames', '1')

## labels
nuke.knobDefault('TimeClip.label', '[value first] to [value last]')
nuke.knobDefault('OCIOColorSpace.label', '<i>[value in_colorspace]</i> <b>to</b> <i>[value out_colorspace]')
nuke.knobDefault('Constant.label', '[value width] x [value height]')
nuke.knobDefault('Remove.label', '[value operation]')
nuke.knobDefault('Tracker.label', '[value transform] <br> ref frame: [value reference_frame]')
nuke.knobDefault('VectorDistort.label', 'ref frame [value referenceFrame]')


## helper functions

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
    


## custom menubar

danTools=nuke.menu("Nuke")
d=danTools.addMenu("&Danny")
bboxB=d.addCommand("python/&bbox2B", "bbob_to_b()", "Shift+B", shortcutContext=2)
serveraw=d.addCommand("python/&Serve Raw", "serve_raw()",  "shift+R", shortcutContext=2)
labelDotsAndStamps=d.addCommand("python/&Label Dots and Stamps", "label_dots_and_stamps()", ",", shortcutContext=2)
ToggleHide=d.addCommand("python/&Toggle Hide", "toggle_hide()", "shift+h", shortcutContext=2)


#custom hotkeys

unpremultKey=d.addCommand("unpremult", "nuke.createNode('Unpremult')", "U", shortcutContext=2)

premultKey=d.addCommand("premult", "nuke.createNode('Premult')", "Ctrl+U", shortcutContext=2)

channelMergeKey=d.addCommand("channelmerge", "nuke.createNode('ChannelMerge')", "Ctrl+M", shortcutContext=2)

import merge_transforms_v2

MergeTrasnforms=d.addCommand("python/&Merge Transforms", "merge_transforms_v2.start()", "shift+t", shortcutContext=2)


import animated_cornerpin_to_matrix

d.addCommand('CornerPinToMatrix', 'animated_cornerpin_to_matrix.animatedCP2MTX()', "Ctrl+shift+t", shortcutContext=2, icon='CornerPin.png')

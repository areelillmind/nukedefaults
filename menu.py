import nuke

## Node default settings and labels


nuke.knobDefault('Exposure.mode', 'Stops')
nuke.knobDefault('MotionBlur.shutterTime', '0.5')
nuke.knobDefault('MotionBlur.shutterSamples', '10')
nuke.knobDefault('STMap.uv', 'rgb')
nuke.knobDefault('IDistort.uv', 'forward')
nuke.knobDefault('LayerContactSheet.showLayerNames', '1')
nuke.knobDefault('Tracker.reference_frame', '1001')
nuke.knobDefault('Tracker4.warp', '4') #Track warp set to "Affine"



## labels
nuke.knobDefault('TimeClip.label', '[value first] to [value last]')
nuke.knobDefault('OCIOColorSpace.label', '<i>[value in_colorspace]</i> <b>to</b> <i>[value out_colorspace]')
nuke.knobDefault('Constant.label', '[value width] x [value height]')
nuke.knobDefault('Remove.label', '[value operation]')
nuke.knobDefault('Tracker.label', '[value transform] <br> ref frame: [value reference_frame]')
nuke.knobDefault('VectorDistort.label', 'ref frame [value referenceFrame]')


## helper functions

def bbob_to_b():
    '''Will set the bbox to 'b' for all selected nodes which have a bbox knob'''
    [ n['bbox'].setValue('B') for n in nuke.selectedNodes() if 'bbox' in n.knobs()]

def serve_raw():
    '''Will set the in raw checkbox to True for all selected nodes which have one'''
    [ n['raw'].setValue(True) for n in nuke.selectedNodes() if 'raw' in n.knobs()]

def label_dots_and_stamps():
    '''Based on initial selections will label all dot nodes and PostageStamps based on the first upstream node which is neither a dot nor a PostageStamp
    Will also take any non-default colours from the top node'''
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
    '''Hides input of selectedNode if unhidden, unhides input if hidden'''
    nh=nuke.selectedNode()['hide_input']
    toggle={True: False, False: True}
    nh.setValue(toggle[nh.getValue()] )

def timewarp_camera():
    '''Select a TimeWarp and CameraNode and Expression link all animated values in the camera to the TimeWarp'''
    sNodes=nuke.selectedNodes()
    if len(sNodes)>2:
        nuke.message('Please select TimeWarp and Camera node only')
    # assign nodes to variables and check we have Camera and TimeWarp.
    camera, timewarp = None, None
    for node in sNodes:
        if node.Class()=="Camera2":
            camera=node
        if node.Class()=="TimeWarp":
            timewarp=node
    if camera and timewarp:
        timeWarpName=timewarp['name'].getValue()
        knobExpression="curve("+timeWarpName+".lookup)"
        for knob in camera.knobs():
            if camera[knob].isAnimated():
                camera[knob].setExpression(knobExpression)
    else:
        nuke.message('Please select a TimeWarp and a Camera node')


## custom menubar

danTools=nuke.menu("Nuke")
d=danTools.addMenu("&Danny")
bboxB=d.addCommand("python/&bbox2B", "bbob_to_b()", "Shift+B", shortcutContext=2)
serveraw=d.addCommand("python/&Serve Raw", "serve_raw()",  "shift+R", shortcutContext=2)
labelDotsAndStamps=d.addCommand("python/&Label Dots and Stamps", "label_dots_and_stamps()", ",", shortcutContext=2)
ToggleHide=d.addCommand("python/&Toggle Hide", "toggle_hide()", "shift+h", shortcutContext=2)
import Copy_With_Inputs as cwp
d.addCommand("python/&Copy With Input", "cwp.copy_with_inputs()", "Ctrl+C")
d.addCommand("python/&Paste With Input", "cwp.paste_with_inputs()", "Alt+V")
d.addCommand("python/&TimeWarp Camera", "timewarp_camera()", "Alt+R", shortcutContext=2)


#custom hotkeys

unpremultKey=d.addCommand("unpremult", "nuke.createNode('Unpremult')", "U", shortcutContext=2)

premultKey=d.addCommand("premult", "nuke.createNode('Premult')", "Ctrl+U", shortcutContext=2)

channelMergeKey=d.addCommand("channelmerge", "nuke.createNode('ChannelMerge')", "Ctrl+M", shortcutContext=2)

## download from here and add to .nuke before uncommenting http://www.nukepedia.com/python/nodegraph/merge_transforms_v2
#import merge_transforms_v2

#MergeTrasnforms=d.addCommand("python/&Merge Transforms", "merge_transforms_v2.start()", "shift+t", shortcutContext=2)


## Download function from here before uncommenting and add to .nuke. https://gist.github.com/EgbertReichel/1ca0062b7420ab5c1806
#import animated_cornerpin_to_matrix

#d.addCommand('CornerPinToMatrix', 'animated_cornerpin_to_matrix.animatedCP2MTX()', "Ctrl+shift+t", shortcutContext=2, icon='CornerPin.png')

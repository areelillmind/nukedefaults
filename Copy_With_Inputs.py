'''Makes a copy of the selected node which retains all the input connections. Useful if you like to copy Postage Stamps for example. It works with nodes which have multiple inputs such as Scenes, Merges  and Scanline Renderers
Free to use and share. Please credit Daniel Mark Miller
'''

import nuke

def copy_with_inputs():
    sourceNode = nuke.selectedNode()
    inputs=sourceNode.dependencies()
    nuke.nodeCopy("%clipboard%")
    sourceNode['selected'].setValue(False)
    copiedNode=nuke.nodePaste("%clipboard%")
    copiedNode['xpos'].setValue(sourceNode['xpos'].getValue()+100)
    copiedNode['ypos'].setValue(sourceNode['ypos'].getValue()-100)
    curInput=0

    for i in inputs:
        copiedNode.setInput(curInput, i)
        curInput+=1
    return copiedNode
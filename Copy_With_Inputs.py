'''Makes a copy of the selected node which retains all the input connections. Useful if you like to copy Postage Stamps for example. It works with nodes which have multiple inputs such as Scenes, Merges and Scanline Renderers
Free to use and share. Please credit Daniel Mark Miller
'''

import nuke, nukescripts

def copy_with_inputs():
    global nodeInputs
    sourceNode = nuke.selectedNode()
    nodeInputs=sourceNode.dependencies()
    nuke.nodeCopy(nukescripts.cut_paste_file())

    
def paste_with_inputs():
    curInput=0
    copiedNode=nuke.nodePaste("%clipboard%")
    for i in nodeInputs:
        copiedNode.setInput(curInput, i)
        curInput+=1
    return copiedNode

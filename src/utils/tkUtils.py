def setupRootGeometry(root, ratio=0.5):
    """
    Make ideal windows geometry and return dimensions
    """
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    rootHeight = (int) (ratio * screenHeight)
    rootWidth = (int) (ratio * screenWidth)

    # widthxheight+x+y
    root.geometry(f"{rootWidth}x{rootHeight}+{(screenWidth - rootWidth) // 2}+{(screenHeight - rootHeight) // 2}")
    return rootWidth, rootHeight

def lockRootDimensions(root, dimensions):
    """
    Bloque les dimensions de la fenêtre
    """
    root.minsize(dimensions[0], dimensions[1])
    root.maxsize(dimensions[0], dimensions[1])

def packRelativeRatio(root, item, ratioX, ratioY, anchor):
    winWidth = root.winfo_width()
    winHeight = root.winfo_height()

    item.pack(padx=int(ratioX * winWidth), pady=int(ratioY * winHeight), anchor=anchor)

def startWithFunction(str1, str2):
    return str1.startswith(str2)

def itemHasTag(canvas, itemID, patternFunction, pattern):
    tags = canvas.gettags(itemID)
    n = len(tags)
    i = 0
    while (i < n) and (not patternFunction(tags[i], pattern)):
        i += 1
    
    if (i >= n):
        return None
    else:
        return tags[i]
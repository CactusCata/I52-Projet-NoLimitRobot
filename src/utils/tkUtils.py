def setupRootGeometry(root, ratio=0.5):
    """
    Make ideal windows geometry and return dimensions
    """
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    rootHeight = (int) (ratio * screenHeight)
    rootWidth = (int) (rootHeight * 1.618) # omg the god golden number

    # widthxheight+x+y
    root.geometry(f"{rootWidth}x{rootHeight}+{(screenWidth - rootWidth) // 2}+{(screenHeight - rootHeight) // 2}")
    return rootWidth, rootHeight

def lockRootDimensions(root, dimensions):
    """
    Bloque les dimensions de la fenêtre
    """
    root.minsize(dimensions[0], dimensions[1])
    root.maxsize(dimensions[0], dimensions[1])
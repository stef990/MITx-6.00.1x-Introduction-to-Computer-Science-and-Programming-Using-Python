def DFSBinaryOrdered(root, fcn, ltFcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        elif ltFcn(queue[0]):
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
    return False

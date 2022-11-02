from queue import PriorityQueue

def aStarSearch(start):
    Openlst = PriorityQueue()
    Closedlst = list()
    
    start.parent = None
    start.gScore = 0
    start.fScore = start.heuristicEvaluate()
    
    Openlst.put(start)
    
    while not Openlst.empty():
        cur = Openlst.get()[1]
        if cur.isLevelComplete():
            return cur
        Closedlst.append(cur)
        children = cur.generateChildren()
        for child in children:
            if child in Closedlst:
                continue
            tentative_gScore = cur.gScore + 1 # 1 meaning cost from cur to this child
            if tentative_gScore < child.gScore:
                child.parent = cur
                child.gScore = tentative_gScore
                child.fScore = tentative_gScore + child.heuristicEvaluate()
                if (child.fScore,child) not in Openlst:
                    Openlst.put(child)
                    
    return False
            
        
        
    
    
    
    
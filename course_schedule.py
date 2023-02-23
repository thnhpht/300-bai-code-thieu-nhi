def canFinish(numCourses, prerequisites):
    def dfs(node, processed, processing, outNodes):
        if node in processing: return False
        if not outNodes[node]:
            processed.append(node)
            return True
        processing.append(node)
        for child in outNodes[node]:
            if child in processing: return False
            if child in processed: continue
            if not dfs(child, processed, processing, outNodes): 
                return False
        processing.remove(node)
        processed.append(node)
        return True

    inDegrees = [0] * numCourses
    outNodes = [[] for _ in range(numCourses)]
    for pre in prerequisites:
        inDegrees[pre[0]] += 1
        outNodes[pre[1]].append(pre[0])

    roots = []
    for i, degree in enumerate(inDegrees):
        if degree == 0:
            roots.append(i)
    processing = []
    processed = []

    for root in roots:
        if root not in processed:
            if not dfs(root, processed, processing, outNodes): 
                return False
    return len(processed) == numCourses

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(canFinish(numCourses, prerequisites))
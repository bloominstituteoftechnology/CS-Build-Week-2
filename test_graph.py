from basic_utils import Graph
graph = Graph()
graph.vertices = {'1':{'n':'2','e':'3','w':'4','s':'5'},'2':{'s':'1'},'3':{'w':'1'},'4':{'e':'1'},'5':{'n':'1'}}
print(graph.bfs('5','3'))
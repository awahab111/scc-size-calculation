import graph

def scc_iterative_dfs(vertices, edges):
    recognized = set()
    index = {}
    border = []
    stack = []

    for v in vertices:
        if v not in index:
            process = [('not_visited', v)]
            while process:
                process_type, v = process.pop()
                if process_type == 'not_visited':
                    index[v] = len(stack)
                    border.append(index[v])
                    stack.append(v)
                    process.append(('visited', v))
                    process.extend(([('visit_neighbors', e) for e in edges[v]]))
                elif process_type == 'visit_neighbors':
                    if v not in index:
                        process.append(('not_visited', v))
                    elif v not in recognized:
                        while index[v] < border[-1]:
                            border.pop()
                else:
                    # process_type == 'visited'
                    if border[-1] == index[v]:
                        border.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        recognized.update(scc)
                        yield scc
    return

def largest_scc(filename):
    edges = graph.create_adjacency_list(filename)
    vertices = graph.get_vertices(edges)
    result = []
    for scc in  scc_iterative_dfs(vertices, edges):
        result.append(scc)
    
    return len(max(result, key = len))



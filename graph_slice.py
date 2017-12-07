graph = {'edges': [
            {'src': 'a',
             'dst':'b'},
            {'src': 'a',
             'dst':'c'},
            {'src': 'b',
             'dst':'d'},
            {'src': 'b',
             'dst':'e'},
            {'src': 'e',
             'dst':'f'},
         ],
         'vertices': [
            {'name':'a'},
            {'name':'b'},
            {'name':'c'},
            {'name':'d'},
            {'name':'e'},
            {'name':'f'}
         ]
        }

"""
    
    a
   / \
  b   c
 / \
d   e
     \
      f
"""
def slice(name, graph):
    sliced = []
    def forward_slice(name):
        node = [node for node in graph['vertices'] if name == node['name']][0]
        if not any([e for e in graph['edges'] if e['src'] == node['name']]):
            #leaf
            sliced.append(node)
        for e in graph['edges']:
            if e['src'] == node['name']:
                if node['name'] not in [sliced_node['name'] for sliced_node in sliced]:
                    sliced.append(node)
                forward_slice(e['dst'])
    forward_slice(name)
    return sliced

from pprint import pprint
slices = slice('b',graph)
pprint(slices)
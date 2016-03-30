#coding=utf-8
__author__ = 'zjutK'
def lap_cent(graph, nbunch=None, norm=False):
  if nbunch is None:
    vs = graph.nodes()
  else:
    vs = nbunch
  degrees = graph.degree(weight=None)
  if norm is True:
    den = sum(v**2 + v for i,v in degrees.items())
    den = float(den)
  else:
    den = 1
  result = []
  for v in vs:
    neis = graph.neighbors(v)
    loc = degrees[v]
    nei = 2*sum(degrees[i] for i in neis)
    val = (loc**2 + loc + nei)/den
    result.append(val)
  return result


def lap_energy(graph, weight='weight'):
  degrees = graph.degree(weight=weight)
  d1 = sum(v**2 for i,v in degrees.items())
  wl = 0
  for i in graph.edges(data=True):
    wl += (i[2].get(weight))**2
  return [d1,2*wl]

def cw(graph,node,weight='weight'):
  neis = graph.neighbors(node)
  ne = graph[node]
  cw,sub = 0,0
  for i in neis:
    we = ne[i].get(weight)
    od = graph.degree(i,weight=weight)
    sub += -od**2 + (od - we)**2
    cw += we**2
  return [cw,sub]


def lap_cent_weighted(graph, nbunch=None, norm=False, weight='weight'):
  if nbunch is None:
    vs = graph.nodes()
  else:
    vs = nbunch
  if norm == True:
    fe = lap_energy(graph,weight=weight)
    den = float(fe[0]+fe[1])
  else:
    den = 1
  result = []
  for i in vs:
     d2 = graph.degree(i,weight=weight)
     w2 = cw(graph,i,weight=weight)
     fin = d2**2 - w2[1] + 2*w2[0]
     result.append(fin/den)
  return result

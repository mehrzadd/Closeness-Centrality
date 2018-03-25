import sys
import os
import pdb
import timeit
import collections

try:
	first_arg = sys.argv[1]
	d = {}
	start1 = timeit.default_timer()

	def main_program (data=first_arg):
	  status={}
	  node=[]
	  with open(data, 'r') as f:
	    for line in f:
	       (key, val) = line.strip().split('\t')
	       if key not in d:
	           d[key] = [val]     
	       else:
	       #if key in d and val not in d[key]:
	           d[key].append(val)
	       if val not in d:
	           d[val]=[key]
	       #if val in d and key not in d[val]:
	       else:
	           d[val].append(key)
	       node=d.keys()
	  closeness, time=bfs(d, node)
	  od = collections.OrderedDict(sorted(closeness.items()))
	  for key, item in od.items():
	    print("[{0}]\t{1}".format(key,item))
	  print ("running time of this algorithm is "+ time)


	def bfs(graph,node):
		closeness={}
		for start in node:
		  count_path={}

		  #status={u :"free" for u in node}
		  sumi=0
		  q=[start]
		  #path=[int(start)]
		  count=1
		  #
		  count_path[start]=0
		  while q:
			  v=q.pop(0)
			  for u in graph[v]:
			    if u not in count_path:
			      count_path[u]=int(count_path[v])+1
			      count=count+1
			      q.append(u)
			      # sumi=sumi+count_path[u]
			      sumi=sumi+(1/float(count_path[u]))
		  # closeness[int(start)]=float(count)/sumi
		  # if start is "1":
		  # 	pdb.set_trace()
		  closeness[int(start)]=float(1/(float(count)-1))*sumi
		stop1 = timeit.default_timer()
		runtime= float(stop1) - float(start1)
		#pdb.set_trace()
		return closeness, str(runtime)

	if __name__ == '__main__':
		main_program()

except Exception as e:
  print ("please give an input as edgelist")
  sys.stdout.flush()

import math
import random

t = 0 #Time
Tstop = 2000 #TIME of simulation
posStop = 16 #number of slices TODO: better handling

# chosen number - needs change
pr1 = 0.2 # move
pr2 = 0.3 # attach
pr3 = 0.4 # do nothing

processes = [pr1, pr2, pr3]

class Cluster:
  def __init__(self, pos = 0, size = 2):
    self.pos = pos
    self.size = size

cl = Cluster()

while(t<Tstop and cl.pos < posStop):

    """
    TODO:
    --- update only whose need to
    --- loop over clusters
    --- slices innicialization, better handling
    --- tpos -> time list - better handling, into list of events in time
    """

    tpos = [(-math.log(random.uniform(0.0, 1.0)) / process , i) for i,process in enumerate(processes)]
    mintpos = min(tpos)
    dt = mintpos[0]
    minpos = mintpos[1]

    t = t + dt

    if(minpos == 0):
        cl.pos += 1
    if(minpos == 1):
        cl.size += 1

print(cl.pos, cl.size)





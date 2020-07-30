#from data import *
#from parameter import *
#import nevergrad.parameterization as p
import nevergrad as ng

import numpy as np
#import typing as tp


ControlParams = p.Array( shape=(5,) ).set_bounds( -1, 1, rollover=False )
#RollingParams = p.Array( shape=(5,) ).set_bounds( -1, 1, rollover=True )
source = [ -0.5, 0.25, 0.25, -100.0, 500.0 ]
destination = [ 0.5, -0.5, 0.25, 0.0, -2.0 ]
expected_results = [ 1.0, -0.75, 0.0, 100.0, -502.0 ]

source_array = p.Array( init=source )
destination_array = p.Array( init=destination )
vector = ControlParams.vector( source_array, destination_array )

print( vector )
print( expected_results )

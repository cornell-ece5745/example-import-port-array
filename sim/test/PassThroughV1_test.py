#=========================================================================
# PassThroughV1 unit test
#=========================================================================

import pytest
import random

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from PassThroughV1 import PassThroughV1

# Use the same seed so that debugging will be easier
random.seed(0xdeadbeef)

#-------------------------------------------------------------------------
# 4x 16-bit ports
#-------------------------------------------------------------------------

def test_directed( cmdline_opts ):
  run_test_vector_sim( PassThroughV1( 4, 16 ), [
      "in_[0]  in_[1]   in_[2]   in_[3]   out[0]*  out[1]*  out[2]*  out[3]*",
    [ b16(0),  b16(0),  b16(0),  b16(0),  b16(0),  b16(0),  b16(0),  b16(0)  ],
    [ b16(1),  b16(0),  b16(3),  b16(3),  b16(1),  b16(0),  b16(3),  b16(3)  ],
    [ b16(-1), b16(42), b16(30), b16(25), b16(-1), b16(42), b16(30), b16(25) ],
    [ b16(42), b16(-1), b16(20), b16(16), b16(42), b16(-1), b16(20), b16(16) ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# Random parameterized test
#-------------------------------------------------------------------------

@pytest.mark.parametrize( "nports, nbits", [
    (2, 16), (2, 32), (2, 64),
    (3, 16), (3, 32), (3, 64),
    (4, 16), (4, 32), (4, 64),
  ]
)
def test_random( nports, nbits, cmdline_opts ):
  nvectors = 10
  bits_type = mk_bits(nbits)

  hd_str  = ' '.join( [ f"in_[{i}]" for i in range(nports) ] )
  hd_str += ' '
  hd_str += ' '.join( [ f"out[{i}]*" for i in range(nports) ] )

  # Generate test vectors
  tvectors = [ hd_str ]
  for i in range(nvectors):
    vector = []
    # Add input data
    for j in range(nports):
      vector.append( bits_type( random.randint(0, 1024) ) )
    # Add output data
    for j in range(nports):
      vector.append( vector[j] )
    tvectors.append( vector )

  run_test_vector_sim( PassThroughV1( nports, nbits ), tvectors, cmdline_opts )


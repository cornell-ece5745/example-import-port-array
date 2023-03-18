#=========================================================================
# PassThroughV2 unit test
#=========================================================================

import pytest
import random

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from PassThroughV2 import PassThroughV2

# Use the same seed so that debugging will be easier
random.seed(0xdeadbeef)

#-------------------------------------------------------------------------
# 4x 16-bit ports
#-------------------------------------------------------------------------

def test_directed( cmdline_opts ):
  run_test_vector_sim( PassThroughV2( 4, 16 ), [
      "in_                                          out*",
    [ concat( b16(0),  b16(0),  b16(0),  b16(0)  ), concat( b16(0),  b16(0),  b16(0),  b16(0)  ) ],
    [ concat( b16(1),  b16(0),  b16(3),  b16(3)  ), concat( b16(1),  b16(0),  b16(3),  b16(3)  ) ],
    [ concat( b16(-1), b16(42), b16(30), b16(25) ), concat( b16(-1), b16(42), b16(30), b16(25) ) ],
    [ concat( b16(42), b16(-1), b16(20), b16(16) ), concat( b16(42), b16(-1), b16(20), b16(16) ) ],
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

  hd_str  = 'in_ out*'

  # Generate test vectors
  tvectors = [ hd_str ]
  for i in range(nvectors):
    vector, tmp = [], []
    # Add input data
    for j in range(nports):
      tmp.append( bits_type( random.randint(0, 1024) ) )
    vector.append( concat( *tmp ) )
    # Add output data
    vector.append( vector[0] )
    tvectors.append( vector )

  run_test_vector_sim( PassThroughV2( nports, nbits ), tvectors, cmdline_opts )

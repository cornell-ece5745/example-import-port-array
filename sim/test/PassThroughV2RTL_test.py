import pytest
import random

from pymtl3 import *
from pymtl3.stdlib.test import run_test_vector_sim

from PassThroughV2RTL import PassThroughV2RTL

# Use the same seed so that debugging will be easier
random.seed(0xdeadbeef)

def test_directed( dump_vcd, test_verilog ):
  # 4 Bits16 ports
  run_test_vector_sim( PassThroughV2RTL( 4, 16 ), [
      "in_                                          out*",
    [ concat( b16(0), b16(0),  b16(0),  b16(0)   ), concat( b16(0),  b16(0),  b16(0),  b16(0) )  ],
    [ concat( b16(1), b16(0),  b16(3),  b16(3)   ), concat( b16(1),  b16(0),  b16(3),  b16(3) )  ],
    [ concat( b16(-1), b16(42), b16(30), b16(25) ), concat( b16(-1), b16(42), b16(30), b16(25) ) ],
    [ concat( b16(42), b16(-1), b16(20), b16(16) ), concat( b16(42), b16(-1), b16(20), b16(16) ) ],
  ], dump_vcd, test_verilog )

@pytest.mark.parametrize( "nports, nbits", [
    (2, 16), (2, 32), (2, 64),
    (3, 16), (3, 32), (3, 64),
    (4, 16), (4, 32), (4, 64),
  ]
)
def test_random( nports, nbits, dump_vcd, test_verilog ):
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

  run_test_vector_sim( PassThroughV2RTL( nports, nbits ), tvectors, dump_vcd, test_verilog )

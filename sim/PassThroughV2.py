#=========================================================================
# PassThroughV2
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class PassThroughV2( VerilogPlaceholder, Component ):
  def construct( s, nports, nbits ):
    s.in_ = InPort ( mk_bits(nbits * nports) )
    s.out = OutPort( mk_bits(nbits * nports) )


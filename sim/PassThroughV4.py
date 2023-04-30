#=========================================================================
# PassThroughV4
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

class PassThroughV4( VerilogPlaceholder, Component ):
  def construct( s, nports, nbits ):
    s.istream = [ IStreamIfc( mk_bits(nbits) ) for _ in range(nports) ]
    s.ostream = [ OStreamIfc( mk_bits(nbits) ) for _ in range(nports) ]


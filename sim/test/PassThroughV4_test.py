#=========================================================================
# PassThroughV4 unit test
#=========================================================================

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_sim
from pymtl3.stdlib.stream import StreamSourceFL, StreamSinkFL

from PassThroughV4 import PassThroughV4

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

class TestHarness( Component ):

  def construct( s ):

    # Instantiate models

    s.srcs  = [ StreamSourceFL( Bits16 ) for _ in range(2) ]
    s.dut   = PassThroughV4( nports=2, nbits=16 )
    s.sinks = [ StreamSinkFL( Bits16 ) for _ in range(2) ]

    # Connect

    for i in range(2):
      s.srcs[i].ostream //= s.dut.istream[i]
      s.dut.ostream[i]  //= s.sinks[i].istream

  def done( s ):
    for i in range(2):
      if not s.srcs[i].done() or not s.sinks[i].done():
        return False
    return True

  def line_trace( s ):
    srcs_str  = "|".join([ src.line_trace()  for src  in s.srcs  ])
    sinks_str = "|".join([ sink.line_trace() for sink in s.sinks ])
    return f"{srcs_str} > ({s.dut.line_trace()}) > {sinks_str}"

#-------------------------------------------------------------------------
# test_basic
#-------------------------------------------------------------------------

def test_basic( cmdline_opts ):

  th = TestHarness()

  msgs0 = [ b16( 1), b16( 3), b16( 2), b16( 9) ]
  msgs1 = [ b16(11), b16(13), b16(12), b16(19) ]

  th.set_param( "top.srcs[0].construct",  msgs=msgs0 )
  th.set_param( "top.srcs[1].construct",  msgs=msgs1 )
  th.set_param( "top.sinks[0].construct", msgs=msgs0 )
  th.set_param( "top.sinks[1].construct", msgs=msgs1 )

  th.elaborate()

  run_sim( th, cmdline_opts, duts=['dut'] )


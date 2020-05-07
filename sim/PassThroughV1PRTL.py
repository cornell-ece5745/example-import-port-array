from pymtl3 import *
from pymtl3.passes.backends.verilog import TranslationConfigs

class PassThroughV1PRTL( Component ):
  def construct( s, nports, nbits ):
    s.in_ = [ InPort( mk_bits(nbits) ) for _ in range(nports) ]
    s.out = [ OutPort( mk_bits(nbits) ) for _ in range(nports) ]

    for i in range(nports):
      s.out[i] //= s.in_[i]

    s.config_verilog_translate = TranslationConfigs(
        # You can leave this option unset if your rtl_language is Verilog
        translate = False,
        # Use the xRTL module name instead of xPRTL
        explicit_module_name = 'PassThroughV1RTL',
    )

  def line_trace( s ):
    inputs  = ', '.join( [ str(port) for port in s.in_ ] )
    outputs = ', '.join( [ str(port) for port in s.out ] )
    return f"{inputs} > {outputs}"

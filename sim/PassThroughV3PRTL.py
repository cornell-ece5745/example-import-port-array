from pymtl3 import *
from pymtl3.passes.backends.verilog import TranslationConfigs

class PassThroughV3PRTL( Component ):
  def construct( s, nports, nbits ):
    s.in_ = InPort( mk_bits(nbits * nports) )
    s.out = OutPort( mk_bits(nbits * nports) )

    s.out //= s.in_

    s.config_verilog_translate = TranslationConfigs(
        # You can leave this option unset if your rtl_language is Verilog
        translate = False,
        # Use the xRTL module name instead of xPRTL
        explicit_module_name = 'PassThroughV3RTL',
    )

  def line_trace( s ):
    return f"{s.in_} > {s.out}"

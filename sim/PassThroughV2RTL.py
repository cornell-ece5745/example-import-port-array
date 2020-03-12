from pymtl3 import *
from pymtl3.passes.backends.verilog import \
    VerilogPlaceholderConfigs, TranslationConfigs

# rtl_language = 'pymtl'
rtl_language = 'verilog'

class PassThroughV2VRTL( Component, Placeholder ):
  def construct( s, nports, nbits ):
    s.in_ = InPort( mk_bits(nbits * nports) )
    s.out = OutPort( mk_bits(nbits * nports) )

    from os import path
    s.config_placeholder = VerilogPlaceholderConfigs(
        src_file = path.dirname(__file__) + '/PassThroughV2VRTL.v',
        # If the top module name is the same as the component class
        # name it is safe to not set it.
        # top_module = 'PassThroughV2VRTL',
        params = {
          'num_ports' : nports,
          'bitwidth'  : nbits,
        },
        # The Verilog module does not have clk and reset
        has_clk = False,
        has_reset = False,
    )
    s.config_verilog_translate = TranslationConfigs(
        # You can leave this option unset if your rtl_language is Verilog
        translate = False,
        # Use the xRTL module name instead of xVRTL
        explicit_module_name = 'PassThroughV2RTL',
    )

# Check for the global rtl_language setting on CI
import sys
if hasattr( sys, '_called_from_test' ):
  if sys._pymtl_rtl_override:
    rtl_language = sys._pymtl_rtl_override

# Import based on rtl_language
if rtl_language == 'pymtl':
  from PassThroughV2PRTL import PassThroughV2PRTL as PassThroughV2RTL
elif rtl_language == 'verilog':
  PassThroughV2RTL = PassThroughV2VRTL
else:
  raise Exception("Invalid RTL language!")

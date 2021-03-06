from pymtl3 import *
from pymtl3.passes.backends.verilog import \
    VerilogPlaceholderConfigs, TranslationConfigs

rtl_language = 'pymtl'

class PassThroughV1VRTL( Component, Placeholder ):
  def construct( s, nports, nbits ):
    s.in_  = [ InPort( mk_bits(nbits) ) for _ in range(nports) ]
    s.out = [ OutPort( mk_bits(nbits) ) for _ in range(nports) ]

    from os import path
    s.config_placeholder = VerilogPlaceholderConfigs(
        src_file = path.dirname(__file__) + '/PassThroughV1VRTL.v',
        # If the top module name is the same as the component class
        # name it is safe to not set it.
        # top_module = 'PassThroughV1VRTL',
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
        explicit_module_name = 'PassThroughV1RTL',
    )

# Check for the global rtl_language setting on CI
import sys
if hasattr( sys, '_called_from_test' ):
  if sys._pymtl_rtl_override:
    rtl_language = sys._pymtl_rtl_override

# Import based on rtl_language
if rtl_language == 'pymtl':
  from PassThroughV1PRTL import PassThroughV1PRTL as PassThroughV1RTL
elif rtl_language == 'verilog':
  PassThroughV1RTL = PassThroughV1VRTL
else:
  raise Exception("Invalid RTL language!")

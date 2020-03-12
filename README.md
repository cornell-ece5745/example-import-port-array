# Verilog import examples
Examples about how to import a Verilog module with an array of ports

# Examples
This repo includes example modules PassThroughV1 ~ PassThroughV3 which pass the
data at the input ports on to the output ports. All modules are parametrized
by the bitwidth of the ports. PassThroughV1 uses an unpacked array of ports.
PassThroughV2 uses a packed array of ports. PassThroughV3 uses regular vector
ports.

`PassThroughV*RTL.py` includes the wrapper for that version of Verilog module
which is in `PassThroughV*VRTL.v`.

# How to run these examples
## Choose your RTL language
Set `rtl_language` in PassThroughV\*RTL.py to be either `pymtl` or `verilog`.

## Run the test
```
  % git clone git@github.com:cornell-ece5745/example-import-port-array.git
  % cd example-import-port-array
  % TOP=$PWD
  % mkdir $TOP/sim/test/build & cd $TOP/sim/test/build
  % pytest ../PassThroughV1RTL_test.py [--test-verilog] [--dump-vcd]
```
The options in brackets are optional.

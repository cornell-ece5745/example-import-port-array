# Verilog import examples

Three examples of how to import a Verilog module with an array of ports.

## Unpacked array of ports

You can find a Verilog module having unpacked array of ports at
`PassThroughV1.v`. Its wrapper is in file `PassThroughV1.py`. In this
case, the list of ports (`s.in_ = [ InPort( mk_bits(nbits) ) for _ in
range(nports) ]`) in the PyMTL wrapper will be mapped to an unpacked port
(`input logic [nbits-1:0] in_ [0:nports-1] `) of the Verilog module.

## Packed array of ports

You can find a Verilog module having unpacked array of ports at
`PassThroughV2.v`. Its wrapper is in file `PassThroughV2.py`. In this
case, the vector port (`s.in_ = InPort( mk_bits(nbits * nports) )`) in
the PyMTL wrapper will be mapped to a packed port (`input logic
[nports-1:0][nbits-1:0] in_ `) of the Verilog module. Note that in PyMTL3
a list of ports will be translated to an unpacked port array in Verilog.
That is why you need a vector port in PyMTL3 to correctly import a
packed array of ports in Verilog.

## Wide vector port

Of course, you may also pack every dimension of the array into a single
long vector. That implementation can be found in `PassThroughV3.v` whose
wrapper is in `PassThroughV3.py`. Note how you need to manually index
into the vector port in Verilog to extract the desired slice of the
signal. The PyMTL3 wrapper is the same as the one in `PassThroughV2.py`,
because now every dimension has been packed into the vector port.

## How to run these examples

```
  % git clone git@github.com:cornell-ece5745/example-import-port-array.git
  % cd example-import-port-array
  % mkdir -p sim/build
  % cd sim/build
  % pytest ../PassThroughV1_test.py -sv
  % pytest ../PassThroughV2_test.py -sv
  % pytest ../PassThroughV3_test.py -sv
```


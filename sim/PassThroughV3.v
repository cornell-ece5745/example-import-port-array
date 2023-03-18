//========================================================================
// PassThroughV2
//========================================================================

module PassThroughV3
#(
  parameter nports = 2,
  parameter nbits  = 32
)(
  input  logic [(nports*nbits)-1:0] in_,
  output logic [(nports*nbits)-1:0] out
);

  genvar i;

  generate
    for(i = 0; i < nports; i= i+1) begin
      assign out[i*nbits +: nbits] = in_[i*nbits +: nbits];
    end
  endgenerate

endmodule

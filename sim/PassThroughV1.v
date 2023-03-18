//========================================================================
// PassThroughV1
//========================================================================

module PassThroughV1
#(
  parameter nports = 2,
  parameter nbits  = 32
)(
  input  logic [nbits-1:0] in_ [0:nports-1],
  output logic [nbits-1:0] out [0:nports-1]
);

  genvar i;

  generate
    for(i = 0; i < nports; i= i+1) begin
      assign out[i] = in_[i];
    end
  endgenerate

endmodule

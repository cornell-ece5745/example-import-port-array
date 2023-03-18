//========================================================================
// PassThroughV2
//========================================================================

module PassThroughV2
#(
  parameter nports = 2,
  parameter nbits  = 32
)(
  input  logic [nports-1:0][nbits-1:0] in_,
  output logic [nports-1:0][nbits-1:0] out
);

  genvar i;

  generate
    for(i = 0; i < nports; i= i+1) begin
      assign out[i] = in_[i];
    end
  endgenerate

endmodule

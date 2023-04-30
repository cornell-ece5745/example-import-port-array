//========================================================================
// PassThroughV4
//========================================================================

module PassThroughV4
#(
  parameter nports = 2,
  parameter nbits  = 32
)(
  input  logic [nbits-1:0] istream_msg [nports],
  input  logic             istream_val [nports],
  output logic             istream_rdy [nports],

  output logic [nbits-1:0] ostream_msg [nports],
  output logic             ostream_val [nports],
  input  logic             ostream_rdy [nports]
);

  genvar i;

  generate
    for(i = 0; i < nports; i= i+1) begin
      assign ostream_msg[i] = istream_msg[i];
      assign ostream_val[i] = istream_val[i];
      assign istream_rdy[i] = ostream_rdy[i];
    end
  endgenerate

endmodule

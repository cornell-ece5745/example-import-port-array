module PassThroughV3VRTL
#(
  parameter num_ports = 2,
  parameter bitwidth  = 32
)
(
  input  logic [(num_ports*bitwidth)-1:0] in_,
  output logic [(num_ports*bitwidth)-1:0] out
);

  genvar i;

  generate
    for(i = 0; i < num_ports; i= i+1) begin
      assign out[i*bitwidth +: bitwidth] = in_[i*bitwidth +: bitwidth];
    end
  endgenerate

endmodule

# rotation_cube.souleiman

One way of changing the rotation of the cube is just to change the order of R_x, R_y and/or R_z in this part of code:

matrix_mult(R_x, R_z, MR)

matrix_mult(MR,R_y , MRF)

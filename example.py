import importlib.util
import numpy as np
import matplotlib.pyplot as plt


# === Import Lumerical API ===
module_name = "lumapi"
module_path = "C:/Program Files/Lumerical/v242/api/python/lumapi.py"
spec = importlib.util.spec_from_file_location(module_name, module_path)
lumapi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lumapi)


# === Spusti MODE ===
mode = lumapi.DEVICE()

mode.addmodelmaterial()
mode.set("name","tapper")
mode.set("color",np.array([1,0,0]))

mode.addmodelmaterial()
mode.set("name","BOX")
mode.set("color",np.array([0,1,0]))

x1 = 1e-6
x2 = 1e-6 + 10e-6
w_1 = 1e-6
w_2 = 10e-6

v = np.array([
      [x1, -w_1/2],
      [x1,  w_1/2],
      [x2,  w_2/2],
      [x2, -w_2/2]
])
 
mode.addpoly()
mode.set("name", "taper")
mode.set("vertices", v)
mode.set("material", "tapper")
mode.set("x",0)
mode.set("y",0)
mode.set("z min", 4.5e-6)
mode.set("z max", 4.5e-6 + 0.17e-6)
mode.set("color opacity", 1)



mode.addrect()
mode.set("name","BOX")
mode.set("x min",0)
mode.set("x max",12e-6)
mode.set("y", 0)
mode.set("y span", 10e-6)
mode.set("z min", 0e-6)
mode.set("z max", 4.5e-6)
mode.set("material", "BOX")
mode.set("detail",100)

mode.select("simulation region")
mode.set("x",0)
mode.set("x span",0)
mode.set("y", 0)
mode.set("y span", 0)
mode.set("z", 0)
mode.set("z span", 0)
mode.set("dimension","3D");


# import inverse_tapers

# inverse_tapers.nth_power(solver_object = mode, material = "tapper", 
#                          w_start = 1 , w_end = 10 , length = 10, 
#                          x = 1 , y = 0, z_min = 4.5, z_max =  4.5 + 0.4, n=5, num_of_points = 100)
# mode.set("detail",100)





# mode.addmaterialproperties("EM","Ag (Silver) - CRC");

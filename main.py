# Exercise 6
from pathlib import Path
import satpy as satpy
import utils as ut

#%%

# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]

files = satpy.find_files_and_readers(base_dir= "./data", reader="seviri_l1b_nc")

scn = satpy.Scene(filenames=files)
scn.attrs
scn.all_dataset_names()

#%%

# 2. Load the composites "natural_color" and "convection" [2P]

scn.available_composite_names()
scn.load(["natural_color"])
#scn.show("natural_color")
scn.load(["convection"])
#scn.show("convection")

#%%

# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 


ut.resample_area(scn, projection="laea", lat_origin =-3, lon_origin=23, width=500, height=500,
                  llx=-15E5, lly=-15E5 , urx=15E5, ury=15E5, saveFile="natural_color_Kongo.png",savePath = "./output", scene="natural_color",
                  area_id = "Demokratische Republik Kongo" , description = "Demokratische Republik Kongo in der Lambert Azimuthal Equal Area-Projektion", proj_id = "Demokratische Republik Kongo")

ut.resample_area(scn, projection="laea", lat_origin =-3, lon_origin=23, width=500, height=500,
                  llx=-15E5, lly=-15E5 , urx=15E5, ury=15E5, saveFile="convection_Kongo.png",savePath = "./output", scene="convection",
                  area_id = "Demokratische Republik Kongo" , description = "Demokratische Republik Kongo in der Lambert Azimuthal Equal Area-Projektion", proj_id = "Demokratische Republik Kongo")

#%%
# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]

# look at the function of task 3

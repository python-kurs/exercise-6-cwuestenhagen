# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def resample_area(scn, projection, lat_origin, lon_origin, width, height,
                  llx, lly, urx, ury, saveFile, savePath, scene,
                  area_id = "NA" , description = "NA", proj_id = "NA"):
    """
    resample a scene to a specific area and projection
    
    Parameters
    ----------
    scn : scene
    projection : projection of the loaded scene
    lat_origin : latitude of origin
    lon_origin : longitude of origin
    width : width of the resampled scene
    height : height of the resampled scene
    llx : projection x coordinate of lower left
    lly : projection y coordinate of lower left
    urx : projection x coordinate of upper right
    ury : projection y coordinate of upper right
    saveFile : name of the produced image
    savePath : path to the directory for produced image 
    scene : specific composit 
    area_id : id of the area
    description : description of the resampled area
    proj_id : id of the project
        
    Returns
    -------
    
    
    """
    from pyresample.geometry import AreaDefinition
    scn.load([scene])
    proj_dict = {"proj": projection, "lat_ts": lat_origin, "lon_0": lon_origin}
    area_extent = (llx,lly,urx,ury)
    area_def = AreaDefinition(area_id, proj_id, description, proj_dict, width, height, area_extent)
    local_scn = scn.resample(area_def)
    local_scn.save_dataset(dataset_id=scene,
                           writer="simple_image",
                           filename= saveFile,
                           base_dir= savePath)
    




        



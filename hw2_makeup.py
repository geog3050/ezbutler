###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Ezekiel Butler", "ezbutler"])

###################################################################### 
# Problem 1 (20 Points)
#
# This function reads all the feature classes in a workspace, and
# prints the number of feature classes by each shape type. For example,
# polygon: 3, polyline: 2, point: 4

###################################################################### 
def printNumberOfFeatureClassesByShapeType(workspace):
    import arcpy as arc
    arc.env.workspace=workspace
    poly=0
    line=0
    point=0
    multipoint=0
    multipatch=0
    fclist=arc.ListFeatureClasses()
    for fc in fclist:
        desc=arc.Describe(fc)
        if desc.shapetype=='Polygon':
            poly+=1
        elif desc.shapetype=='Polyline':
            line+=1
        elif desc.shapetype=='Point':
            point+=1
        elif desc.shapetype=='Multipoint':
            multipoint+=1
        elif desc.shapetype=='Multipatch':
            multipatch+=1
        else:
            raise Exception('Feature Class shape not recognized')
    print('Polygon:',poly,'Polyline:',line,'Point:',point,'Multipoint:',multipoint,'Multipatch:',multipatch)
###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the feature classes in a workspace, and
# prints the coordinate systems for each file

###################################################################### 
def printCoordinateSystems(workspace):
    import arcpy as arc
    arc.env.workspace=workspace
    fclist=ListFeatureClasses()
    for fc in fclist:
        SR= arc.Describe(fc).spatialReference
        if spatial_ref.name == "Unknown":
        print("{} has an unknown spatial reference".format(fc))
        else:
        print("{} : {}".format(fc, spatial_ref.name))

###################################################################### 
# Problem 3 (60 Points)
#
# Given two feature classes in a workspace:
# check whether their coordinate systems are
# the same, and if not convert the projection of one of them to the other.
# If one of them has a geographic coordinate system (GCS) and the other has
# a projected coordinate system (PCS), then convert the GCS to PCS. 

###################################################################### 
def autoConvertProjections(fc1, fc2, workspace):
    import arcpy as arc
    desc1 = arc.Describe(fc1)
    desc2 = arc.Describe(fc2)
    
    spatial_ref1 = desc1.spatialReference
    spatial_ref2 = desc2.spatialReference
    
    if spatial_ref1.name == spatial_ref2.name:
        print("Coordinate systems are the same.")
    else:
        if spatial_ref1.type == "Geographic":
            arc.management.Project(fc1, "projected_" + fc1, spatial_ref2)
        elif spatial_ref2.type == "Geographic":
                arc.management.Project(fc2, "projected_" + fc2, spatial_ref1)
        else:
                arc.management.Project(fc2, "projected_" + fc2, spatial_ref1)


######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')

def quiz6(input_geodatabase,fcPolygonA,fcPolygonB):
    ##import arcpy, sys, and get parameters
    import arcpy as arc
    import sys
    arc.env.workspace=input_geodatabase
    fcclass= fcPolygonA
    zone= fcPolygonB
    z_field=('Shape_Area')  
    
    ##exception handling
    #z_field check
    zfieldList=arc.ListFields(zone)
    testlist=[field.name for field in zfieldList]
    if z_field in testlist:
        print('Valid z_field')
        pass
    else:
          z_field= input('Enter field name for fcPolygonB shape area')  
            
    # Inputs can only be polygons
    zoneDesc = arcpy.Describe(zone)
    classDesc = arcpy.Describe(fcclass)
    if zoneDesc.shapeType != "Polygon" or classDesc.shapeType != "Polygon":
        print('One or both feature class inputs are not Polygons')
        sys.exit
        
        
    ##Create Instersection table
    table=arc.analysis.TabulateIntersection(zone,z_field,fcclass)
    
    
    ##join Percentage field fcPolygonB 
    arc.management.JoinField(zone,'OBJECTID',table,'OBJECTID',['PERCENTAGE'])
                                        



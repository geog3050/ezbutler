#import arcpy
import arcpy as arc

# set workspace and fc variable
arc.env.workspace="C:\\Users\\Zeke\\Downloads\\airports"

#clone og fc to make into buffer class
arc.management.CopyFeatures('airports.shp', 'airport_buffer')

#add buffer distance attribute to new fc
arc.management.AddField('airport_buffer','buf_dist','FLOAT')

#use cursor to select and fill buffer value
with arc.da.UpdateCursor('airport_buffer',['FEATURE','TOT_ENP','buf_dist']) as cursor:
    for row in cursor:
        if (row[0]=='Airport' and row[1]> 10000):
            row[2]=15000
        elif (row[0]=='Airport' and row[1]<= 10000):
            row[2]=10000
        elif (row[0]=='Seaplane Base' and row[1]>1000):
            row[2]=7500 
        cursor.updateRow(row)

#create buffer for fc using buffer distance attribute
arc.analysis.Buffer('airport_buffer','buffer_class','buf_dist')



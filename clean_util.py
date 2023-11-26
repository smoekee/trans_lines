import geopandas as gpd
import pandas as pd
import fiona


#filter shapefile attributes by specific columns
counties_gdf = gpd.read_file('trans_lines_shape.shp',
            include_fields=['ID', 'OWNER', 'SUB_1', 'SUB_2', 'geometry']                 
                             )

#write filtered dataframe to shapefile
counties_gdf.to_file('clean_trans_lines.shp')

print(counties_gdf)



### EXTRA UTILITIES ###

## for col in counties_gdf.columns:
#    print(col)

## pd.options.display.max_columns = None

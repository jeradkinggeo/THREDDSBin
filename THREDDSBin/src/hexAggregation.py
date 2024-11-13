import os
import arcpy

# Below function from -> https://github.com/KeithVanGraafeiland/OCIS/blob/main/OCIS_Hex_Sample.ipynb


# crf_directory = r"E:\gis_projects\Ocean and Coastal Information System\Raster_Subset\ssp370"
# h3_hex = r'E:\gis_projects\Ocean and Coastal Information System\sde_on_OCIS.sde\ocis.sde.H6'
# rasters = [f for f in os.listdir(crf_directory) if f.endswith('.crf') and os.path.isdir(os.path.join(crf_directory, f))]
# print(rasters)


def hexAgg(in_raster, in_hex, rasters, h3_hex):
    root_path = os.path.dirname(in_hex)
    #print(root_path)
    hex_level = str(os.path.splitext(in_hex)[-1].split('.')[-1])
    #print(hex_level)

    for raster in rasters:
        var_name = raster.replace('_ssp370_2050', '').replace('.crf', '')  
        sample_table = os.path.join(root_path, hex_level + '_sample_' + var_name)
        print(sample_table)
        with arcpy.EnvManager(parallelProcessingFactor="90%"):
            print(raster)
            crf = os.path.join(crf_directory, raster)
            arcpy.sa.Sample(
                in_rasters=crf,
                in_location_data=in_hex,
                out_table=sample_table,
                resampling_type="NEAREST",
                unique_id_field="objectid",
                process_as_multidimensional="CURRENT_SLICE",
                acquisition_definition=None,
                statistics_type="MEAN",
                percentile_value=None,
                buffer_distance=None,
                layout="ROW_WISE",
                generate_feature_class="TABLE"
            )
            arcpy.management.JoinField(
                in_data=sample_table,
                in_field="LOCATIONID",
                join_table=in_hex,
                join_field="objectid",
                fields="grid_id",
                fm_option="NOT_USE_FM",
                field_mapping=None,
                index_join_fields="NO_INDEXES"
            )
            arcpy.management.DeleteField(
                in_table=sample_table,
                drop_field="LOCATIONID;X;Y",
                method="DELETE_FIELDS"
            )
        print("Done processing....." + raster)
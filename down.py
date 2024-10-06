import openeo

def download_eo_data(output_file):
    """Download EO data from OpenEO for the specified date range and spatial extent."""
    # Connect to the Copernicus Data Space Ecosystem
    connection = openeo.connect(url="openeo.dataspace.copernicus.eu")
    connection.authenticate_oidc()

    # Specify the collection and bands
    collection = "SENTINEL2_L2A"
    bands = ["B03", "B04", "B08", "SCL"]

    # Load data
    print("Loading data...")
    eo_cube = connection.load_collection(
        collection,
        temporal_extent=("2023-01-01", "2023-01-31"),
        spatial_extent= {
            "west": -8.84,
            "south": 40.43,
            "east": -8.56,
            "north": 40.88,
            "crs": "EPSG:4326",
        },
        bands=bands,
        max_cloud_cover=50,
    )

    # Apply cloud masking
    SCL = eo_cube.band("SCL")
    cloud_mask = (SCL == 3) | (SCL == 8) | (SCL == 9)
    cloud_mask = cloud_mask.resample_cube_spatial(eo_cube)
    eo_cube = eo_cube.mask(cloud_mask)

    # Calculate weekly mean
    eo_cube = eo_cube.aggregate_temporal_period(period="week", reducer="mean")

    print(f"Downloading data to {output_file}...")
    eo_cube.download(output_file)

    print("Download complete.")


download_eo_data("data/eo_weekly_data.nc")

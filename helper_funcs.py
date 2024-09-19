from pandas import read_csv


# helper functions
def calculate_title_padding(title: str, subtitle: str) -> str:
    # this func helps with formatting logger messages
    length = len(title)-len(subtitle)
    if length<=0:
        return '-'*15 + subtitle + '-'*15
    num: int = int(length/2)
    if length%2 == 0:
        return '-'*num + subtitle + '-'*num
    else:
        return '-'*num + subtitle + '-'*(num+1)
    

def csv_col_reader(*cols: str):
    # this decorator helps retrieving additional columns from the metadata csv file
    # cols: csv column names to be added to the returned tuple
    def inner(func):

        def wrapper(metadata_path: str, raw_dir: str):
            if len(cols) != 0:
                df = read_csv(metadata_path)
                added_info: list = [df[col] for col in cols]
                csv_info, path_info = func(metadata_path, raw_dir)
                emdbs, pdbs, resolutions, emdb_ids = csv_info
                csv_info_with_added_cols = (emdbs, pdbs, resolutions, emdb_ids, *added_info)
                return csv_info_with_added_cols, path_info
            else:
                return func(metadata_path, raw_dir)
        return wrapper
    
    return inner


def read_csv_info(csv_path, raw_dir):
    df = read_csv(csv_path)
    emdbs, pdbs = df["emdb_id"], df["fitted_pdbs"]
    resolutions = df["resolution"].astype(str)
    emdb_ids = [emdb.split("-")[1] for emdb in emdbs]
    folders = [
        f"{emdb}_re_{resolution}"
        for emdb, resolution in zip(emdbs, resolutions)
    ]
    raw_maps = [f"emd_{emdb_id}.map" for emdb_id in emdb_ids]
    models = [f"{pdb}.cif" for pdb in pdbs]

    raw_map_paths = [
        f"{raw_dir}/{folder}/{raw_map}"
        for folder, raw_map in zip(folders, raw_maps)
    ]
    model_paths = [
        f"{raw_dir}/{folder}/{model}"
        for folder, model in zip(folders, models)
    ]
    normalized_map_paths = [
        f"{raw_dir}/{folder}/{raw_map_path.split('/')[-1].split('.')[0]}_normalized.mrc"
        for folder, raw_map_path in zip(folders, raw_map_paths)
    ]

    csv_info = (emdbs, pdbs, resolutions, emdb_ids)
    path_info = (raw_map_paths, model_paths, normalized_map_paths)
    return csv_info, path_info

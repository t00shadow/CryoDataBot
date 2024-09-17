# https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{emdb}/map/emd_{emdb_id}.map.gz"

# https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-3145/map/emd_3145.map.gz"
# https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-27278/map/emd_27278.map.gz"
# https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-26861/map/emd_26861.map.gz"



import urllib.request
import gzip
import shutil

urllib.request.urlretrieve(emdb_fetch_link, raw_map_gz_path)
            with gzip.open(raw_map_gz_path, 'rb') as f_in:
                with open(raw_map_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
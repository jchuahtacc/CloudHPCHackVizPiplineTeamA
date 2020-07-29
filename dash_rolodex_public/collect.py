import shutil
import os
import traceback
import pathlib
import json
import pkgutil
import importlib
from loader import thumbnail_path

metadata = { }
assets_path = pathlib.Path(__file__).parent.joinpath(
    'assets'
)
# For each package, find a thumbnail in that directory
for p in pkgutil.iter_modules(path=['./apps']):
    try:
        metapath = pathlib.Path(__file__).parent.joinpath(
            'apps', 
            p.name, 
            'dashmeta.json'.format(p.name)
        )
        with open(metapath, 'r') as metafile:
            meta = json.load(metafile)
            metadata[p.name] = meta

        if meta["thumbnail"]:
            source = pathlib.Path(__file__).parent.joinpath(
                'apps',
                p.name,
                meta["thumbnail"]
            )
            destination = assets_path.joinpath(
                thumbnail_path(p.name, meta["thumbnail"])
            )
            if (os.path.exists(source)):
                shutil.copy(source, destination)
                print("Copied {} to {}".format(source, destination))
            else:
                print("Thumbnail {} not found".format(source))
        else:
            print("No thumbnail metadata for {}".format(p.name))
    except:
        print("Error while processing metadata from {}".format(p.name))
        traceback.print_exc()

    with open("dashmeta.json", "w") as meta_output:
        json.dump(metadata, meta_output)

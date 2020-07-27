# Dash Rolodex

This project creates a token/session protected Dash Rolodex server, allowing individual dash projects to be served via the Rolodex, while still maintaining the ability to locally develop and serve child dash projects. Dash applications will appear in a "gallery".

## Get it Running

#### From this directory...

Create a Python 3 virtual environment

```
python3 -m venv ~/rolodex_env
```

Activate the virtual environment (every time you want to run it)

```
source ~/rolodex_env/bin/activate
```

Install the requirements (before you run it this first time)

```
pip install -r requirements.txt
```

**Start the server via gunicorn:**

```
gunicorn -w 8 -b :8050 app:server
```

Browse to the server, with the default token at address [http://localhost:8050/?token=abcde](http://localhost:8050/?token=abcde)


## Adding Dash Applications

Plot.ly Dash applications can be placed in the [`./apps`](./apps) directory. You may store
metadata information in the root of the application, in the file `dashmeta.json`. Here is an
example metadata file:

```
{
    "name": "My Dash App",
    "description": "This Dash app's long description",
    "thumbnail": "thumbnail.png"
}
```

## Configuring Rolodex

The [`gallerymeta.json`](./gallerymeta.json) file contains configuration options. Here is an example:
h
```
{
    "name": "COVID19 Dash Gallery"
}
```

 In addition,
thumbnail files and Dash application metadata must be collected into a [`dashmeta.json`](./dashmeta.json)
file. The easiest way to do that is to run:

```
python collect.py
```

This will scan for Dash apps, read their individual `dashmeta.json` files and aggregate them, and
copy any thumbnail files into the [`./assets'](./assets) folder.

You may also recursively search for and install all `requirements.txt` files by running
[`./install_all_requirements.sh`](./install_merged_requirements.s)

## Dash Application Format

Your Plot.ly Dash applications must have their application code in `app.py`, with `app` as the main
Dash application object. The root of your Dash application must also have an empty `__init__.py` file.
Rolodex discovers your Dash applications as WSGI applications, via Python's `pkgutil` package.

### Dash application initialization

Dash objects must be initialized with their package name appended to the `requests_pathname_prefix` argument, and an explicit path provided to the `assets_path` argument. 

Here is example code:

```
# Create path arguments for Dash object
ASSETS_PATH = pathlib.Path(__file__).parent.joinpath("assets")
REQUESTS_PATHNAME_PREFIX = os.environ.get("REQUESTS_PATHNAME_PREFIX", "/")

if __name__ == "__main__":
    # If running in debug mode independent of rolodex start with no options
    app = dash.Dash(
        __name__,
        assets_folder=ASSETS_PATH
    )
else:
    # If served from rolodex/gunicorn, change options based on package name
    package_tokens = __package__.split('.')
    if len(package_tokens) > 1:
        REQUESTS_PATHNAME_PREFIX += "{}/".format(package_tokens[-1])

    app = dash.Dash(
        __name__,
        assets_folder=ASSETS_PATH,
        requests_pathname_prefix=REQUESTS_PATHNAME_PREFIX,
    )
```

### Local Module Imports

Due to the way that WSGI apps are served, you will need to modify the way you import
local python modules based on if your app is running as a standalone development server
or being served by Rolodex as a WSGI app.

Here is example code:

```
import importlib

if __package__ is None or len(__package__) == 0:
    # Importing local module mymodule via standard import
    import mymodule
else:
    # Importing local module tapis_dash via import lib
    mymodule = importlib.import_module('.mymodule', package=__package__)
```

## Production Environment Variables

You may use the following environment variables:

- `export GALLERY_SESSION_NAME=session`

   Sets the session cookie name. If both `GALLERY_SESSION_NAME`
   and `GALLERY_SESSION_TOKEN` environment variables are present,
   then the gallery will add a session middleware that returns 401 
   on any requests to the gallery that do not include `/?token=GALLERY_SESSION_TOKEN`. The default value is `session`. In a production environment, You may set this to a random value, with:
   
   `export GALLERY_SESSION_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)`
   
- `export GALLERY_SESSION_TOKEN=abcde`

   Sets the session token value. In a production environment, you may this to a random value, with:
   
   `export GALLERY_SESSION_TOKEN=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)`
   
- `export REQUESTS_PATHNAME_PREFIX=/prefix/`
 
  Useful for the `requests_pathname_prefix` named argument for Dash applications


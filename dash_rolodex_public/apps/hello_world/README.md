# Public facing COVID-19 Projections 

## Running locally

Create a Python virtual environment and install the requirements:

```
python3 -m venv ~/dash_env
source ~/dash_env/bin/activate
python3 -m pip install --no-cache -r requirements.txt
```

You may run a local app development server using:

```
python3 app.py
```

This will output the URL (including port) of your local development server.

## Adding images

Put all image files in [`./assets`](./assets). Add additional entries to [`./data/images.json`](./data/images.json).

# Pokemon API

An API built in python with fastAPI.

View available enpoints on the [docs page](https://pokiapi.deta.dev/docs).

View API in action on my live [pokedex app](https://misqke-pokedex.netlify.app/).

## To Clone

built on python v3.10.6

clone the repository

```
git clone https://github.com/misqke/fastapi_pokiapi.git
```

you will need fastAPI and uvicorn installed. If you don't already have them run:

```
pip install fastapi
pip install uvicorn
```

to run localy:

```
uvicorn main:app --reload
```

You also may need to adjust the origins variable in main.py depending on what port you are connecting from.

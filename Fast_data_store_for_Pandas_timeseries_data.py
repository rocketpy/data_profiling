#  PyStore - Fast data store for Pandas timeseries data.

# PyPi: https://pypi.org/project/PyStore/
# Github: https://github.com/ranaroussi/pystore

# pip install PyStore

# Requirements:
"""
    Python 2.7 or Python > 3.5
    Pandas
    Numpy
    Dask
    Fastparquet
    Snappy (Google’s compression/decompression library)
    multitasking
"""

# Dependencies:
# PyStore uses Snappy, a fast and efficient compression/decompression library from Google.
# You'll need to install Snappy on your system before installing PyStore.

# Snappy:   http://google.github.io/snappy/
# PyPi: https://pypi.org/project/python-snappy/

# Info
"""
PyStore is a simple (yet powerful) datastore for Pandas dataframes,
and while it can store any Pandas object, it was designed with storing timeseries data in mind.

It’s built on top of Pandas, Numpy, Dask, and Parquet (via Fastparquet), 
to provide an easy to use datastore for Python developers that can easily query millions of rows per second per client.
"""


# Using PyStore
import pystore
import quandl

# Set storage path (optional)
# Defaults to `~/pystore` or `PYSTORE_PATH` environment variable (if set)
pystore.set_path("~/pystore")

# List stores
pystore.list_stores()

# Connect to datastore (create it if not exist)
store = pystore.store('mydatastore')

# List existing collections
store.list_collections()

# Access a collection (create it if not exist)
collection = store.collection('NASDAQ')

# List items in collection
collection.list_items()

# Load some data from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken="your token here")

# Store the first 100 rows of the data in the collection under "AAPL"
collection.write('AAPL', aapl[:100], metadata={'source': 'Quandl'})

# Reading the item's data
item = collection.item('AAPL')
data = item.data  # <-- Dask dataframe (see dask.pydata.org)
metadata = item.metadata
df = item.to_pandas()

# Append the rest of the rows to the "AAPL" item
collection.append('AAPL', aapl[100:])

# Reading the item's data
item = collection.item('AAPL')
data = item.data
metadata = item.metadata
df = item.to_pandas()


# --- Query functionality ---

# Query avaialable symbols based on metadata
collection.list_items(some_key='some_value', other_key='other_value')


# --- Snapshot functionality ---

# Snapshot a collection
# (Point-in-time named reference for all current symbols in a collection)
collection.create_snapshot('snapshot_name')

# List available snapshots
collection.list_snapshots()

# Get a version of a symbol given a snapshot name
collection.item('AAPL', snapshot='snapshot_name')

# Delete a collection snapshot
collection.delete_snapshot('snapshot_name')



# Delete the item from the current version
collection.delete_item('AAPL')

# Delete the collection
store.delete_collection('NASDAQ')


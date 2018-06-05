import h5py

from

with h5py.File('/home/alexpetit/Databases/mytestfile.hdf5', 'w') as f:
    dset = f.create_dataset('mydataset', (100,), dtype='i')

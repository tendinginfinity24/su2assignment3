import sys
try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
except ImportError:
    comm = 0

import pysu2

# Define your config file name here (ensure it matches your actual file)
config_filename = "flatplate.cfg" 

print(f"Initializing SU2 with {config_filename}...")
# Create the SU2 driver (1 zone, using the communicator)
driver = pysu2.CSinglezoneDriver(config_filename, 1, comm)

print("Starting the solver...")
# This will run the actual CFD iterations
driver.StartSolver()

print("Writing output files and finalizing...")
driver.Postprocess()
driver.Finalize()

print("Simulation finished successfully!")
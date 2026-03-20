Objective: verify the functionality of the SU2 Python wrapper

Implementation:
a python script was written using CSinglezoneDriver from pysu2, it imports the SU2 module and calls the solver, instead of using .cfg, we use this to run the simulation

Results:
from the history.csv file, we can see that the simulation ran almost 6000 iters and then the residuals plateaued
temp vs y plot:
<img width="723" height="753" alt="{A98676A9-2219-41BF-8819-2B8492F78972}" src="https://github.com/user-attachments/assets/a8eecb29-ab4c-44d6-ad9d-32b6b35fc7ed" />

mach contour:
<img width="1470" height="764" alt="machassignment3" src="https://github.com/user-attachments/assets/d8565e12-e015-4524-8b0b-de1320858165" />


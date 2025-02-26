# Tie Resolution Algorithm: a Reference Implementation

This folder contains simple implementation of the algorithm for tie
resolution verification.

Consult [the documentation](../tie-resolution.md) for the details of the
algorithm.


## Content of this folder

* **[tie_resolution.py](tie_resolution.py)**

  The implementation of the tie resolution procedure.

* **[test_tie_resolution.py](test_tie_resolution.py)**

   A simple test. You can execute it by:

   ```
   python3 -m unittest test_tie_resolution
   ```
  
* **[tie_resolution_cli.py](tie_resolution_cli.py)**

  A simple command-line application that calls the tie resolution procedure
  with the provided command-line arguments and prints the computed result
  (computed permutation). See below for the usage.


## Usage

To generate the result of the tie resolution algorithm, in order to resolve

 - ties of `N` candidates/choices with equal number of votes, 
 - in the  ballot with identifier `BALLOT-ID` and voting list with 
   identifier `LIST-ID`, 
 - using the system seed `SYSTEM-SEED` and user seed `USER_SEED`, 

call:

```
python3 tie_resolution_cli SYSTEM-SEED USER-SEED BALLOT-ID LIST-ID N
```

This command will compute and output the permutation of the integers `0` ..
`N-1` which determines the (re)ordering of the `N` candidates with the same
number of votes (on the given ballot/list).

An auditor can now check that this permutation is the one used by the POLYAS
system to determine the candidates order.


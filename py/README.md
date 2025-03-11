# Tie Resolution Algorithm: a Reference Implementation

This folder contains simple implementation of the algorithm for tie
resolution verification.

Consult [the documentation](../tie-resolution.md) for the details of the
algorithm.


Content of this folder
--------------------------------------------------------------------------

* **[tie_resolution.py](tie_resolution.py)**

  An implementation of the core tie resolution algorithm.

* **[test_tie_resolution.py](test_tie_resolution.py)**

   A simple test for the core algorithm. Can be executed it by:

   ```
   python3 -m unittest test_tie_resolution
   ```

* **[tie_resolver.py](tie_resolver.py)**

  Defines class `TieResolver` which can be used to to apply the tie resolution
  algorithm (defined in [tie_resolution.py](tie_resolution.py) to
  the given user data.  It is used by
  [use_tie_resolution.py](use_tie_resolution.py) (see below).

* **[use_tie_resolution.py](use_tie_resolution.py)**

  An example script which applies the tie resulution (using class
  `TieResolver` defined in [tie_resolver.py](tie_resolver.py)) to specific
  data.

  It has the following form:

  ```python
    resolver = TieResolver(
        system_seed = "...", system_commitment = "...", user_seed =  "..."
    )
    resolver.apply(
        ballot_id = "...", list_id = "...", candidates = [ ... ]
    )
  ```

  The user/auditor can modify the data in this script (system seed/commitment,
  user seed, list/ballot identifiers, and the list of candidates in the
  original order) and run it by:
  ```
  python3 use_tie_resolution.py
  ```


Usage
--------------------------------------------------------------------------

In order to resolve ties in the given ballot/candidate list

1. Open file `use_tie_resolution.py` and insert there your data:
   
   - the system seed,
   - the system commitment,
   - the user commitment,
   - ballot identifier,
   - candidate list identifier,
   - the list of the candidates/choices on this list in the original order (as
     displayed on the ballot)

2. Run `python3 use_tie_resolution.py`.
 
   The script will check the commitment and output a rerdered list of
   candidates.

3. Use the reordered list of candidates to determine winners whenever two or
   more candidates received the same number of votes (the candidate which is
   higher in the reordered list wins). See the example below.


Example
--------------------------------------------------------------------------

Let us assume that, on the ballot with identifier `ballot-1` and candidate
list with identifier `list-9`, votes were allocated to the candidates in the
followin way:

| Candidate | Votes |
| :-------: | :---: |
| A         | 12    |
| B         | 15    |
| C         | 15    |
| D         | 12    |
| E         | 15    |

We have two tied groups:
 * in group {B, C, E}, each candidate received 15 votes,
 * in group {A, D}, each candidate received 12 votes.

To resolve these two ties, we should change the data in the
`use_tie_resolution.py` scrip as follows, where the seeds and the commitment
are taken from the audit data:

```python
resolver = TieResolver(
    system_seed = "FAPJC6NH-2B6T64X7-E3BLFJJ2-OKPV4SJI-SMAMM4CE-HO7IXRQ7-BWPVYW2S",
    system_commitment = "QYJ6AT-TBT3M5-6V6H3J-BTH67E-DQ5LDH-STYGIU-47DRIS-W7KA3X-FDVQ",
    user_seed =  "11155"
)

resolver.apply(
    ballot_id = "ballot-1", 
    list_id = "list-9", 
    candidates = [ "A", "B", "C", "D", "E" ]
)

```

Running this script, we obtain the reordered list:

```
    - C
    - D
    - B
    - E
    - A
```

This reordered list determines candidates ranking within each tie groups:


| Candidate | Votes | Ranking |
| :-------: | :---: | :-----: |
| C         | 15    | 1       |
| B         | 15    | 2       |
| E         | 15    | 3       |
| D         | 12    | 4       |
| A         | 12    | 5       |


For instance, D is placed above A, because (they have the same number of
votes) and D is above A in the returned reordered list.


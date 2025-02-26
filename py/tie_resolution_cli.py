import sys

from tie_resolution import tie_resolution

systemSeed = sys.argv[1]
userSeed = sys.argv[2]
ballotId = sys.argv[3]
listId = sys.argv[4]
tiedCandidates = sys.argv[5]

resolution = tie_resolution(
    s_seed = systemSeed,
    u_seed = userSeed,
    ballot_id = ballotId,
    list_id = listId,
    tied_candidates = int(tiedCandidates),
)

print(resolution)
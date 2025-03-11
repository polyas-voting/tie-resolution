from tie_resolution import tie_resolution
import hashlib
import base64  # pybase64

class TieResolver:

    def __init__(self, system_seed: str, system_commitment: str, user_seed: str):
        self.system_seed = system_seed
        self.system_commitment = system_commitment
        self.user_seed = user_seed

    def apply(self, ballot_id: str, list_id: str, candidates: list[str]):
        self.check_commitment()
        self.display_resolution(ballot_id, list_id, candidates)

    def check_commitment(self):
        print("SEEDS")
        print(f"    System commitment = {self.system_commitment}")
        print(f"    System seed = {self.system_seed}")
        print(f"    User seed = {self.user_seed}")
        print()
        expected_commitment = commitment(self.system_seed)
        normalised_system_commitment = self.system_commitment.replace("-", "")
        if expected_commitment == normalised_system_commitment:
            print(f"  ✓ System commitment is correct (it matches the system seed)")
        else:
            print("✗ INCORRECT SYSTEM COMMITMENT")
            print(f"    - Expected: {expected_commitment}")
            print(f"    - Given:    {normalised_system_commitment}")
            exit(-1)
        
    def display_resolution(self, ballot_id: str, list_id: str, candidates: list[str]):
        resolution = tie_resolution(
            s_seed = self.system_seed,
            u_seed = self.user_seed,
            ballot_id = ballot_id,
            list_id = list_id,
            tied_candidates = len(candidates),
        )
        print()
        print(f"Reordered candidates for ballot {ballot_id} and list {list_id}:")
        for i in range(len(candidates)):
            print(f"    - {candidates[resolution[i]]}")
        
def commitment(data: str):
    hashed_data = hashlib.sha256(data.encode()).digest()
    b32_encoded = base64.b32encode(hashed_data).decode()
    return b32_encoded.rstrip('=')


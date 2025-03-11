from tie_resolver import TieResolver

resolver = TieResolver(
    system_seed = "FAPJC6NH-2B6T64X7-E3BLFJJ2-OKPV4SJI-SMAMM4CE-HO7IXRQ7-BWPVYW2S",
    system_commitment = "QYJ6AT-TBT3M5-6V6H3J-BTH67E-DQ5LDH-STYGIU-47DRIS-W7KA3X-FDVQ",
    user_seed =  "11155"
)

resolver.apply(
    ballot_id = "ballot-1", 
    list_id = "list-9", 
    candidates = [
        "A", "B", "C", "D", "E"
    ]
)


"""
Example: ARAW Search on "I need $50k in 6 months for mom's surgery"

Demonstrates the recursive branching search.
"""

from araw_engine import ARAWEngine, BranchType, NodeStatus


def run_surgery_example():
    # Create a new search
    engine = ARAWEngine("surgery_example.db")

    # Initial claim
    root_id = engine.create_search(
        "I need $50k in 6 months for mom's surgery",
        metadata={"user_context": "patient_family", "created_by": "example"}
    )
    print(f"Created search: {root_id}")

    # ============================================
    # DEPTH 1: Branch on main claims
    # ============================================

    # Claim 1: "Mom needs surgery"
    claim1_id = engine.add_node(
        parent_id=root_id,
        claim="Mom needs surgery",
        branch_type=BranchType.ROOT,  # This is a claim to be branched
        leverage_score=0.9  # High leverage - if wrong, changes everything
    )

    engine.branch(
        node_id=claim1_id,
        assume_right_claim="Surgery is necessary - proceed with funding",
        assume_wrong_claim="Surgery might not be necessary",
        alternatives=[
            "Other treatments exist (medication, therapy, lifestyle)",
            "Condition might resolve on its own",
            "Diagnosis might be incorrect",
            "Different procedure might work"
        ],
        leverage_score=0.9
    )

    # Claim 2: "$50k is the cost"
    claim2_id = engine.add_node(
        parent_id=root_id,
        claim="$50k is the cost",
        branch_type=BranchType.ROOT,
        leverage_score=0.7
    )

    engine.branch(
        node_id=claim2_id,
        assume_right_claim="Need to acquire $50k",
        assume_wrong_claim="Cost might be different",
        alternatives=[
            "Other hospitals might be cheaper",
            "Insurance might cover part/all",
            "Payment plans available",
            "Medical tourism options",
            "Negotiate with hospital"
        ],
        leverage_score=0.7
    )

    # Claim 3: "6 months is the timeline"
    claim3_id = engine.add_node(
        parent_id=root_id,
        claim="6 months is the timeline",
        branch_type=BranchType.ROOT,
        leverage_score=0.5
    )

    engine.branch(
        node_id=claim3_id,
        assume_right_claim="Must act within 6 months",
        assume_wrong_claim="Timeline might be flexible",
        alternatives=[
            "Could be sooner (condition worsening)",
            "Could be later (more time to prepare)",
            "Timeline is arbitrary, not medical"
        ],
        leverage_score=0.5
    )

    # Claim 4: "I must provide the money"
    claim4_id = engine.add_node(
        parent_id=root_id,
        claim="I must provide the money",
        branch_type=BranchType.ROOT,
        leverage_score=0.8
    )

    engine.branch(
        node_id=claim4_id,
        assume_right_claim="I need to earn/acquire $50k myself",
        assume_wrong_claim="Others might contribute",
        alternatives=[
            "Family members can help",
            "Insurance coverage",
            "Hospital financial assistance",
            "Crowdfunding",
            "Government assistance programs",
            "Medical loans",
            "Charity organizations"
        ],
        leverage_score=0.8
    )

    # ============================================
    # DEPTH 2: Branch deeper on "Surgery might not be necessary"
    # ============================================

    # Find the "assume wrong" node for surgery
    children = engine.get_children(claim1_id)
    surgery_wrong_node = None
    for child in children:
        if child.branch_type == "assume_wrong":
            surgery_wrong_node = child
            break

    if surgery_wrong_node:
        # Branch on "Diagnosis might be incorrect"
        diagnosis_claim_id = engine.add_node(
            parent_id=surgery_wrong_node.id,
            claim="Diagnosis might be incorrect",
            branch_type=BranchType.ASSUME_WRONG,
            leverage_score=0.85
        )

        engine.branch(
            node_id=diagnosis_claim_id,
            assume_right_claim="Diagnosis is correct - surgery is the treatment",
            assume_wrong_claim="Diagnosis might be wrong",
            alternatives=[
                "Get second opinion",
                "Different diagnostic tests",
                "Specialist consultation"
            ],
            leverage_score=0.85
        )

        # ============================================
        # DEPTH 3: Branch on "Doctor made the diagnosis"
        # ============================================

        # Find the assume_wrong branch for diagnosis
        diagnosis_children = engine.get_children(diagnosis_claim_id)
        diagnosis_wrong = None
        for child in diagnosis_children:
            if child.branch_type == "assume_wrong":
                diagnosis_wrong = child
                break

        if diagnosis_wrong:
            doctor_claim_id = engine.add_node(
                parent_id=diagnosis_wrong.id,
                claim="Doctor's diagnosis is reliable",
                branch_type=BranchType.ASSUME_WRONG,
                leverage_score=0.7
            )

            engine.branch(
                node_id=doctor_claim_id,
                assume_right_claim="Doctor is reliable - trust diagnosis",
                assume_wrong_claim="Doctor's reliability uncertain",
                alternatives=[
                    "Doctor was uncertain/guessing",
                    "Doctor lacks experience with this condition",
                    "Doctor's training might be insufficient",
                    "Diagnostic equipment might be faulty"
                ],
                leverage_score=0.7
            )

            # ============================================
            # DEPTH 4: Branch on "Doctor's training"
            # ============================================

            doctor_children = engine.get_children(doctor_claim_id)
            doctor_wrong = None
            for child in doctor_children:
                if child.branch_type == "assume_wrong":
                    doctor_wrong = child
                    break

            if doctor_wrong:
                training_claim_id = engine.add_node(
                    parent_id=doctor_wrong.id,
                    claim="Doctor's training was adequate",
                    branch_type=BranchType.ASSUME_WRONG,
                    leverage_score=0.5
                )

                engine.branch(
                    node_id=training_claim_id,
                    assume_right_claim="Training was adequate - doctor is competent",
                    assume_wrong_claim="Training might be inadequate",
                    alternatives=[
                        "Medical school quality varies",
                        "Training might be outdated",
                        "Specialty mismatch"
                    ],
                    leverage_score=0.5
                )

    # ============================================
    # PRINT RESULTS
    # ============================================

    print("\n" + "=" * 60)
    print("ARAW SEARCH RESULTS")
    print("=" * 60)

    stats = engine.get_stats()
    print(f"\nStatistics:")
    print(f"  Total nodes: {stats['total_nodes']}")
    print(f"  Max depth: {stats['max_depth']}")
    print(f"  By status: {stats['by_status']}")
    print(f"  Total alternatives: {stats['total_alternatives']}")

    print(f"\n\nHigh Leverage Nodes (>= 0.7):")
    print("-" * 60)
    high_leverage = engine.get_high_leverage(min_score=0.7)
    for node in high_leverage:
        print(f"  [{node.leverage_score:.2f}] {node.claim[:55]}")

    print(f"\n\nUnexplored Nodes:")
    print("-" * 60)
    unexplored = engine.get_unexplored(limit=15)
    for node in unexplored:
        print(f"  [depth={node.depth}] {node.claim[:55]}")

    print(f"\n\nTree Structure (depth 0-4):")
    print("-" * 60)
    tree = engine.export_tree()
    print_tree(tree, max_depth=4)

    # Save full export
    engine.export_json("surgery_example_export.json")
    print(f"\n\nFull tree exported to: surgery_example_export.json")

    engine.close()


def print_tree(node: dict, depth: int = 0, max_depth: int = 3, prefix: str = "", is_last: bool = True):
    """Pretty print a tree"""
    if depth > max_depth:
        if node.get('children'):
            print(f"{prefix}{'└── ' if is_last else '├── '}... ({len(node.get('children', []))} more children)")
        return

    # Branch type indicator
    branch_type = node.get('branch_type', '')
    if branch_type == 'assume_right':
        indicator = "[R] "
    elif branch_type == 'assume_wrong':
        indicator = "[W] "
    else:
        indicator = ""

    claim = node.get('claim', 'Unknown')[:55]
    leverage = node.get('leverage_score', 0)

    if depth == 0:
        print(f"{indicator}{claim}")
    else:
        connector = "└── " if is_last else "├── "
        leverage_str = f" ({leverage:.1f})" if leverage > 0 else ""
        print(f"{prefix}{connector}{indicator}{claim}{leverage_str}")

    children = node.get('children', [])
    for i, child in enumerate(children):
        child_is_last = i == len(children) - 1
        new_prefix = prefix + ("    " if is_last else "│   ")
        print_tree(child, depth + 1, max_depth, new_prefix, child_is_last)


if __name__ == "__main__":
    run_surgery_example()

"""
ARAW - Assume Right Assume Wrong Search

A recursive branching search strategy for exploring possibility space.
"""

from .araw_engine import (
    ARAWEngine,
    Node,
    BranchType,
    NodeStatus,
    create_araw_search,
    load_araw_search,
)

__all__ = [
    "ARAWEngine",
    "Node",
    "BranchType",
    "NodeStatus",
    "create_araw_search",
    "load_araw_search",
]

__version__ = "1.0.0"

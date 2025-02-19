#!/usr/bin/env python

"""
Group SELFIES: A robust fragment-based molecular string representation

Group SELFIES is based on SELFIES, where arbitrary strings can be decoded to molecules with valid valency constraints, but includes tokens that represent entire groups, such as benzene. It is useful as input into generative models or molecular representation in genetic algorithms.
"""

__version__ = "0.0.1"

__all__ = [
    "get_preset_constraints",
    "get_semantic_robust_alphabet",
    "get_semantic_constraints",
    "set_semantic_constraints",
    "len_selfies",
    "split_selfies",
    "get_alphabet_from_selfies",
    "group_encoder",
    "group_decoder",
    "fragment_mols",
    "GroupGrammar",
    "Group",
]

from .group_selfies.bond_constraints import (
    get_preset_constraints,
    get_semantic_constraints,
    get_semantic_robust_alphabet,
    set_semantic_constraints,
)
from .group_selfies.group_decoder import group_decoder
from .group_selfies.group_encoder import group_encoder

from .group_selfies.utils.selfies_utils import (
    get_alphabet_from_selfies,
    len_selfies,
    split_selfies,
)
import group_selfies.group_grammar
import group_selfies.group_mol_graph
from .group_selfies.group_mol_graph import (
    MolecularGraph,
    Group,
)
from .group_selfies.group_grammar import GroupGrammar
from .group_selfies.utils.fragment_utils import (
    fragment_mols,
)

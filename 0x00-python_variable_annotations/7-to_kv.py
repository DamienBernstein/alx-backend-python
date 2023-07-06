#!/usr/bin/env python3
"""Contains a function that converts a Python variable to a KV pair."""
import typing from Union, Tuple


def to_kv(k: str, v: Union[str, float]) -> Tuple[int, float]:
     """Converts a Python variable to a KV pair."""
    return k, v **2

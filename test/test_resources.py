import os
import unittest
import pytest
import requests

import responses
from unittest.mock import mock_open, patch
import sys

sys.path.append("../solutions/")
from resources import complement_string, rna_to_protien


class TestResources(unittest.TestCase):
    def test_complement_string(self):
        s = "ATCG"
        c = "TAGC"
        a = complement_string(s)
        self.assertEqual(c, a)

    def test_rna_to_protien(self):
        rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
        prot = "MAMAPRTEINSTRINGStop"
        prot_1 = rna_to_protien(rna)
        self.assertEqual(prot, prot_1)

import os
import unittest
import pytest
from unittest.mock import mock_open, patch
import sys
import logging
sys.path.append("../solutions/")
from resources import complement_string, rna_to_protien, open_fasta
logging.basicConfig(level=logging.INFO)

class TestResources(unittest.TestCase):

    # Test case 1: open correct fasta
    def test_open_fasta(self):
        fasta_lines = [">Rosalind_1", "ATCCAGCT", ">Rosalind_2", "GGGCAACT"]
        expected_out = ["ATCCAGCT", "GGGCAACT"]
    
        with patch("builtins.open", mock_open(read_data="\n".join(fasta_lines))) as m:
            output = open_fasta(in_file="test_mock.fasta")
            m.assert_called_once_with("test_mock.fasta", "r")
            self.assertEqual(output, expected_out)
           

    # test case 1: expected out
    def test_complement_string(self):
        s = "ATCG"
        c = "TAGC"
        a = complement_string(s)
        self.assertEqual(c, a)

    # test case 2: expected fail
    def test_complement_string(self):
        s = "ATCG"
        c = "ACGT"
        a = complement_string(s)
        self.assertFalse(c == a)

    # def test_rna_to_protien(self):
    #     rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    #     prot = "MAMAPRTEINSTRINGStop"
    #     prot_1 = rna_to_protien(rna)
    #     self.assertEqual(prot, prot_1)

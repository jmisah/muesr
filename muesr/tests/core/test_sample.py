#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import unittest
import numpy as np

from muesr.core.sample import Sample

from muesr.core.sampleErrors import *
from muesr.core.atoms import Atoms
from muesr.core.magmodel import MM, have_sympy
if have_sympy:
    from muesr.core.magmodel import SMM

from muesr.core.spg import Spacegroup

class TestSample(unittest.TestCase):
 
    def setUp(self):
        self._sample = Sample()
        
    def _set_a_cell(self):
        self._sample.cell = Atoms(symbols=['Co'],
                                  scaled_positions=[[0,0,0]],
                                  cell=[[3.,0,0],
                                        [0,3.,0],
                                        [0,0,3.]])
        
    def test_name_property(self):
        
        self.assertEqual(self._sample.name,"No name")
        
        self._sample.name = "test"
        
        self.assertEqual(self._sample.name,"test")
        
        #must be str
        with self.assertRaises(TypeError):
            self._sample.name = 1
            
        self.assertEqual(self._sample.name,"test")
        
        # test unicode
        
        if sys.version_info >= (3,0):
            self._sample.name = u"àèé"
        else:
            with self.assertRaises(TypeError):
                self._sample.name = u"àèé"
        
    
    def test_muons_property(self):
        pass
        
    def test_add_muon_property(self):
        with self.assertRaises(CellError):
            self._sample.add_muon([0,0,0])
            
        self._set_a_cell()
                                        
        
        self._sample.add_muon([0,0,0])
        np.testing.assert_array_equal(self._sample.muons[0], np.zeros(3))
        
        self._sample.add_muon([1,1,1])
        np.testing.assert_array_equal(self._sample.muons[1], np.ones(3))
        
        self._sample.add_muon([1,1,1], cartesian=True)
        np.testing.assert_array_equal(self._sample.muons[2], np.ones(3)/3.)
        
        a = 4.0  # Gold lattice constant
        b = a / 2
        self._sample.cell = Atoms(symbols=['Au'],
                                  positions=[0,0,0],
                                  cell=[(0, b, b), (b, 0, b), (b, b, 0)],
                                  pbc=True)
        
        self._sample.add_muon([1.,1.,1.], cartesian=True)
        np.testing.assert_array_equal(self._sample.muons[3], np.ones(3)/4.)
        
        self._sample.add_muon([.5,.5,.5], cartesian=False)
        self._sample.add_muon([2.,2.,2.], cartesian=True)
        np.testing.assert_array_equal(self._sample.muons[4], self._sample.muons[5])
        
        
    
    def test_mm_property(self):
        self._sample._reset(magdefs=True)
        with self.assertRaises(MagDefError):
            self._sample.mm

        with self.assertRaises(CellError):
            self._sample.mm = MM(19) # randomly large number
                    
        
        self._sample._reset(magdefs=True)
        self._set_a_cell()
        with self.assertRaises(TypeError):
            self._sample.mm = 1
            
        self._sample._reset(magdefs=True, cell=True)
        self._sample.cell = Atoms(symbols=['C'],
                                  scaled_positions=[[0,0,0]],
                                  cell=[[3.,0,0],
                                        [0,3.,0],
                                        [0,0,3.]])
                                        
        with self.assertRaises(MagDefError):
            self._sample.mm = MM(198) # randomly large number        
            
        self._sample.mm = MM(1)
        

    def test_new_mm(self):
        self._sample._reset(magdefs=True, cell=True)
        with self.assertRaises(CellError):
            self._sample.new_mm()
        
        self._set_a_cell()
                                        
        self._sample.new_mm()            
        self.assertTrue(isinstance(self._sample.mm, MM))
        self.assertEqual(len(self._sample.mm.fc), 1)
        
        
    
    def test_new_smm(self):
        if have_sympy:
            self._sample._reset(magdefs=True, cell=True)
            with self.assertRaises(CellError):
                self._sample.new_smm("x,y,z")
            
            # TODO TESTING
        else:
            pass
            
    def test_current_mm_idx_property(self):
        self._sample._reset(magdefs=True, cell=True)
        self._sample.cell = Atoms(symbols=['C'],
                                  scaled_positions=[[0,0,0]],
                                  cell=[[3.,0,0],
                                        [0,3.,0],
                                        [0,0,3.]])        
        
        self._sample.new_mm()
        self._sample.mm.k=np.array([0,0,1.])
        self.assertEqual(self._sample.current_mm_idx,0)
        self._sample.new_mm()
        self._sample.mm.k=np.array([0,0,2.])
        self.assertEqual(self._sample.current_mm_idx,1)
        self._sample.new_mm()
        self._sample.mm.k=np.array([0,0,3.])
        self.assertEqual(self._sample.current_mm_idx,2)
        
        self._sample.current_mm_idx = 0
        self.assertEqual(self._sample.current_mm_idx,0)
        np.testing.assert_array_equal(self._sample.mm.k, np.array([0,0,1.]))


        
    def test_sym_property(self):
        with self.assertRaises(SymmetryError):
            self._sample.sym
            
        with self.assertRaises(TypeError):
            self._sample.sym = 1
            
        with self.assertRaises(TypeError):
            self._sample.sym = 1
            
        self._sample.sym = Spacegroup(113)

    def test_cell_property(self): 
        #needs better testing
        with self.assertRaises(CellError):
            self._sample.cell
            
        with self.assertRaises(TypeError):
            self._sample.cell = 1
            
        self._set_a_cell()
        
        
        

    def test_reset(self):
        
        # test cell reset
        self._sample._reset(cell=True)
        self.assertEqual(self._sample._cell, None)
        with self.assertRaises(CellError):
            self._sample.cell
        
        # test magdef reset    
        self._sample._reset(magdefs=True)
        self.assertEqual(self._sample._magdefs, [])
        self.assertEqual(self._sample._selected_mm, -1)
        with self.assertRaises(MagDefError):
            self._sample.mm
            
        # test muon reset
        self._set_a_cell()
        self._sample.add_muon([0,1.,2])
        self._sample._reset(muon=True)
        self.assertEqual(self._sample._muon, [])
        with self.assertRaises(MuonError):
            self._sample.muons
        
        self._sample._reset(cell=True)
            
        #test symmetry reset
        self._sample.sym = Spacegroup(113)
        self._sample._reset(sym=True)
        self.assertEqual(self._sample._sym, None)
        with self.assertRaises(SymmetryError):
            self._sample.sym
            
                       

    # TODO
    def test_check_sym(self):
        pass
        
    def test_check_lattice(self):
        pass
        
    def test_check_magdefs(self):
        pass
        
    def test_check_muon(self):
        pass

# copyright ############################### #
# This file is part of the Xpart Package.   #
# Copyright (c) CERN, 2021.                 #
# ######################################### #

import xpart as xp
from xpart.pdg import *
from xpart.pdg import _PDG, _elements, _elements_long, _pdg_id_ion, _mass_consistent
from xtrack.line import _dicts_equal

def test_names():
    names = [val[1] for val in _PDG.values()]
    names += [f"{val}174" for val in _elements.values()]
    names += [f"{val} 134" for val in _elements_long.values()]
    for name in [val[1] for val in _PDG.values()]:
        pdg_id = get_pdg_id_from_name(name)
        assert get_name_from_pdg_id(pdg_id) == name
        assert get_pdg_id_from_name(get_name_from_pdg_id(pdg_id)) == pdg_id

def test_lead_208():
    pdg_id = 1000822080
    assert _pdg_id_ion(208, 82) == pdg_id
    assert get_pdg_id_from_mass_charge(xp.Pb208_MASS_EV, 82) == pdg_id
    assert get_name_from_pdg_id(pdg_id) == 'Pb208'
    assert get_pdg_id_from_name('Pb208')    == pdg_id
    assert get_pdg_id_from_name('Pb 208')   == pdg_id
    assert get_pdg_id_from_name('Pb-208')   == pdg_id
    assert get_pdg_id_from_name('Pb_208')   == pdg_id
    assert get_pdg_id_from_name('Pb.208')   == pdg_id
    assert get_pdg_id_from_name('pb208')    == pdg_id
    assert get_pdg_id_from_name('lead208')  == pdg_id
    assert get_pdg_id_from_name('Lead 208') == pdg_id
    assert get_pdg_id_from_name('Lead_208') == pdg_id
    assert _mass_consistent(pdg_id, xp.Pb208_MASS_EV)
    assert get_element_name_from_Z(82) == 'Pb'
    assert get_element_full_name_from_Z(82) == 'Lead'
    assert np.allclose(get_mass_from_pdg_id(pdg_id), xp.Pb208_MASS_EV)
    assert get_properties_from_pdg_id(pdg_id) == (82., 208, 82, 'Pb208')

def test_build_reference_from_pdg_id():
    particle_ref_proton  = xp.reference_from_pdg_id(pdg_id='proton')
    assert particle_ref_proton.pdg_id == 2212
    proton_dict = particle_ref_proton.to_dict()
    proton_dict.pop('pdg_id')
    particle_ref_lead = xp.reference_from_pdg_id(pdg_id='Pb208')
    assert np.allclose(particle_ref_lead.q0, 82.)
    assert np.allclose(particle_ref_lead.mass0, xp.Pb208_MASS_EV)

"""Travis CI memory can't handle all the CBCTs; thus only test them when explicitly asked to."""
import os.path as osp
from unittest import TestCase, skip

from tests import TEST_BANK_DIR
from tests.test_cbct import CBCTMixin, CatPhan503, CatPhan504, CatPhan600


class CatPhan504Mixin(CBCTMixin):
    catphan = CatPhan504
    dir_location = osp.join(TEST_BANK_DIR, 'CBCTs', 'CatPhan 504')


class CatPhan503Mixin(CBCTMixin):
    catphan = CatPhan503
    dir_location = osp.join(TEST_BANK_DIR, 'CBCTs', 'CatPhan 503')


class CatPhan600Mixin(CBCTMixin):
    catphan = CatPhan600
    dir_location = osp.join(TEST_BANK_DIR, 'CBCTs', 'CatPhan 600')


class VarianPelvis(CatPhan504Mixin, TestCase):
    """Test the Varian Pelvis protocol CBCT."""
    file_path = ['Pelvis.zip']
    expected_roll = -0.26
    origin_slice = 32
    hu_values = {'Poly': -36, 'Acrylic': 114, 'Delrin': 345, 'Air': -998, 'Teflon': 992, 'PMP': -188, 'LDPE': -95}
    unif_values = {'Center': 17, 'Left': 5, 'Right': 4, 'Top': 4, 'Bottom': 4}
    mtf_values = {30: 0.83, 50: 0.68, 80: 0.48}
    avg_line_length = 49.8
    lowcon_visible = 3


class VarianPelvisSpotlight(CatPhan504Mixin, TestCase):
    """Test the Varian Pelvis Spotlight protocol CBCT."""
    file_path = ['Pelvis spotlight.zip']
    expected_roll = -0.26
    origin_slice = 32
    hu_values = {'Poly': -43, 'Acrylic': 118, 'Delrin': 341, 'Air': -998, 'Teflon': 967, 'PMP': -198, 'LDPE': -100}
    unif_values = {'Center': 19, 'Left': 3, 'Right': -1, 'Top': -1, 'Bottom': 0}
    mtf_values = {30: 1.19, 50: 0.95, 80: 0.63}
    avg_line_length = 49.94
    lowcon_visible = 5


class VarianLowDoseThorax(CatPhan504Mixin, TestCase):
    """Test the Varian Low-Dose Thorax protocol CBCT."""
    file_path = ['Low dose thorax.zip']
    expected_roll = -0.29
    origin_slice = 32
    hu_values = {'Poly': -42, 'Acrylic': 119, 'Delrin': 341, 'Air': -998, 'Teflon': 992, 'PMP': -191, 'LDPE': -94}
    unif_values = {'Center': 16, 'Left': 7, 'Right': -1, 'Top': 3, 'Bottom': 2}
    mtf_values = {30: 0.74, 50: 0.61, 80: 0.42}
    avg_line_length = 49.7
    lowcon_visible = 2


class VarianStandardHead(CatPhan504Mixin, TestCase):
    """Test the Varian Standard Head protocol CBCT."""
    file_path = ['Standard head.zip']
    expected_roll = -0.19
    origin_slice = 32
    hu_values = {'Poly': -40, 'Acrylic': 127, 'Delrin': 350, 'Air': -997, 'Teflon': 997, 'PMP': -191, 'LDPE': -101}
    unif_values = {'Center': 17, 'Left': 15, 'Right': 4, 'Top': 9, 'Bottom': 9}
    mtf_values = {30: 1.08, 50: 0.86, 80: 0.33}
    avg_line_length = 49.94
    lowcon_visible = 1


class VarianLowDoseHead(CatPhan504Mixin, TestCase):
    """Test the Varian Low-Dose Head protocol CBCT."""
    file_path = ['Low dose head.zip']
    expected_roll = -0.4
    origin_slice = 32
    hu_values = {'Poly': -41, 'Acrylic': 121, 'Delrin': 350, 'Air': -997, 'Teflon': 1003, 'PMP': -197, 'LDPE': -103}
    unif_values = {'Center': 13, 'Left': 11, 'Right': 3, 'Top': 7, 'Bottom': 6}
    mtf_values = {30: 1.06, 50: 0.85, 80: 0.54}
    lowcon_visible = 1
    avg_line_length = 49.93


@skip  # SR slice fails; TODO: make slices modular, so if 1 fails, the others still run
class GEMonthlyCT(CatPhan504Mixin, TestCase):
    """Test a monthly CT scan from GE."""
    file_path = ['GE_CT.zip']
    hu_tolerance = 90
    origin_slice = 143
    hu_values = {'Poly': -32, 'Acrylic': 119, 'Delrin': 333, 'Air': -944, 'Teflon': 909, 'PMP': -173, 'LDPE': -87}
    unif_values = {'Center': 11, 'Left': 11, 'Right': 11, 'Top': 11, 'Bottom': 11}
    mtf_values = {60: 0.51, 70: 0.45, 80: 0.39, 90: 0.30, 95: 0.25}
    lowcon_visible = 4


class ToshibaMonthlyCT(CatPhan504Mixin, TestCase):
    """Test a monthly CT scan from Toshiba."""
    file_path = ['Toshiba.zip']
    origin_slice = 36
    hu_values = {'Poly': -32, 'Acrylic': 106, 'Delrin': 467, 'Air': -992, 'Teflon': 1207, 'PMP': -165, 'LDPE': -85}
    unif_values = {'Center': 8, 'Left': 7, 'Right': 7, 'Top': 7, 'Bottom': 6}
    mtf_values = {30: 0.74, 50: 0.56, 80: 0.33}
    lowcon_visible = 4


class CBCT1(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_1.zip']
    expected_roll = -0.53
    origin_slice = 32
    hu_values = {'Poly': -35, 'Acrylic': 130, 'Delrin': 347, 'Air': -996, 'Teflon': 1004, 'PMP': -186, 'LDPE': -94}
    unif_values = {'Center': 13, 'Left': 17, 'Right': 5, 'Top': 10, 'Bottom': 9}
    mtf_values = {30: 1.3, 50: 0.96, 80: 0.64}
    avg_line_length = 49.9
    lowcon_visible = 1


class CBCT2(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_2.zip']
    expected_roll = -0.3
    origin_slice = 34
    hu_values = {'Poly': -16, 'Acrylic': 135, 'Delrin': 367, 'Air': -965, 'Teflon': 1017, 'PMP': -163, 'LDPE': -71}
    unif_values = {'Center': 47, 'Left': 35, 'Right': 37, 'Top': 36, 'Bottom': 37}
    mtf_values = {30: 0.82, 50: 0.68, 80: 0.48}
    lowcon_visible = 4
    avg_line_length = 49.9


class CBCT3(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_3.zip']
    expected_roll = -2.66
    origin_slice = 36
    hu_values = {'Poly': -44, 'Acrylic': 113, 'Delrin': 325, 'Air': -982, 'Teflon': 952, 'PMP': -194, 'LDPE': -103}
    unif_values = {'Center': -2, 'Left': -3, 'Right': 6, 'Top': 6, 'Bottom': -2}
    mtf_values = {30: 0.8, 50: 0.66, 80: 0.45}
    avg_line_length = 49.9
    lowcon_visible = 4

# CBCT4 is in the regular test_cbct.py file


class CBCT5(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_5.zip']
    origin_slice = 34
    hu_values = {'Poly': -56, 'Acrylic': 101, 'Delrin': 328, 'Air': -999, 'Teflon': 977, 'PMP': -201, 'LDPE': -110}
    unif_values = {'Center': 19, 'Left': -10, 'Right': -5, 'Top': -7, 'Bottom': -8}
    mtf_values = {30: 0.81, 50: 0.67, 80: 0.47}
    avg_line_length = 49.55
    lowcon_visible = 5


class CBCT6(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_6.zip']
    expected_roll = 0.2
    origin_slice = 38
    hu_values = {'Poly': -44, 'Acrylic': 107, 'Delrin': 327, 'Air': -994, 'Teflon': 972, 'PMP': -192, 'LDPE': -100}
    unif_values = {'Center': -3, 'Left': -3, 'Right': -13, 'Top': -7, 'Bottom': -6}
    mtf_values = {30: 1.32, 50: 0.93, 80: 0.61}
    avg_line_length = 49.94
    lowcon_visible = 5


class CBCT7(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_7.zip']
    expected_roll = 0.5
    origin_slice = 36
    hu_values = {'Poly': -48, 'Acrylic': 108, 'Delrin': 331, 'Air': -999, 'Teflon': 984, 'PMP': -198, 'LDPE': -107}
    unif_values = {'Center': 12, 'Left': -7, 'Right': -7, 'Top': -8, 'Bottom': -7}
    mtf_values = {30: 0.81, 50: 0.67, 80: 0.48}
    avg_line_length = 49.6
    lowcon_visible = 3


# classifier not working for this case
class CBCT8(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_8.zip']
    use_classifier = False
    expected_roll = 0.55
    origin_slice = 40
    hu_values = {'Poly': -37, 'Acrylic': 114, 'Delrin': 334, 'Air': -994, 'Teflon': 982, 'PMP': -186, 'LDPE': -97}
    unif_values = {'Center': -4, 'Left': 2, 'Right': -5, 'Top': 0, 'Bottom': -1}
    mtf_values = {80: 0.39, 50: 0.94, 30: 1.32}
    avg_line_length = 49.95
    lowcon_visible = 5


class CBCT9(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_9.zip']
    expected_roll = 0.4
    origin_slice = 35
    hu_values = {'Poly': -53, 'Acrylic': 107, 'Delrin': 330, 'Air': -999, 'Teflon': 980, 'PMP': -199, 'LDPE': -107}
    unif_values = {'Center': 10, 'Left': -8, 'Right': -7, 'Top': -6, 'Bottom': -5}
    mtf_values = {30: 0.82, 50: 0.68, 80: 0.48}
    avg_line_length = 49.6
    lowcon_visible = 3


class CBCT10(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_10.zip']
    expected_roll = 0.4
    origin_slice = 38
    hu_values = {'Poly': -37, 'Acrylic': 109, 'Delrin': 334, 'Air': -992, 'Teflon': 985, 'PMP': -186, 'LDPE': -93}
    unif_values = {'Center': -1, 'Left': 4, 'Right': -5, 'Top': 0, 'Bottom': -1}
    mtf_values = {30: 1.14, 50: 0.93, 80: 0.63}
    lowcon_visible = 4


class CBCT11(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_11.zip']
    expected_roll = 0.5
    origin_slice = 38
    hu_values = {'Poly': -37, 'Acrylic': 108, 'Delrin': 332, 'Air': -994, 'Teflon': 982, 'PMP': -187, 'LDPE': -95}
    unif_values = {'Center': -3, 'Left': 2, 'Right': -7, 'Top': -2, 'Bottom': -3}
    mtf_values = {30: 1.09, 50: 0.87, 80: 0.6}
    avg_line_length = 49.94
    lowcon_visible = 4


class CBCT12(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_12.zip']
    origin_slice = 36
    hu_values = {'Poly': -55, 'Acrylic': 112, 'Delrin': 329, 'Air': -999, 'Teflon': 982, 'PMP': -201, 'LDPE': -107}
    unif_values = {'Center': 3, 'Left': -5, 'Right': -11, 'Top': -9, 'Bottom': -8}
    mtf_values = {30: 0.71, 50: 0.57, 80: 0.39}
    avg_line_length = 49.59
    lowcon_visible = 2


class CBCT13(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_13.zip']
    expected_roll = 0.2
    origin_slice = 36
    hu_values = {'Poly': -51, 'Acrylic': 106, 'Delrin': 329, 'Air': -999, 'Teflon': 976, 'PMP': -198, 'LDPE': -107}
    unif_values = {'Center': 3, 'Left': -9, 'Right': -9, 'Top': -10, 'Bottom': -8}
    mtf_values = {80: 0.46, 30: 0.59, 50: 0.59}
    avg_line_length = 49.66
    lowcon_visible = 3


class CBCT14(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_14.zip']
    expected_roll = 0.84
    origin_slice = 32
    hu_values = {'Poly': -41, 'Acrylic': 125, 'Delrin': 334, 'Air': -995, 'Teflon': 986, 'PMP': -184, 'LDPE': -89}
    unif_values = {'Center': 18, 'Left': 13, 'Right': 15, 'Top': 14, 'Bottom': 14}
    mtf_values = {80: 0.42, 30: 0.74, 50: 0.61}
    avg_line_length = 49.4
    lowcon_visible = 4


class CBCT15(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset."""
    file_path = ['CBCT_15.zip']
    origin_slice = 61
    hu_values = {'Poly': -32, 'Acrylic': 121, 'Delrin': 353, 'Air': -998, 'Teflon': 945, 'PMP': -186, 'LDPE': -93}
    unif_values = {'Center': -2, 'Left': 6, 'Right': 5, 'Top': 11, 'Bottom': 3}
    mtf_values = {80: 0.5, 30: 0.85, 50: 0.7}
    lowcon_visible = 6


class CBCT16(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_16.zip']
    expected_roll = 0.2
    origin_slice = 32
    hu_values = {'Poly': -37, 'Acrylic': 128, 'Delrin': 342, 'Air': -995, 'Teflon': 1000, 'PMP': -181, 'LDPE': -87}
    unif_values = {'Center': 17, 'Left': 20, 'Right': 18, 'Top': 19, 'Bottom': 19}
    mtf_values = {80: 0.43, 50: 0.62, 30: 0.78}
    avg_line_length = 49.7
    lowcon_visible = 3


class CBCT17(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset"""
    file_path = ['CBCT_17.zip']
    expected_roll = 0.45
    origin_slice = 34
    hu_values = {'Poly': -43, 'Acrylic': 114, 'Delrin': 336, 'Air': -995, 'Teflon': 989, 'PMP': -192, 'LDPE': -101}
    unif_values = {'Center': 11, 'Left': 0, 'Right': -7, 'Top': -6, 'Bottom': -2}
    mtf_values = {30: 0.97, 50: 0.77, 80: 0.55}
    avg_line_length = 49.9
    lowcon_visible = 1


class Catphan504Ring(CatPhan504Mixin, TestCase):
    """A Varian CBCT dataset with ring artifact"""
    file_path = ['ringartifact.zip']
    expected_roll = 0.1
    origin_slice = 32
    hu_values = {'Poly': -52, 'Acrylic': 103, 'Delrin': 321, 'Air': -995, 'Teflon': 950, 'PMP': -201, 'LDPE': -105}
    unif_values = {'Center': -2, 'Left': -4, 'Right': -16, 'Top': -12, 'Bottom': -8}
    mtf_values = {30: 1.08, 50: 0.87, 80: 0.63}
    avg_line_length = 50.1
    lowcon_visible = 3


class Katy1(CatPhan504Mixin, TestCase):
    """CBCT with very high HU values."""
    file_path = ['Katy iX', 'Monday, March 10, 2014 1-05-47 PM (super high HU).zip']
    origin_slice = 44
    hu_values = {'Poly': 584, 'Acrylic': 797, 'Delrin': 1046, 'Air': -404, 'Teflon': 1720, 'PMP': 424, 'LDPE': 522}
    unif_values = {'Center': 612, 'Left': 628, 'Right': 645, 'Top': 642, 'Bottom': 631}
    mtf_values = {80: 0.59, 30: 0.59, 50: 0.59}
    lowcon_visible = 3


class AGElekta1(CatPhan503Mixin, TestCase):
    """An Elekta CBCT dataset"""
    file_path = ['AG Elekta', 'F0-M20-mA25.zip']
    expected_roll = -1.2
    origin_slice = 189
    hu_values = {'Poly': 341, 'Acrylic': 447, 'Delrin': 590, 'Air': -339, 'Teflon': 1039, 'PMP': 241, 'LDPE': 308}
    unif_values = {'Center': 397, 'Left': 355, 'Right': 346, 'Top': 348, 'Bottom': 350}
    mtf_values = {80: 0.27, 30: 0.47, 50: 0.38}
    avg_line_length = 50.2


class AGElekta2(CatPhan503Mixin, TestCase):
    """An Elekta CBCT dataset"""
    file_path = ['AG Elekta', 'F1-S10-mA10.zip']
    expected_roll = -0.44
    origin_slice = 189
    hu_values = {'Poly': 746, 'Acrylic': 834, 'Delrin': 969, 'Air': 181, 'Teflon': 1324, 'PMP': 670, 'LDPE': 722}
    unif_values = {'Center': 707, 'Left': 758, 'Right': 748, 'Top': 758, 'Bottom': 750}
    mtf_values = {80: 0.29, 50: 0.43, 30: 0.53}
    avg_line_length = 50.2


class Elekta4(CatPhan503Mixin, TestCase):
    """An Elekta CBCT dataset"""
    file_path = ['Elekta_4.zip']
    origin_slice = 129
    hu_values = {'Poly': -319, 'Acrylic': -224, 'Delrin': -91, 'Air': -863, 'Teflon': 255, 'PMP': -401, 'LDPE': -352}
    unif_values = {'Center': -273, 'Left': -267, 'Right': -266, 'Top': -267, 'Bottom': -267}
    mtf_values = {80: 0.49, 50: 0.71, 30: 0.9}


class Elekta7(CatPhan503Mixin, TestCase):
    """An Elekta CBCT dataset"""
    file_path = ['Elekta_7.zip']
    origin_slice = 159
    hu_values = {'Poly': -128, 'Acrylic': -16, 'Delrin': 141, 'Air': -782, 'Teflon': 541, 'PMP': -226, 'LDPE': -164}
    unif_values = {'Center': -81, 'Left': -73, 'Right': -72, 'Top': -73, 'Bottom': -73}
    mtf_values = {80: 0.61, 50: 0.81, 30: 0.92}


class Elekta8(CatPhan503Mixin, TestCase):
    """An Elekta CBCT dataset"""
    file_path = ['Elekta_8.zip']
    origin_slice = 161
    hu_values = {'Poly': -324, 'Acrylic': -229, 'Delrin': -97, 'Air': -868, 'Teflon': 245, 'PMP': -406, 'LDPE': -356}
    unif_values = {'Center': -293, 'Left': -286, 'Right': -285, 'Top': -286, 'Bottom': -286}
    mtf_values = {80: 0.43, 50: 0.69, 30: 0.88}


class UNC100kV(CatPhan503Mixin, TestCase):
    file_path = ['UNC-Chapel Hill', '100kV_CBCT_Feb2016.zip']
    origin_slice = 131
    hu_values = {'Poly': -112, 'Acrylic': 35, 'Delrin': 245, 'Air': -973, 'Teflon': 848, 'PMP': -239, 'LDPE': -168}
    unif_values = {'Center': -45, 'Left': -72, 'Right': -73, 'Top': -71, 'Bottom': -61}
    mtf_values = {80: 0.85, 50: 1.05, 30: 1.22}


class UNC120kV(CatPhan503Mixin, TestCase):
    file_path = ['UNC-Chapel Hill', '120kV_CBCT_Feb2016.zip']
    origin_slice = 131
    hu_values = {'Poly': -274, 'Acrylic': -150, 'Delrin': 22, 'Air': -996, 'Teflon': 486, 'PMP': -380, 'LDPE': -315}
    unif_values = {'Center': -223, 'Left': -236, 'Right': -238, 'Top': -239, 'Bottom': -232}
    mtf_values = {80: 0.64, 50: 0.96, 30: 1.25}


class CatPhan600_1(CatPhan600Mixin, TestCase):
    file_path = ['zzCAT201601.zip']
    expected_roll = -0.66
    origin_slice = 160
    hu_values = {'Poly': -31, 'Acrylic': 124, 'Delrin': 344, 'Air': -958, 'Teflon': 921, 'PMP': -173, 'LDPE': -87}
    unif_values = {'Center': 14, 'Left': 14, 'Right': 13, 'Top': 14, 'Bottom': 12}
    mtf_values = {30: 0.55, 50: 0.45, 80: 0.3}
    avg_line_length = 50.1


class TOHPhilips2mm(CatPhan504Mixin, TestCase):
    file_path = ['H TOH - Philips120kV2mm.zip']
    expected_roll = -0.2
    origin_slice = 61
    hu_values = {'Poly': -30, 'Acrylic': 130, 'Delrin': 292, 'Air': -1000, 'Teflon': 874, 'PMP': -178, 'LDPE': -87}
    unif_values = {'Center': 22, 'Left': 20, 'Right': 20, 'Top': 20, 'Bottom': 20}
    mtf_values = {30: 0.87, 50: 0.7, 80: 0.5}
    avg_line_length = 49.9
    lowcon_visible = 6


class DBCatPhan503Roll(CatPhan503Mixin, TestCase):
    file_path = ['DB', 'Catphan503 MFOV_resolution problem.zip']
    expected_roll = -0.12
    origin_slice = 79
    hu_values = {'Poly': -95, 'Acrylic': 12, 'Delrin': 166, 'Air': -740, 'Teflon': 564, 'PMP': -189, 'LDPE': -130}
    unif_values = {'Center': -75, 'Left': -60, 'Right': -57, 'Top': -56, 'Bottom': -56}
    mtf_values = {30: 0.59, 50: 0.51, 80: 0.36}
    avg_line_length = 48.9
    lowcon_visible = 6

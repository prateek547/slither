import unittest
import subprocess, os, sys
  
class TestNamingConvention(unittest.TestCase):
    testDataDir = "./slither_format/tests/test_data/"
    testDataFile1 = "naming_convention_contract.sol"
    testDataFile2 = "naming_convention_modifier.sol"
    testDataFile3 = "naming_convention_structure.sol"
    testDataFile4 = "naming_convention_enum.sol"
    testDataFile5 = "naming_convention_event.sol"
    testFilePath1 = testDataDir+testDataFile1
    testFilePath2 = testDataDir+testDataFile2
    testFilePath3 = testDataDir+testDataFile3
    testFilePath4 = testDataDir+testDataFile4
    testFilePath5 = testDataDir+testDataFile5
    
    def setUp(self):
        outFD1 = open(self.testFilePath1+".out","w")
        errFD1 = open(self.testFilePath1+".err","w")
        p1 = subprocess.Popen(['python3', '-m', 'slither_format','--verbose','--detect','naming-convention',self.testFilePath1], stdout=outFD1,stderr=errFD1)
        p1.wait()
        outFD1.close()
        errFD1.close()

        outFD2 = open(self.testFilePath2+".out","w")
        errFD2 = open(self.testFilePath2+".err","w")
        p2 = subprocess.Popen(['python3', '-m', 'slither_format','--verbose','--detect','naming-convention',self.testFilePath2], stdout=outFD2,stderr=errFD2)
        p2.wait()
        outFD2.close()
        errFD2.close()

        outFD3 = open(self.testFilePath3+".out","w")
        errFD3 = open(self.testFilePath3+".err","w")
        p3 = subprocess.Popen(['python3', '-m', 'slither_format','--verbose','--detect','naming-convention',self.testFilePath3], stdout=outFD3,stderr=errFD3)
        p3.wait()
        outFD3.close()
        errFD3.close()

        outFD4 = open(self.testFilePath4+".out","w")
        errFD4 = open(self.testFilePath4+".err","w")
        p4 = subprocess.Popen(['python3', '-m', 'slither_format','--verbose','--detect','naming-convention',self.testFilePath4], stdout=outFD4,stderr=errFD4)
        p4.wait()
        outFD4.close()
        errFD4.close()

        outFD5 = open(self.testFilePath5+".out","w")
        errFD5 = open(self.testFilePath5+".err","w")
        p5 = subprocess.Popen(['python3', '-m', 'slither_format','--verbose','--detect','naming-convention',self.testFilePath5], stdout=outFD5,stderr=errFD5)
        p5.wait()
        outFD5.close()
        errFD5.close()

    def tearDown(self):
        p1 = subprocess.Popen(['rm','-f',self.testFilePath1+'.out',self.testFilePath1+'.err',self.testFilePath1+'.format'])
        p1.wait()
        p2 = subprocess.Popen(['rm','-f',self.testFilePath2+'.out',self.testFilePath2+'.err',self.testFilePath2+'.format'])
        p2.wait()
        p3 = subprocess.Popen(['rm','-f',self.testFilePath3+'.out',self.testFilePath3+'.err',self.testFilePath3+'.format'])
        p3.wait()
        p4 = subprocess.Popen(['rm','-f',self.testFilePath4+'.out',self.testFilePath4+'.err',self.testFilePath4+'.format'])
        p4.wait()
        p5 = subprocess.Popen(['rm','-f',self.testFilePath5+'.out',self.testFilePath5+'.err',self.testFilePath5+'.format'])
        p5.wait()
        
    def test_naming_convention_contract(self):
        outFD1 = open(self.testFilePath1+".out","r")
        outFD1_lines = outFD1.readlines()
        outFD1.close()
        for i in range(len(outFD1_lines)):
            outFD1_lines[i] = outFD1_lines[i].strip()
        self.assertTrue(os.path.isfile(self.testFilePath1+".format"),"Patched .format file is not created?!")
        self.assertEqual(outFD1_lines[0],"Number of Slither results: 2")
        self.assertEqual(outFD1_lines[1],"Number of patches: 9")
        self.assertEqual(outFD1_lines.count("Detector: naming-convention (contract definition)"), 2)
        self.assertEqual(outFD1_lines.count("Detector: naming-convention (contract state variable)"), 2)
        self.assertEqual(outFD1_lines.count("Detector: naming-convention (contract function variable)"), 5)
        self.assertEqual(outFD1_lines.count("Old string: contract one"), 1)
        self.assertEqual(outFD1_lines.count("New string: contract One"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 53"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 65"), 1)
        self.assertEqual(outFD1_lines.count("Old string: three k"), 1)
        self.assertEqual(outFD1_lines.count("New string: Three k"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 117"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 124"), 1)
        self.assertEqual(outFD1_lines.count("Old string: three l"), 1)
        self.assertEqual(outFD1_lines.count("New string: Three l"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 206"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 213"), 1)
        self.assertEqual(outFD1_lines.count("Old string: one m"), 1)
        self.assertEqual(outFD1_lines.count("New string: One m"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 343"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 348"), 1)
        self.assertEqual(outFD1_lines.count("Old string: one n"), 1)
        self.assertEqual(outFD1_lines.count("New string: One n"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 423"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 428"), 1)
        self.assertEqual(outFD1_lines.count("Old string: contract three"), 1)
        self.assertEqual(outFD1_lines.count("New string: contract Three"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 498"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 512"), 1)
        self.assertEqual(outFD1_lines.count("Old string: one"), 1)
        self.assertEqual(outFD1_lines.count("New string: One"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 646"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 649"), 1)
        self.assertEqual(outFD1_lines.count("Old string: one r = new one()"), 1)
        self.assertEqual(outFD1_lines.count("New string: One r = new one()"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 773"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 790"), 1)
        self.assertEqual(outFD1_lines.count("Old string: one q"), 1)
        self.assertEqual(outFD1_lines.count("New string: One q"), 1)
        self.assertEqual(outFD1_lines.count("Location start: 871"), 1)
        self.assertEqual(outFD1_lines.count("Location end: 876"), 1)
        self.assertEqual(outFD1_lines.count("Detector: naming-convention (contract new object)"), 1, "Contract naming-convention doesn't work for new object creation.")
        self.assertEqual(outFD1_lines.count("Old string: one r = new one()"), 2)
        self.assertEqual(outFD1_lines.count("New string: One r = new one()"), 2)
        self.assertEqual(outFD1_lines.count("Location start: 773"), 2)
        self.assertEqual(outFD1_lines.count("Location end: 790"), 2)

    def test_naming_convention_modifier(self):
        outFD2 = open(self.testFilePath2+".out","r")
        outFD2_lines = outFD2.readlines()
        outFD2.close()
        for i in range(len(outFD2_lines)):
            outFD2_lines[i] = outFD2_lines[i].strip()
        self.assertTrue(os.path.isfile(self.testFilePath2+".format"),"Patched .format file is not created?!")
        self.assertEqual(outFD2_lines[0],"Number of Slither results: 2")
        self.assertEqual(outFD2_lines[1],"Number of patches: 4")
        self.assertEqual(outFD2_lines.count("Detector: naming-convention (modifier definition)"), 2)
        self.assertEqual(outFD2_lines.count("Detector: naming-convention (modifier uses)"), 2)
        self.assertEqual(outFD2_lines.count("Old string: modifier One"), 1)
        self.assertEqual(outFD2_lines.count("New string: modifier one"), 1)
        self.assertEqual(outFD2_lines.count("Location start: 215"), 1)
        self.assertEqual(outFD2_lines.count("Location end: 227"), 1)
        self.assertEqual(outFD2_lines.count("Old string: () One"), 1)
        self.assertEqual(outFD2_lines.count("New string: () one"), 1)
        self.assertEqual(outFD2_lines.count("Location start: 288"), 1)
        self.assertEqual(outFD2_lines.count("Location end: 295"), 1)
        self.assertEqual(outFD2_lines.count("Old string: modifier Two"), 1)
        self.assertEqual(outFD2_lines.count("New string: modifier two"), 1)
        self.assertEqual(outFD2_lines.count("Location start: 423"), 1)
        self.assertEqual(outFD2_lines.count("Location end: 435"), 1)
        self.assertEqual(outFD2_lines.count("Old string: () one Two returns"), 1)
        self.assertEqual(outFD2_lines.count("New string: () one two returns"), 1)
        self.assertEqual(outFD2_lines.count("Location start: 503"), 1)
        self.assertEqual(outFD2_lines.count("Location end: 522"), 1)

    def test_naming_convention_structure(self):
        outFD3 = open(self.testFilePath3+".out","r")
        outFD3_lines = outFD3.readlines()
        outFD3.close()
        for i in range(len(outFD3_lines)):
            outFD3_lines[i] = outFD3_lines[i].strip()
        self.assertTrue(os.path.isfile(self.testFilePath3+".format"),"Patched .format file is not created?!")
        self.assertEqual(outFD3_lines[0],"Number of Slither results: 2")
        self.assertEqual(outFD3_lines[1],"Number of patches: 6")
        self.assertEqual(outFD3_lines.count("Detector: naming-convention (struct definition)"), 2)
        self.assertEqual(outFD3_lines.count("Detector: naming-convention (struct use)"), 4)
        self.assertEqual(outFD3_lines.count("Old string: struct s {    uint i;  }"), 2)
        self.assertEqual(outFD3_lines.count("New string: struct S {    uint i;  }"), 2)
        self.assertEqual(outFD3_lines.count("Location start: 108"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 134"), 1)
        self.assertEqual(outFD3_lines.count("Location start: 434"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 460"), 1)
        self.assertEqual(outFD3_lines.count("Old string: s s1"), 2)
        self.assertEqual(outFD3_lines.count("New string: S s1"), 2)
        self.assertEqual(outFD3_lines.count("Location start: 171"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 175"), 1)
        self.assertEqual(outFD3_lines.count("Location start: 497"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 501"), 1)
        self.assertEqual(outFD3_lines.count("Old string: s sA"), 1)
        self.assertEqual(outFD3_lines.count("New string: S sA"), 1)
        self.assertEqual(outFD3_lines.count("Location start: 570"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 574"), 1)
        self.assertEqual(outFD3_lines.count("Old string: s"), 1)
        self.assertEqual(outFD3_lines.count("New string: S"), 1)
        self.assertEqual(outFD3_lines.count("Location start: 585"), 1)
        self.assertEqual(outFD3_lines.count("Location end: 586"), 1)

    def test_naming_convention_enum(self):
        outFD4 = open(self.testFilePath4+".out","r")
        outFD4_lines = outFD4.readlines()
        outFD4.close()
        for i in range(len(outFD4_lines)):
            outFD4_lines[i] = outFD4_lines[i].strip()
        self.assertTrue(os.path.isfile(self.testFilePath4+".format"),"Patched .format file is not created?!")
        self.assertEqual(outFD4_lines[0],"Number of Slither results: 2")
        self.assertEqual(outFD4_lines[1],"Number of patches: 7")
        self.assertEqual(outFD4_lines.count("Detector: naming-convention (enum definition)"), 2)
        self.assertEqual(outFD4_lines.count("Detector: naming-convention (enum use)"), 5)
        self.assertEqual(outFD4_lines.count("Old string: enum e {ONE, TWO}"), 2)
        self.assertEqual(outFD4_lines.count("New string: enum E {ONE, TWO}"), 2)
        self.assertEqual(outFD4_lines.count("Location start: 73"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 90"), 1)
        self.assertEqual(outFD4_lines.count("Location start: 375"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 392"), 1)
        self.assertEqual(outFD4_lines.count("Old string: e e1"), 2)
        self.assertEqual(outFD4_lines.count("New string: E e1"), 2)
        self.assertEqual(outFD4_lines.count("Location start: 125"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 129"), 1)
        self.assertEqual(outFD4_lines.count("Location start: 427"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 431"), 1)
        self.assertEqual(outFD4_lines.count("Old string: e eA"), 1)
        self.assertEqual(outFD4_lines.count("New string: E eA"), 1)
        self.assertEqual(outFD4_lines.count("Location start: 498"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 502"), 1)
        self.assertEqual(outFD4_lines.count("Old string: e e2 = eA"), 1)
        self.assertEqual(outFD4_lines.count("New string: E e2 = eA"), 1)
        self.assertEqual(outFD4_lines.count("Location start: 522"), 1)
        self.assertEqual(outFD4_lines.count("Location end: 531"), 1)
        self.assertEqual(outFD4_lines.count("Old string: e1 = e.ONE"), 1, "Enum naming-convention doesn't work while accessing enum members.")
        self.assertEqual(outFD4_lines.count("New string: e1 = E.ONE"), 1)

    def test_naming_convention_event(self):
        outFD5 = open(self.testFilePath5+".out","r")
        outFD5_lines = outFD5.readlines()
        outFD5.close()
        for i in range(len(outFD5_lines)):
            outFD5_lines[i] = outFD5_lines[i].strip()
        self.assertTrue(os.path.isfile(self.testFilePath5+".format"),"Patched .format file is not created?!")
        self.assertEqual(outFD5_lines[0],"Number of Slither results: 2")
        self.assertEqual(outFD5_lines[1],"Number of patches: 4")
        self.assertEqual(outFD5_lines.count("Detector: naming-convention (event definition)"), 2)
        self.assertEqual(outFD5_lines.count("Detector: naming-convention (event calls)"), 2)
        self.assertEqual(outFD5_lines.count("Old string: event e(uint);"), 2)
        self.assertEqual(outFD5_lines.count("New string: event E(uint);"), 2)
        self.assertEqual(outFD5_lines.count("Location start: 75"), 1)
        self.assertEqual(outFD5_lines.count("Location end: 89"), 1)
        self.assertEqual(outFD5_lines.count("Location start: 148"), 1)
        self.assertEqual(outFD5_lines.count("Location end: 152"), 1)
        self.assertEqual(outFD5_lines.count("Old string: e(i)"), 2)
        self.assertEqual(outFD5_lines.count("New string: E(i)"), 2)
        self.assertEqual(outFD5_lines.count("Location start: 148"), 1)
        self.assertEqual(outFD5_lines.count("Location end: 152"), 1)
        self.assertEqual(outFD5_lines.count("Location start: 438"), 1)
        self.assertEqual(outFD5_lines.count("Location end: 442"), 1)

if __name__ == '__main__':
    unittest.main()
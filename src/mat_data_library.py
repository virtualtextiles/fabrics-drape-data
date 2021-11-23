# Textile Material Drape Library 
# (C) Prof. Dr. Yordan Kyosev
# TU Dresden  Germany
# Chair of Development and Assembly of Textile Products
# MIT License applies to this file

# for XML
import xml.etree.ElementTree as ET

# for json
import json
import jsonpickle

class tensile:
    def __init__(self, direction):
        self.dir=direction
        # linearised points curve. [0] is the first, [1] is the second and the elongation is at the same time the elongation limit
        self.forces=[]
        self.elongations=[]
        #  Max Force
        self.ForceMax=0
        self.ElAtForceMax=0
        #  Breaking Force respo. max Elongation
        self.ForceBreak=0
        self.ElAtForceBreak=0
        # raw courve points points
        self.forces_raw=["1","2","3"]
        self.elongations_raw=[]
        self.time_raw=[]
        # units
        self.unit_force="N/m"
        self.unit_elongation="%"
        self.unit_time="s"
        
        # test device parameter
        self.ClampLength=200;
        self.Length_unit="mm";
        self.SampleWidth=50;
        self.TestingSpeed=101;
        self.Speed_unit="mm/min";
        self.TestingType="Stripe" # "or Grap"
        
        # continuum Mechanics
        # Lateral Contraction coefficient depending on the elongation. If only one value equal to Poisson
        self.Poisson=[]
        self.ElongationPoisson=[]
        
    def xml(self):
        # angle added for better readability but the angle is used as attribute for easy reading
        tens=ET.Element("dir" + str(self.dir))
        
        tens.set("dir", str(self.dir))
        # linearised points curve. [0] is the first, [1] is the second and the elongation is at the same time the elongation limit
        tens.set("forces",';'.join(self.forces))
        tens.set("elongations",';'.join(self.elongations))
        #  Max Force
        tens.set("ForceMax",str(self.ForceMax))
        tens.set("ElAtForceMax",str(self.ElAtForceMax))
        #  Breaking Force respo. max Elongation
        tens.set("ForceBreak",str(self.ForceBreak))
        tens.set("ElAtForceBreak", str(self.ElAtForceBreak))
        # raw courve points points
        tens.set("forces_raw",';'.join(self.forces_raw))
        tens.set("elongations_raw",';'.join(self.elongations_raw))
        tens.set("time_raw",';'.join(self.time_raw))
        # units
        tens.set("unit_force",str(self.unit_force))
        tens.set("unit_elongation",str(self.unit_elongation))
        tens.set("unit_time",str(self.unit_time))
        
        # test device parameter
        tens.set("ClampLength",str(self.ClampLength))
        tens.set("Length_unit", str(self.Length_unit))
        tens.set("SampleWidth",str(self.SampleWidth))
        tens.set("TestingSpeed",str(self.TestingSpeed))
        tens.set("Speed_unit", str(self.Speed_unit))
        tens.set("TestingType",str(self.TestingSpeed)) #="Stripe" # "or Grap"
        
        # continuum Mechanics
        # Lateral Contraction coefficient depending on the elongation. If only one value equal to Poisson
        tens.set("Poisson",str(self.Poisson))
        tens.set("ElongationPoisson",str(self.ElongationPoisson))
        
        return tens
    
class bending:
    def __init__(self, direction):
        self.dir=direction
        self.type="Cantilever"
        self.stiffness=10
        self.unit=""
        
    def xml(self):
        be = ET.Element("dir" + str(self.dir))
        be.set("dir", str(self.dir))
        be.set("type",self.type)
        be.set("stiffness",str(self.stiffness))
        be.set("unit",self.unit)
        return be

class thickness:
    def __init__(self):
        self.thickness=0
        self.thickness10=1
        self.thicknessCurve=[]
        self.pressureCurve=[]
    def xml(self):
        root = ET.Element("thickness")
        root.set("thickness", str(self.thickness))
        root.set("thickness10", str(self.thickness10))
        root.set("thicknessCurve", ';'.join(self.thicknessCurve))
        root.set("pressureCurve", ';'.join(self.pressureCurve))
        return root
                 
class materialdata:
    def __init__(self):
        
        self.type="woven"
        self.name="abc"

        # weight
        self.gsm=100
        self.gsm_unit="g/m2"

        #thickness data
        self.thickness=thickness()
        
        # values for bending
        self.bend0=bending(0)
        self.bend45=bending(45)
        self.bend90=bending(90)
        # if more values for anisotropy investigations
        #self.bending=[]
        
        # tensile
        self.tens0=tensile(0)
        self.tens45=tensile(45)
        self.tens90=tensile(90)
        
        #shear
        self.shear=[]
        
        #extracted
        self.vidya=""
        self.clo3d=""
        self.lectra=""
        self.vstitcher=""
        
    def saveXML(self, filename):
        root=ET.Element("Drape-Parameters-XML")
        root.set("encoding","UTF-8")
        root.set("DI_version","1.0")
        
        root.set("type", self.type)
        root.set("name", self.name)

        
        # thickness data
        root.append(self.thickness.xml())
        
        # weight
        w = ET.SubElement(root, "weight")
        w.set("value", str(self.gsm))
        w.set("unit", self.gsm_unit)

        # values for bending
        be=ET.SubElement(root,"bending")
        be.append(self.bend0.xml())
        be.append(self.bend45.xml())
        be.append(self.bend90.xml())
        # if more values for anisotropy investigations
        
        
        # tensile
        t=ET.SubElement(root,"tension")
        t.append(self.tens0.xml())
        t.append(self.tens45.xml())
        t.append(self.tens90.xml())
        self.tens=[]
        
        #shear
        self.shear=[]
        
        #extracted
        self.assyst=0
        self.clo3d=0
        self.lectr=0
        self.vstich=0
        
        tree=ET.ElementTree(root)
        ## from Pyton3.9  ET.indent(tree, space="\t", level=0)
        tree.write(filename, encoding="UTF-8", xml_declaration=True, default_namespace=None, method="xml")
        
        
    def toJSON(self,filename):
        # https://pynative.com/make-python-class-json-serializable/
        empJSON = jsonpickle.encode(self, unpicklable=False, indent=5)
        #print(empJSON)
        with open(filename, "w") as write_file:
            write_file.write(empJSON)
            
m=materialdata()
x=m.tens0.xml()
t=m.saveXML('text.xml')
m.toJSON("test.json")
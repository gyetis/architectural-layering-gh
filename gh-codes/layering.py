__author__="GizemYetis, OzanYetkin, KongpyungMoon & Ozkan Kilic"
__mail__="yetis.gizem@metu.edu.tr, ozan.yetkin@metu.edu.tr, kpmoon@gmail.com & okilic@ybu.edu.tr"
__institution__="Middle East Technical University, Yildirim Beyazit University"

import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
import System.Drawing.Color as sdc

if active:
    #create layer
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    for i,j in zip(layer,color):
        rs.AddLayer(name=i, color=sdc.FromName(j), visible=True)
    
    #create object
    sc.doc = ghdoc
    attributes=[]
    geometry=[]
    for i in elements:
        doc_obj=rs.coercerhinoobject(i)
        attributes.append(doc_obj.Attributes)
        geometry.append(doc_obj.Geometry)
    
    #match layers
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    layertable = sc.doc.Layers
    for l,a,g in zip(layer, attributes, geometry):
        layerindex = layertable.Find(l,True)
        a.LayerIndex = layerindex
        #bake objects
        rhino_obj = sc.doc.Objects.Add(g,a)
    sc.doc = ghdoc

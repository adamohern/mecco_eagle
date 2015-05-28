#python

args = lx.args()

def scaleSet(setName,scales):
	lx.eval("select.typeFrom polygon true")
	lx.eval("select.useSet %s select" %setName)
	lx.eval("tool.set actr.auto on 0")
	lx.eval("tool.set TransformScale on")
	lx.eval("tool.setAttr xfrm.transform SX %s" % scales)
	lx.eval("tool.setAttr xfrm.transform SY %s" % scales)
	lx.eval("tool.setAttr xfrm.transform SZ %s" % scales)
	lx.eval("tool.doApply")
	lx.eval("tool.set TransformScale off")
	lx.eval("tool.clearTask center")
	lx.eval("select.drop polygon")

fullpath = lx.eval("query platformservice alias ? {kit_mecco_eagle:Mesh/eagle_in_a_barrel.lxl}")
lx.out(fullpath)
lx.eval("preset.do {%s}" % fullpath)

scaleSet("bird",args[0])
scaleSet("barrel",args[1])
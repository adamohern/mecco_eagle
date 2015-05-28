#python

import lx
import lxu.command
import traceback

class eagle(lxu.command.BasicCommand):
    
    def __init__(self):
		lxu.command.BasicCommand.__init__(self)
        
		#Command accepts an argument
		self.dyna_Add('Eagle Scale', lx.symbol.sTYPE_FLOAT)
		self.dyna_Add('Barrel Scale', lx.symbol.sTYPE_FLOAT)
		
    def cmd_Flags (self):
	
		#Command is undoable
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO
		
    def cmd_DialogInit (self):
	
        #Set default argument values
        self.attr_SetFlt(0, 1.0)
        self.attr_SetFlt(1, 1.0)
        
    def CMD_EXE(self, msg, flags):
	
		#Get arguments and assign
		eagleScale = self.dyna_Float(0, 1.0)
		barrelScale = self.dyna_Float(1, 1.0)
		
		#Run the script
		lx.eval("@idiot.py %s %s" % (eagleScale,barrelScale))
		
    def basic_Execute(self, msg, flags):
        try:
            self.CMD_EXE(msg, flags)
        except Exception:
            lx.out(traceback.format_exc())
		
    def basic_Enable(self,msg):
        return True
        
lx.bless(eagle, "mecco.idiot")
from .example_dialog import exampleDialog
from .example import *


class Processing:
    def __init__(self):
        self.dlg = exampleDialog()
    def onPbCalculateClicked(self):
        self.var = example()
        value_aa = self.var.run(value_a)
        value_bb = self.var.run.value_b
        product = value_aa * value_bb  
        self.dlg.lblProductAB.setText(f"{product}")

    def onPbPrintHelloWorldClicked(self):
        if self.dlg.cbUseDutch.isChecked():
            print('Walawala Ololo')
        else:
            print('Hello World')

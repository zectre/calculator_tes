from .example_dialog import exampleDialog
from .example import *


class Processing:
    def onPbCalculateClicked(self):

            self.dlg = exampleDialog()
            value_a = self.dlg.spValueA.value()
            value_b = self.dlg.spValueB.value()
            
            product = value_a * value_b
            
            self.dlg.lblProductAB.setText(f"{product}")

    def onPbPrintHelloWorldClicked(self):
            self.dlg = exampleDialog()
            if self.dlg.cbUseDutch.isChecked():
                print('Walawala Ololo')
            else:
                print('Hello World')

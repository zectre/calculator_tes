from .example_dialog import exampleDialog

class Processing:
    def onPbCalculateClicked(self):
            # value_a = self.dlg.spValueA.value()
            # value_b = self.dlg.spValueB.value()
            
            product = value_a * value_b
            
            # self.dlg.lblProductAB.setText(f"{product}")

    def onPbPrintHelloWorldClicked(self):
            if self.dlg.cbUseDutch.isChecked():
                print('Walawala Ololo')
            else:
                print('Hello World')

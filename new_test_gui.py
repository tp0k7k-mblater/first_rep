
# import logging
# import os
# import signal
import sys
# import json

from PyQt6 import uic
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton, QWidget) 

window = None
msg = {}


def getConnectingIpAddress():
    return window.lineEditIpAddress.text()

def getConnectingPort():
    return window.LineEditPort.text()



def onGetMassegeButton():
    global window
    msg = '''
    {
    "cid": "6f6509c0-804a-4f06-ba5c-49368ecd22ae",
    "type": "COMMAND_ANSWER",
    "data": {
        "id": "OWON,XDM3051,24150249,V3.8.0,2",
        "connectionSetting": {
            "ip": "192.168.88.99",
            "port": 3000
        },
        "measurements": {
            "mode": "voltageDc",
            "range": "200V",
            "value": "6.292223E-04"
        }
      }
    }
    '''
    window.plainTextEdit.setPlainText(msg)
  
def onSetConnectionSettingsClicked():
    # ipAddress = getConnectingIpAddress()
    # port = getConnectingPort() 
    msg = """
     {
      "cid": "d5f0441c-5758-11f0-8a40-047c168307c1",
      "type": "COMMAND",
      "data": {
       "connectionSettings": {
         "ip": "%s",
         "port": %d
        }
      }
    }   
    """ % (getConnectingIpAddress(),getConnectingPort())  #(ipAddress,port)

    # mqttWorker.post_message("in/write", msg)

    window.lineEdit.setText(msg)

def onParseConnectionSettingsButton():
    global window
    msg = {}
    msg = window.plainTextEdit.toPlainText()
    data = eval(msg.replace('\n', ''))
    port = data
    # ipAddress = data['data']['connectionSettings']['ip']          
    # port = data['data']['connectionSettings']['port']  
    # types = type(ipAddress) 
    # ipAddress = msg["ip"]          
    # port = msg['port']       
    
    # print(ipAddress,port)
   
    # window.lineEditIpAddress.setText(ipAddress)
    window.LineEditPort.setText(port)
    
    # types = type(ipAddress) 
    # window.lineEditType.setText(types)
    # line_edit.returnPressed.connect(on_line_edit_return_pressed)


def startGui():
    global window
    app = QApplication(sys.argv)

    window = uic.loadUi("new_test_gui.ui")
    # line_edit = QLineEdit('input text')

    window.getMassegeButton.clicked.connect(onGetMassegeButton)
    window.parseConnectionSettingsButton.clicked.connect(onParseConnectionSettingsButton)
  
    # window.readConnectionSettingsButton.clicked.connect(onReadConnectionSettingsButtonClicked)
    window.setConnectionSettings.clicked.connect(onSetConnectionSettingsClicked)
  
    # def onWindowClosedEvent(event):
    #     logging.debug("Window closed")
    #     logging.info("Killing app...")
    #     os.kill(os.getpid(), signal.SIGUSR1)

    # window.closeEvent = onWindowClosedEvent
    window.show()



    app.exec()


if __name__ == "__main__":
    startGui()

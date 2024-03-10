import subprocess
import PySimpleGUI as sg
import time
import subprocess
from time import sleep
from pywinauto import Application
from pywinauto.keyboard import send_keys
from AppOpener import open
import time




class WhatsAppUp():

    


    def __init__(self,number):


        self.number=number
        self.runbandicam=open("Bandicam")
        
        self.stop_flag = True

    def stop_action(self):
        # Set the flag to stop the loop
        self.stop_flag = False

    def run_method_pre(self):
        self._precheck_events()

    def run_method_post(self):
        self._postcheck_events()


    def _precheck_events(self):
        self.start_applications_py()
        sleep(1)
        self.get_phonenumber()
        sleep(1)
        self.click_call_button()
        self.start_recording()
        sleep(1)
        self.lock_screen()

    def _postcheck_events(self):
        self.click_end_button()
        sleep(1)
        self.unlock_screen()
        sleep(1)
        self.stop_recording()
        sleep(1)
        self.lock_screen()


    def start_applications_py(self):
        sleep(3)
        self.startapp = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
        sleep(1)
        self.appwhatsapp = Application(backend='uia').connect(title_re="WhatsApp")

    def get_phonenumber(self):
        sleep(0.25)
        self.url = f"whatsapp://send?phone=+91{self.number}"
        self.subwhatsapp=subprocess.Popen(["cmd", "/C", f"start {self.url}"], shell=True)
        sleep(0.25)
        self.url = f"whatsapp://send?phone=+91{self.number}"
        self.subwhatsapp=subprocess.Popen(["cmd", "/C", f"start {self.url}"], shell=True)
    
    
    
    def start_recording(self):
        self.dialog = self.appwhatsapp.window(title="Video call ‎- WhatsApp")
        self.button = self.dialog.child_window(title="Add members", auto_id="ParticipantSideBarTriggerButton", control_type="Button")
        while self.stop_flag:
            try:
                if self.button.is_enabled():
                    send_keys("{VK_F12}")
                    self.stop_action() 
            except:
                time.sleep(1)
                continue

    def stop_recording(self):
        sleep(1)
        send_keys("{VK_F12}")

    def lock_screen(self):
        sleep(1)
        send_keys("^%{VK_NUMPAD0}")

    def unlock_screen(self):
        sleep(1)
        send_keys("^%{VK_NUMPAD0}")
    
    def click_call_button(self):
        while True:
            try:
                self.appwhatsapp.WhatsAppDialog.child_window(title="Video call", auto_id="VideoCallButton", control_type="Button").click()
                break
            except:
                time.sleep(1)
                continue


    def click_end_button(self):  
        try: 
            self.appwhatsapp.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()   
        except:
            subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

    def check_group_call(self):
        self.dialog = self.appwhatsapp.window(title="Group video call ‎- WhatsApp", control_type="Window")
        self.trigger= self.dialog.child_window(title="Group video call ‎- WhatsApp", auto_id="TitleBar", control_type="Window")
        while True:
           try: 
                if self.trigger.is_enabled():
                    sg.theme('NeutralBlue')
                    sg.popup('Conference Not Allowed',font='stencil 50')
                    break 
           except:
                time.sleep(1)
                continue
 

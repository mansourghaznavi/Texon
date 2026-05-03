import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from Texon_Ui import Ui_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_page()
        self.ui.setupUi(self)

        self.ui.txt_upper.clicked.connect(self.text_uppercase)
        self.ui.txt_lower.clicked.connect(self.text_lower)
        self.ui.txt_copitalize.clicked.connect(self.text_copitalize)
        self.ui.txt_reverse.clicked.connect(self.reverse_text)
        self.ui.count_char.clicked.connect(self.count_char)
        self.ui.del_additional_space.clicked.connect(self.remove_extra_space)
        self.ui.count_words.clicked.connect(self.count_word_function)

   
    
    # convert the charecter to Upper
    def text_uppercase(self):
        
        upper_text=self.ui.txt_input.toPlainText().upper()
        self.ui.txt_input.setPlainText(upper_text)

    # convert the charectar to lower
    def text_lower(self):
        orginal_text=self.ui.txt_input.toPlainText()
        text_lower=orginal_text.lower()
        self.ui.txt_input.setPlainText(text_lower)   
        

    
    
   # Capitalize each word
    def text_copitalize(self):
        my_list=[]

        my_list=self.ui.txt_input.toPlainText().split()
        list_cap=(word.capitalize() for word in my_list)
        final_list=" ".join(list_cap)
        self.ui.txt_input.setPlainText(final_list)


        # Reverse each word
    def reverse_text(self):
        my_lsit=[]
        my_lsit=self.ui.txt_input.toPlainText().split()
        t_reverse=(word[::-1] for word in my_lsit)
        final_list=" ".join(t_reverse)
        self.ui.txt_input.setPlainText(final_list)
 

      # Count  Charectar
    def count_char(self):
        orgianl_text=self.ui.txt_input.toPlainText()
        no_sapce_text=orgianl_text.replace(" ","")
        
        count_charectar=len(no_sapce_text)
        count_charectar_str=str(count_charectar)
        self.ui.lab_char.setText(f"{count_charectar_str} \n Charecters")  


     # Count The Charectar
    def remove_extra_space(self):
        orginal_text=self.ui.txt_input.toPlainText()
        clean_text=" ".join(orginal_text.split())
        self.ui.txt_input.setPlainText(clean_text)



      # Count  word
    def count_word_function(self):
        my_list=[]
        my_list=self.ui.txt_input.toPlainText().split()
        len_list=len(my_list)
        len_list_str=str(len_list)
        self.ui.lab_words.setText(f"{len_list_str} \n Words")          

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()        

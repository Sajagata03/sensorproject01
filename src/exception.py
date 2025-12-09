import sys



def error_message_detail(error, error_details: sys):
    print(error)
    print(error_details)
    print(error_details.exc_info())
    _,_,exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred pythonscript name {0} line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno , str(error)
    )

    return error_message



class Customexception(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message,error_details = error_details
        )

    def __str__(self):
        return self.error_message
    
#Once raise is executed → program terminates → no print("hello") will run after that.
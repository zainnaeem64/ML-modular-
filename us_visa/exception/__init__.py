
def error_message_detail(error_message: str, error_detail: str = None) -> str:
    """Constructs a detailed error message."""
    
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} with message: {error_message}"

    return error_message


class USVisaexception(Exception):

    def __init__(self,error_message,error_detail):


        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message




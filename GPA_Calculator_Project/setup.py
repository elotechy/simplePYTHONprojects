from cx_Freeze import setup, Executable 
  
setup(name = "GPA Calculator" , 
      version = "1.0" , 
      description = "An App to Calculate GPA for a semester" , 
      executables = [Executable("GPA_Calculator_Class.py")]) 
from tkinter import *

class GPA_APP:
    def __init__(self, window):
        self.grade_weights = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
        self.window = window
        self.mainFrame = Frame(window)
        self.mainFrame.pack()

        self.headLabel = Label(self.mainFrame, text = "WELCOME TO THE GPA CALULATOR",fg="black", bg="deep pink", font=('times', 15, ' bold '))
        self.headLabel.grid(row=0, column=0)

        self.Space1 = Label(self.mainFrame, text = "")
        self.Space1.grid(row=1, column=0)

        self.nCourseLabel = Label(self.mainFrame, text = "ENTER NUMBER OF COURSES",fg="black", bg="deep pink", width = 30, height = 2, font=('times', 10, ' bold '))
        self.nCourseLabel.grid(row=2, column=0)

        self.nCourses = Entry(self.mainFrame, width = 15)
        self.nCourses.grid(row=2, column=1)


        self.AddCourseBtn = Button(window, text='Add Courses!',command = self.addCourses, width = 15, height = 2 ) 
        self.AddCourseBtn.pack(padx = 50, pady=10)

        self.courseFrame = Frame(window)
        self.courseFrame.pack()

    def clear_screen(self):
        self.notice.destroy()
    
    def notice_screen(self):
        self.notice = Tk()
        self.notice.title("Error")
        self.notice.configure(background='red')
        self.notice_label = Label(self.notice, text='Hey! , Enter a Valid Value', bg='red', fg ='black', font=('times', 12, ' bold '))
        self.notice_label.pack()
        self.Ok = Button(self.notice, text = "OK", command = self.clear_screen, bg='red',fg='white')
        self.Ok.pack()

    def addCourses(self):
        if (self.nCourses.get() != ""):
            self.numCourses = int(self.nCourses.get())
            print(self.numCourses)
            self.course_list = []
            self.course_grade = []
            self.course_credit = []
            
            self.CourseLabel = Label(self.courseFrame, text="Course :")
            self.CourseLabel.grid(row=0, column=0)

            self.CreditLabel = Label(self.courseFrame, text="Credit :")
            self.CreditLabel.grid(row=0, column=1)

            self.GradeLabel = Label(self.courseFrame, text="Grade :")
            self.GradeLabel.grid(row=0, column=2)

            for i in range(0, self.numCourses):
                self.course_list.append(Entry(self.courseFrame))
                self.course_list[i].grid(row = i+1, column=0, padx=10, pady=10)
                
                self.course_credit.append(Spinbox(self.courseFrame, values=(1,2,3,4,5,20)))
                self.course_credit[i].grid(row = i+1,column=1,padx=10,pady=10)

                self.course_grade.append(Spinbox(self.courseFrame, values=("A", "B", "C", "D", "E", "F","ABS")))
                self.course_grade[i].grid(row = i+1,column=2,padx=10,pady=10)
            
            self.Cal_GPA_btn = Button(self.window, text='Calculate GPA', command= self.CalculateGPA) 
            self.Cal_GPA_btn.pack(pady=8)
            #self.Cal_GPA_btn.config(state = DISABLED)
        
        else:
            self.notice_screen()


            
    def CalculateGPA(self):
        print("Calculating")
        total_credit = 0
        total_weight = 0
        for j in range (0, self.numCourses):
            total_credit += int(self.course_credit[j].get())
            total_weight += int(self.course_credit[j].get())*int(self.grade_weights[self.course_grade[j].get()])
        final_GPA = float(total_weight/total_credit)
        if final_GPA >=4.5:
            status = "First Class"
        elif ((final_GPA >=3.5) and (final_GPA < 4.5)):
            status = "Second Class Upper"
        elif ((final_GPA >=2.5) and (final_GPA < 3.5)):
            status = 'Second Class Lower'
        elif ((final_GPA >=1.0) and (final_GPA < 2.5)):
            status = 'Third Class'
        else:
            status = 'Pass'
        
        def clear_display():
            self.Display.destroy()

        def DisplayGPA():
            self.Display = Tk()
            self.Display.title('Error')
            self.Display.configure(background='green')
            self.DisplayLabel = Label(self.Display, text='Your GPA is {:.2f}'.format(final_GPA), bg='green', fg ='white', font=('times', 15, ' bold ') )
            self.DisplayLabel.pack()
            self.DisplayLabel = Label(self.Display, text='Congratulations!! You made a  {}'.format(status), bg='green', fg ='white', font=('times', 15, ' bold ') )
            self.DisplayLabel.pack()
            self.Ok = Button(self.Display, text = "OK", command = clear_display, bg='red',fg='white')
            self.Ok.pack()
        
        DisplayGPA()

root=Tk()
app = GPA_APP(root)
root.mainloop()
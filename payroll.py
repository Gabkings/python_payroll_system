from tkinter import *
import random 
import time
import datetime

#define the name of application

payroll = Tk()

payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management System")
payroll["bg"] = "grey"

text_Input = StringVar()
#**********************Variable declarations ********************************
Employee_name = StringVar()
Address = StringVar()
Employer = StringVar()
Reference = StringVar()
City_weighting = StringVar()
Basic_salary = StringVar()
Overtime = StringVar()
Gross_pay = StringVar()
Net_pay = StringVar()
Tax = StringVar()
Pension = StringVar()
Student_loan = StringVar()
NI_payment = StringVar()
Deduction = StringVar()
Postal_code = StringVar()
Gender = StringVar()
Pay_date = StringVar()
Tax_period = StringVar()
NI_number = StringVar()
NI_code = StringVar()
Pensionable_pay = StringVar()
Other_payment_due = StringVar()
#********************** End variable declarations ***************************
#**********************Buttons functionality start *************************
#exit button functionality
def Exit():
	payroll.destroy()

#Reset button functionality
def Reset():
	Employee_name .set("")
	Address .set("")
	Employer .set("")
	Reference .set("")
	City_weighting .set("")
	Basic_salary .set("")
	Overtime .set("")
	Gross_pay .set("")
	Net_pay .set("")
	Tax .set("")
	Pension .set("")
	Student_loan .set("")
	NI_payment .set("")
	Deduction .set("")
	Postal_code .set("")
	Gender .set("")
	Pay_date .set("")
	Tax_period .set("")
	NI_number .set("")
	NI_code .set("")
	Pensionable_pay .set("")
	Other_payment_due .set("")
#Wage button functionality
def WagePayment():
	CW = float(City_weighting.get())
	if CW != "":
		CW = float(City_weighting.get())
	else:
		CW = 0
	BS = float(Basic_salary.get())
	if BS != "":
		BS = float(Basic_salary.get())
	else:
		BS = 0
	OT = float(Overtime.get())
	if OT != "":
		OT = float(Overtime.get())
	else:
		OT = 0
	TGP = CW + BS + OT
	Gross_pay.set(str(" %.2f " %(TGP)))
	TX = float(Tax.get())
	if TX != "":
		TX = float(Tax.get())
	else:
		TX = 0
	PS = float(Pension.get())
	if PS != "":
		PS = float(Pension.get())
	else:
		PS = 0
	SL = float(Student_loan.get())
	if SL != "":
		SL = float(Student_loan.get())
	else:
		SL = 0
	NIP = float(NI_payment.get())
	TTD = TX + PS + SL+ NIP
	Deduction .set(str(" %.2f " %(TTD)))
	Net_pay .set(str(" %.2f " %(TGP - TTD)))

#Pay Reference button functionality
def PayReference():
	Pay_date.set(time.strftime("%x"))
	Reference .set("PR"+str(random.randint(20000,74000)))
	NI_number .set("NI"+str(random.randint(20000,74000)))

#Pay Reference button functionality
def PayCode():
	Tax_period .set(datetime.datetime.now().month)
	NI_code .set("xa#"+str(random.randint(2000,7400)))

#**********************Buttons functionality ends *************************
Tops = Frame(payroll,width=1350,height=50, bd=8, relief="raise",bg="#f4f6f9")
Tops.pack(side=TOP)
lf = Frame(payroll,width=700,height=575, bd=8, relief="raise",bg="#f4f6f9")
lf.pack(side=LEFT)
rf = Frame(payroll,width=630,height=575, bd=8,relief="raise",bg="#f4f6f9")
rf.pack(side=RIGHT)
lbInfo = Label(Tops,font=('arial',50,'bold'),text="                  Payroll Management System                  ",fg="Steel Blue",
	bd=4,bg="powder blue")
lbInfo.grid(row=0,column=0)
left_inside_lt = Frame(lf,width=700,height=200, bd=8,relief="raise",bg="#f4f6f9" )
left_inside_lt.pack(side=TOP)
left_iniself_lf = Frame(lf,width=330,height=370, bd=8,relief="raise",bg="#f4f6f9")
left_iniself_lf.pack(side=LEFT)
left_iniself_lr = Frame(lf,width=330,height=370, bd=8,relief="raise",bg="#f4f6f9")
left_iniself_lr.pack(side=RIGHT)
#inside the right frame

right_inside_rt = Frame(rf,width=620,height=200, bd=8,relief="raise",bg="#f4f6f9")
right_inside_rt.pack(side=TOP)
right_iniself_rl = Frame(rf,width=310,height=370, bd=8,relief="raise",bg="#f4f6f9")
right_iniself_rl.pack(side=LEFT)
right_iniself_rf = Frame(rf,width=310,height=370, bd=8,relief="raise",bg="#f4f6f9")
right_iniself_rf.pack(side=RIGHT)

#******************** Left side part ***********************
lbl_employee_name = Label(left_inside_lt,bg="powder blue" ,font=('arial',12,'bold'),text="Employee Name",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_employee_name .grid(row=0,column=0)
text_employee_name = Entry(left_inside_lt ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Employee_name)
text_employee_name.grid(row=0,column=1)

lbl_employee_address = Label(left_inside_lt ,bg="powder blue",font=('arial',12,'bold'),text=" Address",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_employee_address .grid(row=1,column=0)
text_employee_address = Entry(left_inside_lt ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Address)
text_employee_address.grid(row=1,column=1)

lbl_employee_reference = Label(left_inside_lt ,bg="powder blue" ,font=('arial',12,'bold'),text="Reference ",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_employee_reference.grid(row=2,column=0)
text_employee_reference = Entry(left_inside_lt ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Reference)
text_employee_reference.grid(row=2,column=1)

lbl_employer = Label(left_inside_lt,bg="powder blue" ,font=('arial',12,'bold'),text="Employer  ",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_employer .grid(row=3,column=0)
text_employer = Entry(left_inside_lt ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Employer)
text_employer.grid(row=3,column=1)

#********************************left side right frame left side **************
lbl_city_weighting = Label(left_iniself_lf,bg="powder blue" ,font=('arial',12,'bold'),text="City Weighting",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_city_weighting.grid(row=0,column=0)
text_city_weighting = Entry(left_iniself_lf ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=City_weighting)
text_city_weighting.grid(row=0,column=1)

lbl_basic_salary = Label(left_iniself_lf ,bg="powder blue",font=('arial',12,'bold'),text="Basic Salary",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_basic_salary.grid(row=1,column=0)
text_basic_salary = Entry(left_iniself_lf ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Basic_salary)
text_basic_salary.grid(row=1,column=1)

lbl_overtime = Label(left_iniself_lf ,bg="powder blue",font=('arial',12,'bold'),text="Overtime",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_overtime.grid(row=2,column=0)
text_overtime = Entry(left_iniself_lf ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Overtime)
text_overtime.grid(row=2,column=1)

lbl_gross_pay = Label(left_iniself_lf ,bg="powder blue",font=('arial',12,'bold'),text="Gross Pay",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_gross_pay.grid(row=3,column=0)
text_gross_pay = Entry(left_iniself_lf ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Gross_pay)
text_gross_pay.grid(row=3,column=1)

lbl_net_pay = Label(left_iniself_lf,bg="powder blue" ,font=('arial',12,'bold'),text="Net Pay",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_net_pay.grid(row=4,column=0)
text_net_pay = Entry(left_iniself_lf ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Net_pay)
text_net_pay.grid(row=4,column=1)
#********************************left side right frame right side **************
lbl_tax = Label(left_iniself_lr,bg="powder blue" ,font=('arial',12,'bold'),text="Tax",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_tax.grid(row=0,column=0)
text_tax = Entry(left_iniself_lr ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Tax)
text_tax.grid(row=0,column=1)

lbl_pension = Label(left_iniself_lr,bg="powder blue" ,font=('arial',12,'bold'),text="Pension",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_pension.grid(row=1,column=0)
text_pension = Entry(left_iniself_lr,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Pension)
text_pension.grid(row=1,column=1)

lbl_student_loan = Label(left_iniself_lr ,bg="powder blue",font=('arial',12,'bold'),text="Student Loan",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_student_loan.grid(row=2,column=0)
text_student_loan = Entry(left_iniself_lr ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Student_loan)
text_student_loan.grid(row=2,column=1)

lbl_ni_payment = Label(left_iniself_lr ,bg="powder blue",font=('arial',12,'bold'),text="NI Payment",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_ni_payment.grid(row=3,column=0)
text_ni_payment = Entry(left_iniself_lr ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=NI_payment)
text_ni_payment.grid(row=3,column=1)

lbl_deductions = Label(left_iniself_lr ,bg="powder blue",font=('arial',12,'bold'),text="Deductions",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_deductions.grid(row=4,column=0)
text_deductions = Entry(left_iniself_lr ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Deduction)
text_deductions.grid(row=4,column=1)
#******************* Right side part ************************
lbl_postal_code = Label(right_inside_rt ,bg="powder blue",font=('arial',12,'bold'),text="Postal Code",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_postal_code .grid(row=0,column=0)
text_postal_code = Entry(right_inside_rt,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Postal_code)
text_postal_code.grid(row=0,column=1)

lbl_gender = Label(right_inside_rt ,bg="powder blue",font=('arial',12,'bold'),text="Gender ",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_gender .grid(row=1,column=0)
text_gender = Entry(right_inside_rt,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=48,justify="right",bg="powder blue",textvariable=Gender)
text_gender.grid(row=1,column=1)

#************************************************

#********************************right side right frame right side **************
lbl_paydate = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="Pay Date",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_paydate.grid(row=0,column=0)
text_paydate = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Pay_date)
text_paydate.grid(row=0,column=1)

lbl_tax_period = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="Tax Period",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_tax_period.grid(row=1,column=0)
text_tax_period = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Tax_period)
text_tax_period.grid(row=1,column=1)

lbl_ni_number = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="NI Number",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_ni_number.grid(row=2,column=0)
text_ni_number = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=NI_number)
text_ni_number.grid(row=2,column=1)

lbl_ni_code = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="NI Code",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_ni_code.grid(row=3,column=0)
text_ni_code = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=NI_code)
text_ni_code.grid(row=3,column=1)

lbl_taxable_pay = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="Taxable Pay",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_taxable_pay.grid(row=4,column=0)
text_taxable_pay = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Tax_period)
text_taxable_pay.grid(row=4,column=1)

lbl_pensionable_pay = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="Pensionable Pay",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_pensionable_pay.grid(row=4,column=0)
text_pensionable_pay = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Pensionable_pay)
text_pensionable_pay.grid(row=4,column=1)

lbl_otherpayment_due = Label(right_iniself_rl ,bg="powder blue",font=('arial',12,'bold'),text="Other Payment Due",fg="Steel Blue",bd=1, 
	anchor="w")
lbl_otherpayment_due.grid(row=5,column=0)
text_otherpayment_due = Entry(right_iniself_rl ,font=('arial',12,'bold'),
	fg="Steel Blue",bd=4,width=18,justify="right",bg="powder blue",textvariable=Other_payment_due)
text_otherpayment_due.grid(row=5,column=1)

#********************************right side right frame right side **************

btn_pensionable_pay = Button(right_iniself_rf ,pady=8,font=('arial',12,'bold'),
	fg="Steel Blue",bd=8,width=23,text="Wage Payment",bg="powder blue",command=WagePayment).grid(row=0,column=0)

btn_reset_system = Button(right_iniself_rf ,pady=8,font=('arial',12,'bold'),
	fg="Steel Blue",bd=8,width=23,text="Reset System",bg="powder blue",command=Reset).grid(row=1,column=0)

btn_pay_reference = Button(right_iniself_rf ,pady=8,font=('arial',12,'bold'),
	fg="Steel Blue",bd=8,width=23,text="Pay Reference",bg="powder blue",command=PayReference).grid(row=2,column=0)

btn_pay_code = Button(right_iniself_rf ,pady=8,font=('arial',12,'bold'),
	fg="Steel Blue",bd=8,width=23,text="Pay Code",bg="powder blue",command=PayCode).grid(row=3,column=0)

btn_exit = Button(right_iniself_rf ,pady=8,font=('arial',12,'bold'),
	fg="Steel Blue",bd=8,width=23,text="Exit",bg="powder blue",command=Exit).grid(row=4,column=0)
payroll.mainloop()
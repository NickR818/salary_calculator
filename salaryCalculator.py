"""
Chapter 8 challenge
1/25/24
**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
GUI-Based version of the Salary Calculator app which calculates an employee's weekly earnings.
"""
from breezypythongui import EasyFrame
# Other imports go here
import tkinter
from tkinter.font import Font
# Class header(class name will change project to project)
class SalaryCalculator(EasyFrame):
	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator 2.0", resizable = False, background = "lightgreen")
		self.title = self.addLabel(text = "Salary Calculator 2.0", row = 0, column = 0, columnspan = 2, font = Font(weight = "bold", size = 22), sticky = "NSEW", background = "lightgreen", foreground = "darkgreen")
		self.wageLabel = self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "lightgreen", foreground = "forestgreen")
		self.wageInput = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.hoursLabel = self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, background = "lightgreen", foreground = "forestgreen")
		self.hoursInput = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hoursInput.bind("<Return>", lambda event: self.compute())
		self.calculate = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.calculate["background"] = "peachpuff"
		self.salaryLabel = self.addLabel(text = "The employee's salary is:", row = 4, column = 0, columnspan = 2, sticky = "NSEW", background = "lightgreen", foreground = "forestgreen")
	# Definition of the compute(self) function
	def compute(self):
		wage = self.wageInput.getNumber()
		hours = self.hoursInput.getNumber()
		salary = wage * hours
		self.salaryLabel["text"] = "The employee's salary is: $%0.2f" % salary
# Global definition of the main() function
def main():
	# Instantiate an object from the class into mainloop
	SalaryCalculator().mainloop()
# Global call to main() for program entry
if __name__ == "__main__":
	main()
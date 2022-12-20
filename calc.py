import tkinter 
from tkinter import *



root = tkinter.Tk()
root.wm_title("speed entering calculator")





#creating canvas
canvas1 = tkinter.Canvas(root, bg="black")
canvas1.pack()

#making entry box for values
entry1 = tkinter.Entry(root, justify="center")
canvas1.create_window(200,140,height=100,width=100, window=entry1)




 





class method1:

	i=0
	list1=[]

	
	



	#function for enter
	def entering(self, a):

		global i #to inform this function that i is global variable
		

		try:     # try and exception used to print message if error happen

			value1=int (entry1.get()) #entry1.get()is used to get values which entered in entry box
			self.add_value_to_list(value1)
			value1=self.i + value1
			label1['text']=value1
			self.i=value1


		
		except ValueError as ve:
			print(f'only integer')
		
		

		entry1.delete(0, END) # used to clear entry box


    
	#function for add all values to a list
	def add_value_to_list(self, value):
		global list1
		self.list1.append(value)
		self.list_add(self.list1)
		print(self.list1)
		 #used to change value in label2


	#function used to make a string with + sign
	def list_add(self, list):
		string=""
		st="+"
		
		for i in list:
			string=string+str(i)+st
		

		label2['text']=string


	


		


	
	





ob=method1()

li="" #this used to define li otherwise the error will be shown
#label2 for display all values like 5+2+etc...
label2=Label(root, text =li, height=5) 
label2.pack()

#label1 for display answer
value = "the values should be shown here"
label1=Label(root, text =value, height=5) 
label1.pack()




#binding enter key as adding
root.bind('<Return>',ob.entering)






root.mainloop()


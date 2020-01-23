from flask import Flask, render_template

from assign_ import function

app = Flask(__name__)

@app.route('/')
def index():
	data = function()
	
	context = {"context":[ ["Name of customers who ordered once", data[3]], ["Name of customers who ordered twice", data[4]], ["Name of customers who ordered three times", data[5]], ["Name of customers who ordered four times", data[6]], ["Name of customers who ordered more than five times", data[7]]], "context1": [["One time Order",data[2][0]], ["Two time Order",data[2][1]], ["Three time Order",data[2][2]], ["Four time Order",data[2][3]], ["More than five time order",data[2][4]]], "context3": [["Total number of order",data[0]], ["Total amount of order in rupees", data[1]]]}

	
	
	return render_template("graph.html", context = context)

if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask,render_template,jsonify,request
import numpy as np
import pickle 
app= Flask(__name__)

model = pickle.load(open('churn_pickle.pkl','rb'))


@app.route('/')
def churn():
	return render_template('/churn/churn_template.html')

@app.route('/churn_home', methods=["POST"])
def churn_home():
		print('testing')
		geo_filter= ''
		male_filter=''

		print('testing1')

		data1 = request.form['CreditScore']

		if request.form['Geography'] == 'france' : 
			geo_filter=0
		elif request.form['Geography'] == 'spain':
			geo_filter=1
		else:
			geo_filter=2


		if request.form['Gender'] == 'M' : 
			 male_filter=0
		else:
			male_filter=1	
			
		data2 = request.form['Age']
		data3 = request.form['Tenure']
		data4 = request.form['Balance']
		data5 = request.form['NumOfProducts']
		data6 = request.form['HasCrCard']
		data7 = request.form['IsActiveMember']
		data8 = request.form['EstimatedSalary']

		final= np.array([[data1,geo_filter,male_filter,data2,data3,data4,data5,data6,data7,data8]])
		print(final)
		score = model.predict(final)
		print(score)

		#return '''The predicaton of the values are{} :'''.format(score)

		return render_template('/churn/churn_template_new.html',score= score[0])

if __name__=='__main__':
	app.run(debug=True,port=1000)  
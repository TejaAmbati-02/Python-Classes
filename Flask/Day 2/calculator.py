from flask import Flask, request, render_template, jsonify
import math
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method=='POST'):
        ops = request.form["operation"]
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1+num2
            result = "This is the sum of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'subtract'):
            r = num1-num2
            result = "This is the subtract of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'multiply'):
            r = num1*num2
            result = "This is the multiply of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'divide'):
            r = num1/num2
            result = "This is the divide of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'log'):
            r = log10(num1)
            result = "This is the log of "+str(num1)+" and"+str(num2)+" is "+str(r)

        return render_template('results.html', result= result)  



@app.route('/postman_action',methods=['POST'])
def test_ops():
    if(request.method=='POST'):
        ops = request.json["operation"]
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            r = num1+num2
            result = "This is the sum of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'subtract'):
            r = num1-num2
            result = "This is the subtract of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'multiply'):
            r = num1*num2
            result = "This is the multiply of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'divide'):
            r = num1/num2
            result = "This is the divide of "+str(num1)+" and"+str(num2)+" is "+str(r)

        if(ops == 'log'):
            r = log10(num1)
            result = "This is the log of "+str(num1)+" and"+str(num2)+" is "+str(r)

        return jsonify(result)


if __name__ =='__main__':
    app.run(host='0.0.0.0')
    
from flask import Flask,render_template,request,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/answer' ,methods=['POST'])
def answer():
    feet=int(request.form['feet'])
    inches=int(request.form['inches'])
    if(inches>11):
        return render_template('home.html',feet=feet,inches=inches,weight=weight,data="Inches cannot me more than 11")
    weight=int(request.form['weight'])
    meter=(feet*0.3048)+(inches*0.0254)
    ans=weight/(meter*meter)
    if(ans<18.5):
        return render_template('home.html',data=f'Your BMI is {round(ans,1)}',info='You Are UnderWeight')
    elif(ans>=18.5 and ans<24.9):
        return render_template('home.html',data=f'Your BMI is {round(ans,1)}',info='You Are Normal Weigth')
    elif(ans>=25 and ans<29.9):
        return render_template('home.html',data=f'Your BMI is {round(ans,1)}',info='You Are Over Weight')
    elif(ans>30):
        return render_template('home.html',data=f'Your BMI is {round(ans,1)}',info='You Are Having Obesity')
    
if __name__=='__main__':
    app.run()
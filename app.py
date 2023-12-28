from flask import Flask, render_template
from cursor import cursor

app = Flask(__name__)

@app.route('/')
def index():
    print('in app.py')
    AT_data,RH_data,Rain_Hourly_data,Pressure_data,WD_10M_data,WS_10M_Hrly_data= cursor()

    return render_template('index.html', AT_data=AT_data, RH_data=RH_data, Rain_Hourly_data=Rain_Hourly_data,
                           Pressure_data=Pressure_data, WD_10M_data=WD_10M_data, WS_10M_Hrly_data=WS_10M_Hrly_data)

if __name__ == '__main__':
    app.run(debug=True)

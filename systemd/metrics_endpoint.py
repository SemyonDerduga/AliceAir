import sys
import co2meter
from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/metrics')
def hello_world():
    try:
        mon = co2meter.CO2monitor()
    except:
        sys.exit(1)
    date, co2, temperature = mon.read_data()
    prometeus_format = f'''# HELP co2_concentration Carbon dioxide concentration PPM
# TYPE co2_concentration gauge
co2_concentration {co2}
# HELP temperature Temperature at home
# TYPE temperature gauge
temperature {temperature}'''
    return Response(prometeus_format, mimetype='text')


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<name>')
def hello_name(name):
   dict = {'phy':50,'che':60,'maths':70}
   folderpath=r'\templates'


   return render_template('result.html', result = dict)
   #return render_template('hello.html', Name=name)

if __name__ == '__main__':
   app.run(debug = True)
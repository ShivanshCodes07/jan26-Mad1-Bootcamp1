from flask import Flask, render_template, request 
app = Flask(__name__)
@app.route('/')
def aboutmyself():
    name = request.args.get('name')
    email = request.args.get('email')
    hobby = request.args.get('hobby')

    return render_template('about.html', name=name, email=email, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)
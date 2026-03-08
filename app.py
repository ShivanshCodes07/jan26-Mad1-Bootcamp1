from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def aboutmyself():
    name = request.args.get('name')
    email = request.args.get('email')

    return render_template('about.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
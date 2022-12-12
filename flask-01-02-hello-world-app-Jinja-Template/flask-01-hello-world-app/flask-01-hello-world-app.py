from flask import Flask  # flask kütüphanesinden çekiyor

app = Flask(__name__)  # bu 3 komut -from, app, if- flaskın temel komutu

@app.route('/')    #decorator


def hello():
    return "Hello World from Flask!!!"

@app.route('/second')      #http://localhost:5000/second
def second():
    return 'Bize Her Yer Trabzon!!!!'


@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'   #http://localhost:5000/third/subthird

@app.route('/forth/<string:id>')  # numara girince bilgi çekiyor    localhost:5000/forth/sayı  yazınca çıkıyor
def forth(id):
    return f'Id number of this page is {id}'   # bilgi çekme http://localhost:5000/forth/123 123 yerine ne yazarsak o geliyor

if __name__ == '__main__':  
    app.run(debug=True) #localhost:5000 internete yazınca calıştı debug=True, port=2000 yazarsak 2000 portundan internete yazmamız lazım
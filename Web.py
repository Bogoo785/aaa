from flask import Flask
app=Flask(__name__) #_name_代表目前執行的模組

@app.route("/")
def home():
    return "Hello Flask2"
@app.route("/test")
def test():
    return"This is Test"
if __name__=="__main__" :
    app.run()#立刻啟動伺服器
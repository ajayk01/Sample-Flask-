from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/uploader" , methods = ['GET', 'POST'])
def upload_file():
   # try:
       if request.method == 'POST':
           f = request.files['file-f']
           b=request.form.get("card-type")
           user_id = 1;
           path = r"C:\\Users\\snpaj\\Desktop\\sample_flask\\image-temp\\"+str(user_id)+"\\"+b;
           app.config["IMAGE_UPLOADS"] = path
           b=b+"-front.jpg";
           f.save(os.path.join(app.config["IMAGE_UPLOADS"],secure_filename(b)))
           f = request.files['file-b']
           
           b1=b+"-back.jpg";
           f.save(os.path.join(app.config["IMAGE_UPLOADS"],secure_filename(b1)))
           # os.remove(b);
           return 'file uploaded successfully'+request.form.get("card-type")
   # except:
       # return "Upload the docs"
   
  


if __name__ == '__main__':
   app.run(debug = True)
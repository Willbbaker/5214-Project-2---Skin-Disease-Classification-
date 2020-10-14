# from flask import Flask, render_template
# app= Flask(__name__)

# @app.route('/')
# def index():
# 	return render_template("index.html")

# if __name__ == '__main__':
# 	app.run(debug=True)

from flask import Flask, request, render_template
app = Flask(__name__)

# from commons import get_tensor
# from inference import get_skin_disease

#just added:
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html', value='hi')

	if request.method == 'POST':
		print(request.files)

	# if 'file' not in request.files:
	# 	print('file not uploaded')
	# 	return
	# 	file = request.files['file']
	# 	image = file.read()
	# 	category, skin_disease = get_skin_disease(image_bytes=image)
	# 	#category, skin_disease = get_skin_disease(image_bytes=image)
	# 	get_skin_disease(image_bytes=image)
	# 	tensor = get_tensor(image_bytes=image)
	# 	print(get_tensor(image_bytes=image))
	# 	return render_template('result.html', disease=skin_disease)
	# 	#return render_template('result.html', disease=skin_disease, category=category)
 # 		#return render_template('result.html', disease=disease_name)
 #  		#return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
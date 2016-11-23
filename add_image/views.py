from django.http import HttpResponse
import os
import json
import cv2
import io
import transform_img as tf



def accept_req(request):
	#print '*** IN PRODUCTION ***'
	#return HttpResponse("<h1> *** ADD IMAGE IN PRODUCTION ***<h1>")

	try:
		if request.method == 'POST':
			
			header_req = request.headers.get('x-image-profile-id')
			print 'nvjnvnds'
			photo = request.files['photo']
			in_memory_file = io.BytesIO()
			photo.save(in_memory_file)
			data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
			color_image_flag = 1
			img = cv2.imdecode(data, color_image_flag)
			temp_path = '../data/add_image/' + str(header_req)+ '.jpg'
			cv2.imwrite(temp_path, img)
			print header_req
			#print temp_path
			add_response = tf.main_fun(temp_path, header_req)
			print add_response
			ret_val={'message':'image queued for adding.','status':2,'data':header_req }
			return 	jsonify(**ret_val)

	except:
		ret_val={'message':'request cannot be processed','status':0,'data':header_req }
		return 	jsonify(**ret_val)
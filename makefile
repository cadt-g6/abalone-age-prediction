img_name=samdyvin/abalone

build:
	docker build -t ${img_name} .

run:
	docker run -it -p 80:80 ${img_name}


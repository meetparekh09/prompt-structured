IMAGE_NAME := prompt-structured-app
CONTAINER_NAME := prompt-structured-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --network="host" \
		-v $(PWD):/app \
		--name $(CONTAINER_NAME) \
		-it --rm $(IMAGE_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) bash

clean:
	docker rmi -f $(IMAGE_NAME)


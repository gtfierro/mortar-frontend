CONTAINER_AUTH_TOKEN := $(shell hexdump -e '"%x"' -n 24 /dev/urandom)
CONTAINER_BASE_URL := "camp/$(CURPROJ)"

NOTEBOOK_FLAGS += --NotebookApp.allow_origin='*'
NOTEBOOK_FLAGS += --NotebookApp.allow_remote_access=True
JUPYTER_ENABLE_LAB=1

# "mortar": sha1:7e7bf58db7c6:90d0c0a56c8a3b48236238c13a6af7de7fc03ebb

DOCKER_RUN_FLAGS = \
	--rm \
	-p 8888:8888 \
	-v /var/run/docker.sock:/var/run/docker.sock \
	--shm-size 1000000000 \
	-e "GEN_CERT=yes" \
	-e "CONTAINER_AUTH_TOKEN=$(CONTAINER_AUTH_TOKEN)" \
	-e "CONTAINER_BASE_URL=$(CONTAINER_BASE_URL)" \
	-e "NOTEBOOK_FLAGS=$(NOTEBOOK_FLAGS)" \
	-e "JUPYTER_ENABLE_LAB=$(JUPYTER_ENABLE_LAB)" \
	
.PHONY: run
run:
	@echo "####################################################################################"
	@echo GO TO https://localhost:8888/?token=$(CONTAINER_AUTH_TOKEN)
	@echo "####################################################################################"
	@echo
	docker run -it --user=root $(DOCKER_RUN_FLAGS) pymortar

.PHONY: build
build:
	cp -r ../../analytics .
	docker build -t pymortar .

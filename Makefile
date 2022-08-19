IMAGE_BASE = airlabs-to-s3-transfer


.PHONY: help
help: ## Prints all targets in this Makefile, each with a help message
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  \
			awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Qustion: Not sure if I need to check tag, env, test, etc in my project?


###############################################################################
# Docker
###############################################################################

.PHONY: build-%
build-%: ## Builds specific image from multistage build in Dockerfile.
		docker image build --target=$* -t $(IMAGE_BASE):$* .


.PHONY: clean-%
clean-%: ## Cleans up all images.
		@-docker image remove $(IMAGE_BASE):$*


###############################################################################
# Test Local
###############################################################################

.PHONY: run-local-test
run-local-test: ## Run test image locally
		docker container run --rm $(IMAGE_BASE):test



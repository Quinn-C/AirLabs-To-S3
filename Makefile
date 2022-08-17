IMAGE_NAME = airlabs-to-s3-transfer

# Question1: to confirm whether should I register my container in ECR?
# If not, any ECR related stuff, I don't have to add them into my Makefile?

.PHONY: help
help: ## Prints all targets in this Makefile, each with a help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  \
			awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

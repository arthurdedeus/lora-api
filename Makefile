include deploy/.env

.PHONY: deploy
deploy:
	gcloud builds submit --config cloudmigrate.yaml
	gcloud run deploy lora-api --platform managed --image gcr.io/lora-api-349221/lora-api --region southamerica-east1

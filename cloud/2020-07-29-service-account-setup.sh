# Replace <PROJECT_ID> with the Project Id where you will be launching CloudyCluster
PROJECT="pearc-hack-1"

# Replace <SERVICE_ACCOUNT_NAME> with the name you want to use for the service account.
# Must be alphanumeric, between 6-30 characters long, and contain no capitol letters or spaces.
NAME="inst04service"

#############DO NOT CHANGE ANYTHING BELOW THIS COMMENT
SERVICE_ACCOUNT=$NAME@$PROJECT.iam.gserviceaccount.com

# Create the service account
gcloud iam service-accounts create $NAME --project=$PROJECT --display-name "CloudyCluster service account"

# Add the Datastore Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/datastore.user

# Add the Network Admin Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/compute.networkAdmin

# Add the Security Admin Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/compute.securityAdmin

# Add the Project IAM Admin Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/resourcemanager.projectIamAdmin

# Add the Service Account Admin Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/iam.serviceAccountAdmin

# Add the Service Account User Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/iam.serviceAccountUser

# Add the Compute Instance Admin Permissions
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/compute.instanceAdmin.v1

# Add Stackdriver Permission
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/logging.logWriter

# Add Storage Admin Permission
gcloud projects add-iam-policy-binding $PROJECT --member serviceAccount:$NAME@$PROJECT.iam.gserviceaccount.com --role roles/storage.admin

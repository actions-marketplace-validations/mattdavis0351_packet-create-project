import packet
import os

# Collect input variables from workflow
API_key = os.getenv("INPUT_API_KEY")
org_name = os.getenv("INPUT_ORG_NAME")
project_name = os.getenv("INPUT_PROJECT_NAME")


# Check if required inputs have been received
if API_key == "No key supplied":
    raise ValueError(
        f"Cannot supply empty API key. Current key is: %s" % API_key)

# Create Packet.com API client
manager = packet.Manager(auth_token=API_key)

# If org name is not default
org_id = ""
if org_name != "default":
    # list orgs for API key
    orgs = manager.list_organizations()
    # look for org with desired name
    for org in orgs:
        # if desired name is found set org_id to that orgs id
        if org.name == org_name:
            org_id = org.id
        else:
            # if desire name is not found raise exception letting user know
            raise ValueError(
                "Supplied organization name does not match orgs associated with the supplied API key")
    # Now that we have the org id create a new project in that org with desired name
    new_proj = manager.create_organization_project(
        org_id=org_id, name=project_name)
else:
    # If the user didn't supply an org, create new project with default org of API key
    new_proj = manager.create_project(project_name)
    print(f"Project %s created with id %s" % (new_proj.name, new_proj.id))

# Set outputs for action
print(f"::set-output name=project_id::{new_proj.id}")
print(f"::set-output name=project_name::{new_proj.name}")

# Profit

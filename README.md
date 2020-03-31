# GitHub Actions for creating projects on Packet.com

## Automate your infrastructure

This GitHub Action will create a new project on [packet.com](https://packet.com). Projects allow you to organize groups of resources and collaborators within your organization.

# Creating projects

With this action you can automate yoru workflow to provision projects using the [packet.com api](https://api.packet.net).

To use this action you will first need an [authentication token](https://www.packet.com/developers/api/authentication/) which can be generated through the [Packet Portal](https://app.packet.net/login?redirect=%2F%3F__woopraid%3DjUPDKi0tqtym).

**Packet.com is NOT a free service, so you will be asked to provide billing information. This action will NOT have access to that information.**

## Sample workflow that uses the packet-create-project action

```yaml
# File: .github/workflows/workflow.yml

on: [push]

name: Packet Project Sample

jobs:
  create-new-project:
    runs-on: ubuntu-latest
    name: Creating new packet project
    steps:
      - uses: mattdavis0351/packet-create-project@v1
        with:
          API_key: ${{ secrets.PACKET_API_KEY }}
          org_name: My Packet org # if not supplied will use default org for API key
          project_name: My-new-packet-project
```

## Available Inputs

| Input          | Description                                                                  | Default         | Required           |
| -------------- | ---------------------------------------------------------------------------- | --------------- | ------------------ |
| `API_key`      | Packet.com API authorization token                                           | No key supplied | :white_check_mark: |
| `org_name`     | Organization to place new project in, uses default user org if not specified | default         | :x:                |
| `project_name` | Desired name for new project                                                 | GitHub Actions  | :white_check_mark: |

## Outputs from action

This action supplies the following outputs which can be consumed by subsequent actions in the current job.

| Output         | Description                                            |
| -------------- | ------------------------------------------------------ |
| `project_id`   | ID of the newly created project returned as a string   |
| `project_name` | Name of the newly created project returned as a string |

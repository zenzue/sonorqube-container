# SonarScanner Docker Integration

This guide explains how to use the official SonarScanner Docker image to analyze your project with SonarQube.

## Prerequisites

- Docker installed on your machine
- Access to a SonarQube server

## Setup Instructions

### Pulling the Official SonarScanner Docker Image

Before running the scan, you need to pull the official SonarScanner Docker image from Docker Hub:

```bash
docker pull sonarsource/sonar-scanner-cli:latest
```

### Running SonarScanner

To scan your project, run the following command in your project's root directory:

```bash
docker run --rm \
  -e SONAR_HOST_URL="http://host:9000" \
  -e SONAR_LOGIN="KEY" \
  -v $(pwd):/usr/src \
  sonarsource/sonar-scanner-cli \
  -Dsonar.projectKey=Test \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://host \
  -Dsonar.login=key
```

This command includes:

- `--rm`: Removes the container after the scan completes, cleaning up any temporary files.
- `-e`: Specifies environment variables for the SonarQube server URL and authentication token.
- `-v $(pwd):/usr/src`: Mounts the current directory to `/usr/src` in the Docker container.
- `sonarsource/sonar-scanner-cli`: The Docker image to use.

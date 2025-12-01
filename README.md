# Python Docker Project

This project generates dummy data and exports it to a local folder using a Docker container.

## 🚀 How to Run

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/python-docker-project.git](https://github.com/your-username/python-docker-project.git)
    cd python-docker-project
    ```
2.  **Build the Docker Image:**
    ```bash
    docker build -t python-docker-project .
    ```
3.  **Create a Local Output Folder:**
    ```bash
    mkdir downloads
    ```
4.  **Run the Container (PowerShell Syntax):**
    * This command mounts your local `downloads` folder to the container's output folder (`/app/downloads`).
    ```powershell
    $local_downloads_path = (Get-Item -Path ".\downloads").FullName
    docker run --rm -v $local_downloads_path:/app/downloads python-docker-project
    ```
    (Note: You might use the more robust `wsl wslpath` conversion if they also run into the path issues we had.)

### 2. Share via Version Control

The best way to share is by putting your project on a site like **GitHub, GitLab, or Bitbucket**.

1.  **Initialize Git:**
    ```powershell
    git init
    ```
2.  **Add Files and Commit:**
    ```powershell
    git add .
    git commit -m "Initial commit of Python Docker project"
    ```
3.  **Push to a Remote Repository:**
    (You would set up a remote repository link and push the code here.)

---

## 🐳 Method 2: Sharing the Built Image via Docker Hub

If you want someone to run the project instantly without having to build it, you can upload the pre-built image to a **Docker Registry**. The most popular one is **Docker Hub**.

### Prerequisites:
* A Docker Hub account.
* The image built locally: `docker build -t python-docker-project .`

### Step 1: Tag the Image

Docker Hub requires your image to be tagged with your username and the repository name.

```powershell
# Replace 'your-username' with your actual Docker Hub ID
docker tag python-docker-project your-username/python-docker-project:latest
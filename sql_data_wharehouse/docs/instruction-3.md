# Instructions for Running PostgreSQL with a Docker Volume

This document explains how to run the PostgreSQL Docker container with a **volume mount**. This is the correct, professional way to share files from your local machine (the "host") with the PostgreSQL server running inside the container.

### Your Assignment

Your task is to construct the correct `docker run` command based on the template below, adapting it to your own settings, and then execute it in your terminal.

---

### Understanding the `docker run` Command

Here is a template for the `docker run` command. You will need to replace the placeholder values with your own.

```sh
docker run --name my-postgres-container -e POSTGRES_PASSWORD=123 -p 5432:5432 -v C:\Users\Nitro\SQL\sql_data_wharehouse\datasets:/data -d postgres
```

Let's break down each part of this command:

*   `docker run`: The basic command to start a new container.

*   `--name my-postgres-container`: (Optional, but recommended) Gives your container a memorable name. You can change `my-postgres-container` to whatever you like.

*   `-e POSTGRES_PASSWORD=your_password`: **(Important)** Sets the password for the `postgres` superuser. You **must** replace `your_password` with the same password you were using before to connect with DBeaver.

*   `-p 5432:5432`: **(Important)** Maps the port from the container to your host machine. This is what allows DBeaver to connect to the database. The format is `host_port:container_port`. `5432` is the standard PostgreSQL port. If you were using a different port before, you should use that here.

*   `-v C:\Users\Nitro\SQL\sql_data_wharehouse\datasets:/data`: **(This is the new, crucial part)** This is the volume mount. It maps a directory from your host machine to a directory inside the container.
    *   The part before the colon (`:`) is the **absolute path on your host machine**: `C:\Users\Nitro\SQL\sql_data_wharehouse\datasets`.
    *   The part after the colon (`:`) is the **absolute path inside the container**: `/data`. You can think of this as creating a "shared folder" named `data` inside the container that points to your local `datasets` folder.

*   `-d`: Runs the container in "detached" mode, meaning it runs in the background.

*   `postgres`: The name of the Docker image to use.

### What You Need to Do

1.  **Construct your command:** Copy the template above and replace `your_password` with your actual PostgreSQL password. You can also change the container name if you wish.
2.  **Run the command:** Open your terminal (like PowerShell or Command Prompt) and execute your complete `docker run` command.
3.  **Verify the container is running:** You can run the command `docker ps` to see a list of your running containers. You should see your new `my-postgres-container` in the list.
4.  **Connect with DBeaver:** Try to connect to your database with DBeaver, just as you did before. If the connection is successful, it means you have correctly started the container.

---

### Troubleshooting

**Error:** `docker: Error response from daemon: Conflict. The container name "/my-postgres-container" is already in use...`

**Reason:** This happens if you try to run the `docker run` command with a `--name` that is already being used by another container. This commonly occurs if a previous attempt to run the container succeeded in creating the container but failed for another reason (e.g., wrong password).

**Solution:** You must remove the old, conflicting container before creating a new one with the same name.

1.  **First, remove the old container:**
    ```sh
    docker rm -f my-postgres-container
    ```
    *(The `-f` flag forces the removal of a running container.)*

2.  **Then, run your correct `docker run` command again.**

---

Once you have successfully started the container with the volume mount and have connected to it with DBeaver, report back to me. We will then be ready to test our server-side `COPY` command.
# Configure Server Services

Complete [02 Build Azure Resources](02_build-azure-resources.md) before starting this page.

Use the **server VM** you created in the previous page.

## Step 2. Configure the server VM

Install and enable Nginx on the **server** VM.

```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
systemctl status nginx --no-pager
```

Create the page:

```bash
cat <<'EOF' | sudo tee /var/www/html/index.html >/dev/null
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Azure Segmented Service Deployment</title>
<style>
body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; line-height: 1.6; }
h1 { color: #1a4f8b; }
.box { padding: 16px; background: #f4f7fb; border-left: 4px solid #1a4f8b; }
</style>
</head>
<body>
<h1>Azure Segmented Service Deployment</h1>
<p>This site is the public-facing prototype for the practical exam.</p>
<div class="box">
<h2>What this demonstrates</h2>
<p>Port 80 is public. SSH and the internal service are restricted by NSG policy.</p>
</div>
</body>
</html>
EOF
```

Validate:

- `systemctl status nginx` shows `active`
- `curl http://localhost` returns your page

## **Screenshot 2: Nginx Running on the Server**

**Requirement:** Show the **server hostname** in the terminal prompt and `systemctl status nginx` with `Active: active (running)` visible.

## Step 3. Configure the internal-only service

Run a simple service on port 8080 on the **server** VM.

Recommended setup:

```bash
mkdir -p ~/internal-site
cat <<'EOF' > ~/internal-site/index.html
<h1>Internal-only service</h1>
<p>If you can read this from the client VM, the policy works.</p>
EOF
nohup python3 -m http.server 8080 --directory ~/internal-site > ~/http8080.log 2>&1 &
sleep 1
ss -ltnp | grep 8080
curl http://127.0.0.1:8080
```

What this does:

- `mkdir -p ~/internal-site` creates a folder to hold the internal-only webpage
- `cat <<'EOF' ... EOF` writes a simple `index.html` file into that folder
- `nohup python3 -m http.server 8080 --directory ~/internal-site ... &` starts a small Python web server on port `8080` in the background
- `sleep 1` gives the service a moment to start before you test it
- `ss -ltnp | grep 8080` confirms that something is listening on port `8080`
- `curl http://127.0.0.1:8080` tests the service locally from the server VM itself

Example output:

```text
steve@vm-steve-server:~$ mkdir -p ~/internal-site
cat <<'EOF' > ~/internal-site/index.html
<h1>Internal-only service</h1>
<p>If you can read this from the client VM, the policy works.</p>
EOF

nohup python3 -m http.server 8080 --directory ~/internal-site > ~/http8080.log 2>&1 &
sleep 1
ss -ltnp | grep 8080
curl http://127.0.0.1:8080
[1] 2794
LISTEN 0      5            0.0.0.0:8080      0.0.0.0:*    users:(("python3",pid=2794,fd=3))
<h1>Internal-only service</h1>
<p>If you can read this from the client VM, the policy works.</p>
steve@vm-steve-server:~$
```

Validate:

- `ss -ltnp | grep 8080` shows the listener
- `curl http://127.0.0.1:8080` works on the server

## **Screenshot 3: Internal-Only Service Running on Port 8080**

**Requirement:** In one screenshot, show the **server hostname**, the `ss -ltnp | grep 8080` listener output, and the local `curl http://127.0.0.1:8080` result.

---

[Prev](02_build-azure-resources.md) | [Home](README.md) | [Next](04_configure-server-subnet-nsg.md)

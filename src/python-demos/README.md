# FastAPI Server Setup

## Prerequisites
- Python 3.8 or higher

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

### HTTP (Development)
Start the FastAPI server with auto-reload:
```bash
uvicorn server:app --reload --port 1914
```

The server will be available at `http://127.0.0.1:1914`

### HTTPS (Production with SSL Certificate)
If you have SSL certificate files, run with HTTPS:
```bash
uvicorn server:app --reload --port 1914 \
  --ssl-keyfile=/path/to/privkey.pem \
  --ssl-certfile=/path/to/fullchain.pem
```

The server will be available at `https://127.0.0.1:1914`

**Certificate file locations:**
- Replace `/path/to/privkey.pem` with your private key file path
- Replace `/path/to/fullchain.pem` with your certificate file path

**Password-protected keys:**
If your private key is password-protected, use:
```bash
export SSL_KEY_PASSWORD="your_password"
uvicorn server:app --reload --port 1914 \
  --ssl-keyfile=/path/to/privkey.pem \
  --ssl-certfile=/path/to/fullchain.pem \
  --ssl-keyfile-password=$SSL_KEY_PASSWORD
```

⚠️ **Security Note**: Never pass passwords directly in command line arguments - use environment variables or remove the password from the key file.

### HTTPS (Development with Self-Signed Certificate)

**Option 1: Generate with OpenSSL**
```bash
openssl req -x509 -newkey rsa:4096 -nodes \
  -keyout key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost"
```

Then run:
```bash
uvicorn server:app --reload --port 1914 \
  --ssl-keyfile=key.pem \
  --ssl-certfile=cert.pem
```

**Option 2: Use mkcert (Recommended - No Browser Warnings)**

Install mkcert:
- **macOS**: `brew install mkcert`
- **Windows**: `choco install mkcert` (using Chocolatey) or download from [GitHub releases](https://github.com/FiloSottile/mkcert/releases)
- **Linux**: `brew install mkcert` or use package manager

Setup and generate certificate:
```bash
# Install local CA
mkcert -install

# Generate certificate for localhost
mkcert localhost 127.0.0.1
```

This creates `localhost+1.pem` (certificate) and `localhost+1-key.pem` (private key).

Run with:
```bash
uvicorn server:app --reload --port 1914 \
  --ssl-keyfile=localhost+1-key.pem \
  --ssl-certfile=localhost+1.pem
```

⚠️ **Note**: Self-signed certificates (Option 1) will show browser warnings. The `mkcert` approach (Option 2) creates locally-trusted certificates without warnings.

## API Endpoints

- `GET /model` - Returns a list of model IDs in JSON format
- `POST /category` - Creates a category with the provided name (accepts JSON body with "name" field)

## Testing

- HTTP: Visit `http://127.0.0.1:1914/docs` for interactive API documentation (Swagger UI)
- HTTPS: Visit `https://127.0.0.1:1914/docs` for interactive API documentation (Swagger UI)

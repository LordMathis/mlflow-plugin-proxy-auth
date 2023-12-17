# Mlflow Plugin Proxy Auth

Provides authentication to Mlflow server using [Proxy-Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Proxy-Authorization).

## Usage

Clone the repo and install the package into your virtual environment.

```
git clone https://github.com/LordMathis/mlflow-plugin-proxy-auth
pip install .
```

Set up mlflow environment variables

```env
MLFLOW_PROXY_USERNAME=username
MLFLOW_PROXY_PASSWORD=password
MLFLOW_TRACKING_AUTH="proxy_auth_provider"
```

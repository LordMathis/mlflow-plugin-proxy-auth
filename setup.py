from setuptools import find_packages, setup

setup(
    name="mlflow-plugin-proxy-auth",
    version="0.0.3",
    packages=find_packages(),
    install_requires=["mlflow"],
    entry_points={
        "mlflow.request_auth_provider": "dummy-backend=mlflow_plugin_proxy_auth.proxy_auth_header_provider:ProxyAuthProvider",
    },
)

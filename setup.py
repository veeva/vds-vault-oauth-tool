from setuptools import setup, find_packages

setup(
    name = "vds-vault-oauth-tool",
    version = "0.1",
    author = "Vault Developer Support",
    author_email = "kevin.nee@veeva.com",
    description = "A tool to check OAuth2 configurations.",
    install_requires = ["python-jose", "requests", "dotnet;platform_system=='Windows'"],
    include_package_data=True,
    license = "MIT",
    packages = find_packages(),
    entry_points = {"console_scripts": ["vds_vault_oauth_tool=vds_vault_oauth.main:main"]},
    classifiers=[
        "Topic :: Utilities",
        "License :: Apache License, Version 2.0",
    ],
)

# FTS-BFF-WEBADMIN

This is a project started as a POC for a renewed FreeTAKServer admin UI.

It strives to solve the following issues in FTS-UI atm:
- Tight coupling between python code and interfaces.
- Dockerization issues (state on disk) that will result in not possible to run on ECS / CloudRun
- No more WTForms
- Clearer definitions on needed variables

## Architectural overview
![Arch](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/ARCH.png?raw=true)
![Overview](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/OVERVIEW.png?raw=true)
![APIS](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/APIS.png?raw=true)

## Troubleshooting development

- M1 Issue installing cryptography
    -   Run:
        > export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib"
        > export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include"

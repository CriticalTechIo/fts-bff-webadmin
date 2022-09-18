# FTS-BFF-WEBADMIN

This is a project started as a POC for a renewed FreeTAKServer admin UI.

It strives to solve the following issues in FTS-UI atm:
- Tight coupling between python code and interfaces.
- Dockerization issues (state on disk) that will result in not possible to run on ECS / CloudRun
- No more WTForms
- Clearer definitions on needed variables
- Open api spec for the endpoints (with swagger)-> possibility for TS exporting
- Typing and importable API package.
- Settings management in Pydantic

## Architectural overview
|       |        |
|------------|-------------| 
| ![Arch](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/ARCH.png?raw=true) | ![Overview](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/OVERVIEW.png?raw=true) |
|![APIS](https://github.com/CriticalTechIo/fts-bff-webadmin/blob/main/docs/APIS.png?raw=true)|||


## Contributing
I will continue to work on this to evaluate FTS usability for my needs. The FTS community are free to take over development and maintenance if they see fit. If the state of the FTS-UI project evolves, I might scrap this project.

It is a public repo, create an issue. Create a branch and a PR, or fork the repo in its entirety if you want.
Questions in the discord for FTS

## Getting up and running locally
Not much to see atm, but here is how you start the application.
Take a look around in the codebase.

1. Clone it down
2. install poetry, pip install poetry
3. run ´poetry install´
4. run ´poetry run uvicorn service.main:app --reload´
5. In your browser navigate to http://127.0.0.1:8000/docs


## The big list of TODOs
- [X] Setup repo
- [X] Write introdury readme
- [X] Get started on implementation
- [ ] Setup docker
- [ ] Prepare for TDD
- [ ] Create user model and endpoints
- [ ] Create auth functionality
- [ ] Create proxy functionality
- [ ] Pylint & mypy
- [ ] Workflows and publish

## Troubleshooting development

- M1 Issue installing cryptography
    -   Run:
        > export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib"
        > export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include"

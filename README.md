## Pokedex
This application exposes REST endpoints and returns basic pokemon information.It internally calls third party api's to get the pokemon information.

### Packages
The application is built with Python 3.9 and uses FastAPI framework to implement rest endpoints.

Other major packages includes:
- pydantic
- pytest
- dependency-injector

### Prerequisites
Install the below requirements
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)


### Running the application
- Clone the repository to the working directory.

- Navigate to the project directory
     ```bash
     cd <project_directory>
     ```
- Build the docker image
    ```bash
    docker-compose build
    ```
- Run the docker-compose environment.
    ```bash
    docker-compose up
    ```
Once the application is started. Please open the url http://localhost:8000/docs
 for API information and execution.

### Tests
The application uses pytest as a test runner. Run the below command.
```bash
docker-compose run --rm app pytest -vv pokedex/tests --cov=pokedex
```
The output should be something like:
```bash
================================= test session starts ==========================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /code
plugins: Faker-11.1.0, cov-3.0.0, asyncio-0.16.0, anyio-3.4.0
collected 7 items                                                                                                                                                                      

pokedex/tests/unit/test_fun_translation.py::TestTranslations::test_is_legendary_return__200 PASSED                                                                               [ 14%]
pokedex/tests/unit/test_fun_translation.py::TestTranslations::test_habitat_cave_return__200 PASSED                                                                               [ 28%]
pokedex/tests/unit/test_fun_translation.py::TestTranslations::test_shakespeare_trans_return__200 PASSED                                                                          [ 42%]
pokedex/tests/unit/test_fun_translation.py::TestTranslations::test_translation_exception__200 PASSED                                                                             [ 57%]
pokedex/tests/unit/test_pokemon.py::TestPokemon::test_get_valid_response__200 PASSED                                                                                             [ 71%]
pokedex/tests/unit/test_pokemon.py::TestPokemon::test_pokemon_not_found__404 PASSED                                                                                              [ 85%]
pokedex/tests/unit/test_pokemon.py::TestPokemon::test_pokemon_without_en_flavour__200 PASSED                                                                                     [100%]

----------- coverage: platform linux, python 3.9.9-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
pokedex/__init__.py                                  0      0   100%
pokedex/api/__init__.py                              0      0   100%
pokedex/api/v1/__init__.py                           0      0   100%
pokedex/api/v1/endpoints/__init__.py                 0      0   100%
pokedex/api/v1/endpoints/pokemon.py                 16      0   100%
pokedex/api/v1/router.py                             4      0   100%
pokedex/application.py                              16      0   100%
pokedex/clients/__init__.py                          2      0   100%
pokedex/clients/funtranslations.py                  22     13    41%
pokedex/clients/models/__init__.py                   2      0   100%
pokedex/clients/models/pokemon_response.py          14      0   100%
pokedex/clients/models/translation_response.py      10      0   100%
pokedex/clients/pokemon.py                          19     11    42%
pokedex/containers.py                                9      0   100%
pokedex/core/__init__.py                             0      0   100%
pokedex/core/config.py                              22      2    91%
pokedex/error_handlers.py                           37      9    76%
pokedex/exceptions/__init__.py                       2      0   100%
pokedex/exceptions/common.py                         4      0   100%
pokedex/exceptions/pokemon.py                        7      0   100%
pokedex/models/__init__.py                           3      0   100%
pokedex/models/constants.py                          8      0   100%
pokedex/models/pokemon_summary.py                    8      0   100%
pokedex/models/responses.py                         17      2    88%
pokedex/services/__init__.py                         0      0   100%
pokedex/services/interfaces/__init__.py              0      0   100%
pokedex/services/interfaces/ipokemon.py              9      2    78%
pokedex/services/pokemon.py                         28      1    96%
pokedex/tests/__init__.py                            0      0   100%
pokedex/tests/unit/__init__.py                       0      0   100%
pokedex/tests/unit/conftest.py                       7      0   100%
pokedex/tests/unit/factories.py                     11      0   100%
pokedex/tests/unit/test_fun_translation.py          69      0   100%
pokedex/tests/unit/test_pokemon.py                  36      0   100%
--------------------------------------------------------------------
TOTAL                                              382     40    90%


```

#### Design considerations/Improvements for production

These improvements depends on the specific uses cases, in general we might need for good application. 

- Separate application settings for dev, test and prod. Create a base settings class and inherit for different envs.
  and create a settings instance based on env.
- Separate requirements for production and dev as dev have some extra packages for testing. This can be implemented having 
  different docker-compose files for test.
- Add log handlers and more log collection statements.
- Add caching to improve the latency and to avoid remote calls.
- Use Authentication and Authorization.
- Add circuit breaker to avoid exhausting the resources.
- Use secure vault to store the secure information. Ex: server passwords like(redis,db)
- API Monitoring
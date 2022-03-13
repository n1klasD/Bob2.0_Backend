# Bob2.0_Backend
Backend for Personal Digital Assistant Bob 2.0

## Structure

The backend is structured with a microservice architecture. Currently, each folder *controller*, *entertainment*, *finances*, *journey* and *welcome* 
contains the code for one USECASE and docker container and therefore has an own dockerfile. The general structure is seen below.

USECASE                                                                                                                                                            
│   └───Dockerfile                                                                                        
│                                                                                        
├───src                                                                                       
│    ├───  app.py                                                                                        
│    └───  requirements.txt                                                                                        
│                                                                                                                          
└───tests                                                                                        
     └───  test_sample.py                                                                                        
     
Currently, each usecase consists of a flask application, which is a microframework for writing RESTful Apis in Python. The folder *src* contains the source code of the application. The *app.py* file is the entrypoint for the flask application. The files in the folder *tests* are evaluated using pytest. Their filename should start with *test_*. 

## Unittests and Continous Integration

When code is pushed into a USECASE folder, all unittests in the tests folder are automatically run using github actions. When all tests pass, the docker container 
is automatically built and pushed to it´s respective docker hub repository. These repositories are public.


[![Controller test and build](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/controller_test_build.yml/badge.svg)](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/controller_test_build.yml)

[![Entertainment test and build](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/entertainment_test_build.yml/badge.svg)](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/entertainment_test_build.yml)

[![Finances test and build](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/finances_test_build%20copy.yml/badge.svg)](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/finances_test_build%20copy.yml)

[![Journey test and build](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/journey_test_build.yml/badge.svg)](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/journey_test_build.yml)

[![Welcome test and build](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/welcome_test_build.yml/badge.svg)](https://github.com/n1klasD/Bob2.0_Backend/actions/workflows/welcome_test_build.yml)

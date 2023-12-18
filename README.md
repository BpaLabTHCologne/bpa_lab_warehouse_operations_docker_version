# BPA Lab: Warehouse operations process application

## Description 
This repository contains the code of a process application that records the inventory of a high-bay warehouse and enables the storage and retrieval of items in a physical high-bay warehouse by a warehouse robot. 
The process application is available as a Docker container and consists of the following services:
* process-app: control of the process flow, checking of stock levels and recording of changes to stock levels
* robot-app: Physical control of the warehouse robot
* mysql-db: Database for the permanent storage of stock levels
* mqtt-broker: Message broker for communication between the process-app and robot-app services

## Associated BPMN process model
![image](https://github.com/BpaLabTHCologne/bpa_lab_warehouse_operations/assets/134142150/15652fdd-3fdb-4fe9-9b19-9d1be8ed87c4)

## Entry point for concepts and important components of Camunda 8 and Zeebe
* Documentation for the use and understanding of service tasks:
  * https://docs.camunda.io/docs/components/modeler/bpmn/service-tasks/
* Documentation to understand the job worker concept:
  * https://docs.camunda.io/docs/components/concepts/job-workers/

# Getting started

## Clone/Download the repository
Clone or download the code of this repository to your local machine. For cloning you need to install git: https://git-scm.com/downloads 

## Installation of Docker Desktop
To install Docker Desktop, follow this link: https://docs.docker.com/get-docker/ and select the version for your operating system. Then follow the installation instructions. Please note that your PC will restart once during or after the installation.

## Needed configurations

### Configuration of environment variables in own .env file.
The file **.env_example.txt** in the repository serves as an example for an .env-file. 

1. First after you cloned the code of the repository, you should create an .env-file (name of the file: ".env") is created
2. Copy the text from the **.env_example.txt** file into the newly created .env file
3. The first environment value **IS_CLOUD** must be **"true"** or **"false"** depending on whether you are using Camunda 8 Cloud or Self-managed
4. The second environment value **IS_PROD** must again be **"true"** or **"false"**
   * Set the value to **false** if you want to run/test the process application without having access to the physical robot
   * Set the value to **true** if you want to run the process application with the movements of the physical robot **(only when you have access to the robot and the correct setup)**

## Execution of the process application
**Before execution, it is important that all installations and configurations have been done completely and successfully**

1. Start the prompt and change to the path of the folder in which you saved/cloned the repository
2. Then start the docker container by using the following command: `docker compose up --build` and wait till all services are started
3. Run an instance of the warehouse operations process defined by **warehouse-operations-process.bpmn** in Camunda:
     * When you click on "run" the process, the following variables **must be passed** in JSON format:
     * **item** defines the name of the object for which the action will be executed
     * **place_id** defines the place in a shelf for which the action should be executed
     * **shelf_id** defines the shelf for which the action is to be executed
     * **task** is the action that should be executed
     * **transactionId** is a unique number needed for the message events that controlling between both pools/processes
     
* Example: Storing an item on the third place: `{"item":"Bicycle","place_id":3,"shelf_id":1,"task":"store","transactionId":0}`
 
* Example: Retrieving an item from the third place: `{"item":"Bicycle","place_id":3,"shelf_id":1,"task":"retrieve","transactionId":0}`

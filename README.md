# BPA Lab: Warehouse operations process application

## Description 
Dieses Repository enthält den Code einer Prozessapplikation, die bestand eines Hochregallagers erfasst und das Ein- und Auslagern von Gegenständen in einem physischen Hochregallager durch einen Lagerroboter ermöglicht. 
Das Prozessapplikation steht als Docker Container zur Verfügung und besteht aus folgenden Services:
* process-app: Steuerung des Prozessflusses, Überprüfung des Lagerbestandes und Erfassung der Veränderungen des Lagerbestandes
* robot-app: Physische Steuerung des Lagerroboters
* mysql-db: Datenbank, zur permanenten Speicherung der Lagerbestände
* mqtt-broker: Nachrichtenbroker für die Kommunikation zwischen dem process-app und robot-app Services

## Associated BPMN process model
![image](https://github.com/BpaLabTHCologne/bpa_lab_warehouse_operations/assets/134142150/15652fdd-3fdb-4fe9-9b19-9d1be8ed87c4)

## Entry point for concepts and important components of Camunda 8 and Zeebe
* Documentation for the use and understanding of service tasks:
  * https://docs.camunda.io/docs/components/modeler/bpmn/service-tasks/
* Documentation to understand the job worker concept:
  * https://docs.camunda.io/docs/components/concepts/job-workers/

# 

## Download of the repository


## Required installations

### Installation of Docker Desktop
To install Docker Desktop, follow this link: https://docs.docker.com/get-docker/ and select the version for your operating system. Then follow the installation instructions. Please note that your PC will restart once during or after the installation.


## Needed configurations

### Configuration of environment variables in own .env file.
The file **.env_example.txt** serves as an example for an .env file. 

1. First after the project on the own hard disk was cloned, an .env file (name of the file: ".env") is created
2. Copy the text from the **.env.example** file into the newly created .env file
3. In the following it is explained how to get the values of the required environment variables:

### Obtaining the values for the required environment variables
1. Log in to the Camunda Cloud and click on **Cluster**
2. Click on **API** and then on **Create new client**
3. Enter a name in the format **FIRSTNAME_LASTNAME_CREDENTIALS** and click on **Create credentials**
4. When the credentials are created, go to the **Env vars** tab
5. Here should be represented all environment variables you need in your .env file, except **MYSQL_USER**, **MYSQL_PASSWORD** and **IS_CLOUD**
6. For **MYSQL_USER** and **MYSQL_PASSWORD** you should enter the corresponding user and password already created in **Configuration of MySQL database**
7. **IS_CLOUD** must be "true" or "false" depending on whether you are using Camunda 8 Cloud or Self-managed.

## Execution of the process application

### Pre-conditions in BPALab-Setup
* The **router for the local network** must be started 
* The **TXT controller from the warehouse robot** must be started
* The **Raspberry Pi, which serves as MQTT broker**, must be started

### Parameters to be passed for execution 
* If the process is to be started, the following variables must be passed in JSON format:
* **item** defines the name of the object for which the action will be executed
* **place_id** defines the place in a shelf for which the action should be executed
* **shelf_id** defines the shelf for which the action is to be executed
* **task** is the action that should be executed
* **transactionId** is a unique number needed for the message events that control the process between both pools or processes

* Example of placing an item in storage: `{"item":"Bicycle","place_id":3,"shelf_id":1,"task":"store","transactionId":0}` 
* Example of retrieving an item: `{"item":"Bicycle","place_id":3,"shelf_id":1,"task":"retrieve","transactionId":0}` 

### Execution
1. Establish a connection to **eduroam** and the **local network**
2. Start an instance of the process **warehouse-operations-process.bpmn** in Camunda
4. Start the programs **highbay_robot_app.py** for robot control and **warehouse_operations_process_app.py** for process control 

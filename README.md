# opisense_client
Python package providing some functions to interact with the Opisense API. 
More info about Opisense at www.opisense.com

## Getting started
These instructions will guide you through the process of getting you ready to use the opisense_client package

### Prerequisites
#### 1. Get an Opisense account.
Contact info@opinum.com or see www.opinum.com to get an account

#### 2. Get Opisense API credentials.
Contact support@opinum.com to get an API secret and API key

#### 3. Install opisense_client package
You can install opisense_client by typing `pip install opisense-client` in your terminal.

### Objects and Methods description
Every object and method is described with docstrings. You can easily access it by running `help(method)`


## Changelog
### 1.0.0 : 
#### First stable version
#### StandardData
Added variableId as unique identifier option

#### Documentation
Updated README.MD and documented every object and method

### 0.3 :
#### force_path 
Added force_path optional parameter to http.POST and http.PUT. 
Overwrites the default OpisenseObject.api_path in the http call.

#### json_output
Added json_output optional parameter to http.GET
If True, Returns the JSON object from the http response if available.

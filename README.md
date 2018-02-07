# Form validation task
> Simple HTML page and backend for saving data from form to the database.
Form should have 3 fields (Name(required), Email(required),Phone(not required).
Validation rules:
Name should have from 2 till 50 characters.
Email should accept only valid email addresses.
Phone should have from 5 till 13 digits.



![](header.png)

## Required installation to run locally

 * Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
 * Install [VirtualBox Oracle VM VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
 * Install [Vagrant](https://www.vagrantup.com/downloads.html)
 * Install Vagrant plugins:
 ```sh
 * vagrant plugin install vagrant-json-config
```

## How to run locally

* `git clone` this repository:
```bash
# Clone with HTTPS
$ git clone https://github.com/curious725/django_form_validation_task.git
# or Clone with SSH
$ git clone git@github.com:curious725/django_form_validation_task.git
```  

* Use these commands:
```bash
 $ cd /django_form_validation_task
 $ cp sample.secrets.json secrets.json
```
Put your values in secrets.json file. 
And finally run:

 ```bash
 $ vagrant up dev
  ```
  
 ```
 * Navigate to [http://localhost:8000/](http://localhost:8888/) to access server.
 

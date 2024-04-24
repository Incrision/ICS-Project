## Reference material

- https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-4-i2c-temperature-sensor

## PostgreSQL JDBC Driver 
Download and copy the postgres JDBC Driver jar file into the nifi container inside the root directory folder

[PostgreSQL Driver Download](https://jdbc.postgresql.org/download/postgresql-42.4.0.jar)

## Import nifi template
pull down template object from nifi task bar and select imported template name

## Configure parameter context
Add the following parameters
| Name | Value |
| ---- | ----- | 
| db_driver_class | org.postgresql.Driver |
| db_driver_file  | postgresql-42.4.0.jar |
| db_host         | postgres |
| db_name         | csec_db
| db_port         | 5432
| db_user         | csec
| db_user_pass    | csec
| drivers_directory | /		


## Nifi flow configuration
under general 
- set process group name 
- set *Process Group Parameter Context* to recently created parameter context
- apply

under *controller services*, click on settings for Postgres controller service
| Name | Value |
| ---- | ----- | 
| Database Connect URL | jdbc:postgresql://#{db_host}:#{db_port}/#{db_name} |
| Database Driver Class Name | #{db_driver_class} |
| Database Driver Location(s) | #{drivers_directory}#{db_driver_file} |
| Database User | #{db_user} |
| Database Password | #{db_user_pass}
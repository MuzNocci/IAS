# IAS (Internet Administration System)


# BANCO DE DADOS
_________________________________________________________________

### TABELA :: USERS
| id (PK)               | integer           | id()              |
| password              | varchar(128)      | string()          |
| last_login            | timestamp()       | timestamps()      |
| is_superuser          | tinyint(0)        | boolean()         |
| username (UNIQUE)     | varchar(150)      | string()          |
| first_name            | varchar(150)      | string()          |
| last_name             | varchar(150)      | string()          |
| email                 | varchar(254)      | string()          |
| is_staff              | tinyint(1)        | boolean()         |
| is_active             | tinyint(1)        | boolean()         |
| date_joined           | timestamp()       | timestamps()      |


### TABELA :: USERSDATA

| nome do campo         | type bd           | type migration    |
|-----------------------|-------------------|-------------------|
| id                    | integer           | id()              |
| email                 | varchar(255)      | string()          |
| email_marketing       | tinyint(1)        | boolean()         |
| email_verified_at     | timestamp()       | string()          |
| photo                 | varchar(255)      | string()          |
| register              | varchar(14)       | string()          |
| phone                 | varchar(15)       | string()          |
| sex                   | varchar(45)       | string()          |
| zipcode               | varchar(255)      | string()          |
| address               | varchar(255)      | string()          |
| number_address        | interger(5)       | integer()         |
| address_component     | varchar(255)      | string()          |
| district              | varchar(255)      | string()          |
| city                  | varchar(45)       | string()          |
| state                 | varchar(45)       | string()          |
| country               | varchar(255)      | string()          |
| level                 | integer(2)        | integer()         |
| business              | integer(11)       | integer()         |
| plan                  | integer(2)        | integer()         |
| plan_expire           | timestamp()       | timestamps()      |
| remember_token        | varchar(100)      | string()          |
| updated_at            | timestamp()       | timestamps()      |


### TABELA :: BUSINESS

| nome do campo         | type bd           | type migration    |
|-----------------------|-------------------|-------------------|
| id                    | bigint(20)        | id()              |
| name                  | varchar(255)      | string()          |
| surname               | varchar(255)      | string()          |
| logo                  | varchar(255)      | string()          |
| logo_sm               | varchar(255)      | string()          |
| register              | varchar(18)       | string()          |
| email                 | varchar(255)      | string()          |
| phone                 | varchar(255)      | string()          |
| observation           | longtext()        | longText()        |
| zipcode               | varchar(255)      | string()          |
| address               | varchar(255)      | string()          |
| number_address        | interger(5)       | integer()         |
| address_component     | varchar(255)      | string()          |
| district              | varchar(255)      | string()          |
| city                  | varchar(45)       | string()          |
| state                 | varchar(45)       | string()          |
| country               | varchar(255)      | string()          |
| created_at            | timestamp()       | timestamps()      |
| updated_at            | timestamp()       | timestamps()      |
| active                | tinyint(1)        | boolean()         |


### TABELA :: CLIENTS

| nome do campo         | type bd           | type migration    |
|-----------------------|-------------------|-------------------|
| id                    | bigint(20)        | id()              |
| name                  | varchar(255)      | string()          |
| register              | varchar(14)       | string()          |
| surname               | varchar(255)      | string()          |
| registration          | varchar(18)       | string()          |
| sector                | varchar(45)       | string()          |
| jobposition           | varchar(45)       | string()          |
| photo                 | varchar(255)      | string()          |
| email                 | varchar(255)      | string()          |
| email_marketing       | tinyint(1)        | boolean()         |
| phone                 | varchar(255)      | string()          |
| whatsapp              | tinyint(1)        | boolean()         |
| sex                   | varchar(45)       | string()          |
| birthday              | timestamp()       | timestamps()      |
| observation           | longtext()        | longText()        |
| zipcode               | varchar(255)      | string()          |
| address               | varchar(255)      | string()          |
| number_address        | interger(5)       | integer()         |
| address_component     | varchar(255)      | string()          |
| district              | varchar(255)      | string()          |
| city                  | varchar(45)       | string()          |
| state                 | varchar(45)       | string()          |
| country               | varchar(255)      | string()          |
| icms_exempt           | tinyint(1)        | boolean()         |
| simple_tax            | tinyint(1)        | boolean()         |
| created_at            | timestamp()       | timestamps()      |
| updated_at            | timestamp()       | timestamps()      |
| active                | tinyint(1)        | boolean()         |


- plans
- categories
- suppliers
- products
- clients
- orders
- cashers
- notifications
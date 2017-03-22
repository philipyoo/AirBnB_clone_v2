# AirBnB Clone

**Purpose**

The purpose of this project is to recreate the AirBnB site, from the back-end data management to the front-end user interface. 

The project is currently in its first phase, where we are creating a command line interpretor to access objects that will store user data. Users can use the console to create objects, update object attributes, remove objects, list all objects, and store and read data from a .json file.

----------------------------------------

**Authors**
- **Philip Yoo**, \<philip.yoo@holbertonschool.com>, @philipYoo10
- **Jianqin Wang**, \<jianqin.wang@holbertonschool.com>, @jianqinwang94

----------------------------------------

In order to begin the console, you can run either 'python3 console.py' or './console.py' in the command line.

Classes that are currently supported include BaseModel, User, City, State, Amenity, Review, and Place.

The console currently supports the following commands:
- **create \<class name>**, which will create an object of the class declared by user;
- **show \<class name> \<id>**, which will display the object information if it exists;
- **destroy \<class name> \<id>**, which will delete the object if it exists;
- **all \<class name>**, where the class name input is optional and the console will display all instances, or all instances of a specified object;
- **update \<class name> \<id> \<attribute name> \<attribute value>**, whilch will update an instance attribute of a previously declared object.

Additionally, the console also supports the following command formats:
- **\<class name>.all()**, which will display all instances of the specified class;
- **\<class name>.count()**, whilch will display the number of instances of the specified class;
- **\<class name>.show(\<id>)**, whilch will display the instance with correct id and class;
- **\<class name>.destroy(\<id>)**, which will delete the instance with correct id and class;
- **\<class name>.update(\<id>, \<attribute name>, \<attribute value>)**, which will update an instance of the given class and id with the new attribute;
- **\<class name>.update(\<id>, \<dictionary representation>)**, which will update an instance of the given class and id with a dictionary of key value pairs that will be new attributes for the objects. 

----------------------------------------

** List of useful commands: **

- `$ HBNB_TYPE_STORAGE="" python3 -m unittest discover tests 2>&1`
- `$ HBNB_MYSQL_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1`
- `$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p` && `$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db` && `$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p`
- `$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`
- `$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

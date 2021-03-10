## @file mongoinitializer.sh
# @author İsmail Ata İnan
# @brief Contains the bash shell commands necessary for the Mongo database authentication and
# initialization. The application gets ready after initializing the database by these commands when
# the containers are up.

docker exec -it websearcher_mongodb_1 bash
mongo -u atabase -p
atabase
use flaskdb
db.createUser({user: 'atabase', pwd: 'atabase', roles: [{role: 'readWrite', db: 'flaskdb'}]})
db.grantRolesToUser('atabase',[{ role: "dbAdmin", db: "flaskdb" }])
exit
exit

docker exec -it websearcher_mongodb_1 bash
mongo -u atabase -p
atabase
use flaskdb
db.createUser({user: 'atabase', pwd: 'atabase', roles: [{role: 'readWrite', db: 'flaskdb'}]})
db.grantRolesToUser('atabase',[{ role: "dbAdmin", db: "flaskdb" }])
exit
exit

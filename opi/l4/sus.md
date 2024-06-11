# connect 

ssh s371364@helios.se.ifmo.ru -p 2222


# install
wget https://github.com/wildfly/wildfly/releases/download/29.0.1.Final/wildfly-29.0.1.Final.zip
unzip wildfly-29.0.1.Final.zip
~/wildfly-29.0.1.Final/bin/add-user.sh
Выбираем Management User
Юзернейм, пароль - любые
Группа - пустая 
scp -P 2222  s371364@helios.se.ifmo.ru:~/wildfly-29.0.1.Final/bin/client/jboss-cli-client.jar ./jboss-cli-client.jar 

# run
export _JAVA_OPTIONS="-XX:MaxHeapSize=1G -XX:MaxMetaspaceSize=256m"
~/wildfly-29.0.1.Final/bin/standalone.sh -Djboss.http.port=1234

# deploy
scp -P 2222 ./l3/build/libs/l3.war s371364@helios.se.ifmo.ru:~/wildfly-29.0.1.Final/standalone/deployments/l3.war


# console

jconsole -J-Djava.class.path=jboss-cli-client.jar

# to kill:
top 
kill -9

# helios 

ssh -L localhost:1234:127.0.0.1:1234 s371364@se.ifmo.ru -p 2222 -N
ssh -L localhost:9990:127.0.0.1:9990 s371364@se.ifmo.ru -p 2222 -N


service:jmx:remote+http://localhost:9990

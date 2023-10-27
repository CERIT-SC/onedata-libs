#!/bin/bash
java -jar ../swagger-codegen-cli.jar generate -i "https://onedata.org/api/21.02.3/onezone/swagger.json" -l python -o "onezone_client" -c "onezone.conf" -v
java -jar ../swagger-codegen-cli.jar generate -i "https://onedata.org/api/21.02.3/oneprovider/swagger.json" -l python -o "oneprovider_client" -c "oneprovider.conf" -v
java -jar ../swagger-codegen-cli.jar generate -i "https://onedata.org/api/21.02.3/onepanel/swagger.json" -l python -o "onepanel_client" -c "onepanel.conf" -v

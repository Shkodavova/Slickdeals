

apppath= "C:\\Users\\Vladimir\\Desktop\\app-debug.apk"
platformName='Android'

################# FIRST DEVICE ###############################

desiredCapabilitiesAppiumFirstddevice={ "deviceName": "KYV7N15B14001804",
                                        "platformName": platformName,
                                        "app": apppath}

urlFirstAppiumDockerServer='http://127.0.0.1:4723/wd/hub'#http://172.28.49.81:4723/wd/hub'


################# SECOND DEVICE ###############################


desiredCapabilitiesAppiumSeconddevice={ "deviceName": "Z33201905000095",
                                        "platformName": platformName,
                                        "app": apppath}


urlSecondAppiumDockerServer='http://127.0.0.1:4724/wd/hub'#http://172.28.49.81:4724/wd/hub'
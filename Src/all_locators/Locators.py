class Locator(object):
    # **************************************Login Page**************************************
    textbox_Email_xpath = "//input[@id='mat-input-0']"  # xpath
    textbox_Password_xpath = "//input[@id='mat-input-1']"  # xpath
    button_ToggleVisibility = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                              "4]/button "  # xpath
    button_SignI_xpath = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"
    alert_LogInAuthenticationError = "//body[1]/kc-toastr[1]/div[1]/div[1]"
    user_profile_Icon_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/kc-toolbar-user/div"
    button_Logout_xpath = "//span[normalize-space()='LOGOUT']"

    Email_box = "//input[@id='mat-input-0']"  # xpath
    Email_box_test = "//input[@id='mat-inpu-0']"  # xpath
    Password_box = "//input[@id='mat-input-1']"  # xpath
    Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                               "4]/button "  # xpath
    Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

    LogIn_Authentication_Error = "//body[1]/kc-toastr[1]/div[1]/div[1]"

    # ************************************************** Dashboard page************************************
    Dashboard_button = "//span[contains(text(),'Dashboard')]"
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH
    Dashboard_title = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1"

    # ************************************************ header frame **************************************************
    CreateNew_H = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/button[2]"  # XPATH
    CreateNew_H_test = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/buttn[2]"
    Namespace_H = "button[role='menuitem']"  # xpath
    NewApplication_H = "//span[contains(text(),'New Application')]"

    # ******************************Create Application page********************************

    SpringBoot = "//span[contains(text(),'Spring Boot')]"
    SpringBoot_Version_box = "//mat-select[@id='mat-select-1']"
    SpringBoot_Version_2_1_11 = "//span[contains(text(),'2.1.11')]"  # XPATH
    Java_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]"
    Java_Version_11 = "//span[contains(text(),'11')]"
    Java_Version_8 = "//span[contains(text(),'8')]"

    JavaScript = "//span[contains(text(),'JavaScript')]"
    ExpressJS = "//mat-tab-body/div[1]/div[1]/div[2]"
    Express_Js_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # Xpath
    ExpressJs_Version_4_17_1 = "//span[contains(text(),'4.17.1')]"

    Django = "//span[contains(text(),'Django')]"
    Python_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # XPATH
    Python_version_3_7_8 = "//span[contains(text(),'3.7.8')]"  # XPATH
    Python_version_3_6_11 = "//span[contains(text(),'3.6.11')]"  # XPATH
    Django_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Django_Version_2_2_14 = "//span[contains(text(),'2.2.14')]"  # XPATH

    DotNet = "//mat-tab-body/div[1]/div[1]/div[4]"
    DoNet_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]"
    DontNet_V_3_0 = "//span[contains(text(),'3.0')]"
    DotNet_V_2_2 = "//span[contains(text(),'2.2')]"
    DotNet_V_2_1 = "//span[contains(text(),'2.1')]"

    Laravel = "//span[contains(text(),'Laravel')]"
    Laravel_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Laravel_version_6_0 = "//span[contains(text(),'6.0')]"
    Laravel_version_5_8 = "//span[contains(text(),'5.8')]"
    Laravel_version_5_7 = "//span[contains(text(),'5.7')]"
    Laravel_version_5_6 = "//span[contains(text(),'5.6')]"

    # Golang
    Golang = "//mat-tab-body/div[1]/div[1]/div[6]"
    Goecho_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"
    Goecho_V_4_1_14 = "//span[contains(text(),'4.1.14')]"

    ApplicationName_box = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    TeamBox_A = "//*[@id='mat-select-2']"
    Team_Default = "//mat-option[@id='mat-option-1']"
    # Team_None = "//span[contains(text(),'None')]"
    Team_None = "//span[@class='mat-option-text'][normalize-space()='None']"
    Next_button = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/div[3]/button[2]"

    Choose_Namespace_one = "//mat-tab-body/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/div[1]"
    Save_button_A = "//span[contains(text(),'Save')]"
    Create_Application = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/form/div[3]/button[2]"
    check_create_app = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]"
    check_app_status = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[5]/div[2]/div[1]/div[1]/p[2]"

    Overview_button = "//span[contains(text(),'Overview')]"
    PipelineConfig_button = "//span[contains(text(),'Pipeline Config')]"
    Resources_Config_button = "//span[contains(text(),'Resources Config')]"
    External_Endpoints_button = "//span[contains(text(),'External Endpoints')]"
    Environment_Variables_button = "//span[contains(text(),'Environment Variables')]"
    Secrets_button = "//span[contains(text(),'Secrets')]"
    Monitoring_button = "//span[contains(text(),'Monitoring')]"
    Logs_button = "//span[contains(text(),'Logs')]"

    wait_ToCreateApplication = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[3]/ul[1]/li[1]/div[1]/button[1]/span[1]/mat-icon[1]/*[name()='svg'][1]"

    # ******************** For application create validation ***************************

    New_Git_Commit_Pushed_msg = "//body/div[2]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"
    Application_build_finished_successfully_msg = "//span[contains(text(),'Application build finished successfully!')]"

    # Repository already exists with 'test-laravel = "//span[contains(text(),"Repository already exists with 'test-laravel' name")]"
    Live_Pipeline_Logs = "//h5[contains(text(),'Live Pipeline Logs')]"

    # ****************************************From sidebar***********************************
    Applications = "//span[contains(text(),'Applications')]"
    find_Application_tolist = "//span[contains(text(),'101')]"

    # *******************************To deploy application*************************************
    # Deployment is now in pending. It will take a moment to start = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    # Now we are deploying your application. Please wait for a while. It may take upto 3 minutes = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    # Application Deployed! = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"
    # To_deploy = "//li[@id='6367295d806b560001d2dd50']//*[name()='svg']//*[name()='rect']"  # XPATH
    To_deploy = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    Deploy_button = "//span[normalize-space()='Deploy']"
    Okay_button = "//span[contains(text(),'Okay')]"
    Deployment_Pending_msg = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    deployment_failed = "//span[contains(text(),'[Alert] Application deployment failed!')]"
    close = "// span[contains(text(), 'close')]"
    Deployment_Pending_time_msg = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    Application_Deployed = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"

    to_check_deploy = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    Deployed_success_status = "//p[contains(text(),'Success')]"
    Deployed_status = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-ci-cd-pipeline/div[5]/div[2]/div[1]/div/p[2]"

    deployed_validation = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[3]/ul[1]/li[1]/div[1]/button[1]/span[1]/mat-icon[1]/*[name()='svg'][1]"

    # ********************************************** delete Application ********************************
    application_Settings = "(//span[contains(@class,'inline-block py-4 px-4')][normalize-space()='Settings'])[1]"
    application_Delete = "//span[contains(text(),'Delete')]"
    Application_namebox_D = "//input[@placeholder='Type here...']"
    Delete_permanently_button = "//span[contains(text(),'I understand this, Delete permanently')]"
    Application_Deleted_Success_msg = "//p[normalize-space()='Application Deleted Successfully']"
    DeleteApp_byIcon = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/kc-application-init[1]/div[1]/button[1]"

    #  for failed app
    Application_Initialization_failed = "//h5[contains(text(),'*** Application Initialization Failed ***')]"

    # *************************************** database ********************************
    # go to Database page

    Database_button = "//div[@class='cdk-overlay-container']//button[4]"
    wait_forfilter = "//span[contains(text(),'Select Database')]"
    MySQL_button = "//mat-tab-body//button[1]"

    Postgresql = "//h3[contains(text(),'Postgresql')]"
    Postgresql_Version_12_3_0 = "//span[contains(text(),'12.3.0')]"
    Web_Client_Email = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[5]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    Web_Client_Password = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[5]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/input[1]"

    Mongodb = "//h3[contains(text(),'Mongodb')]"
    teamBox_database = "(//div[@class='mat-select-arrow-wrapper'])[1]"
    defaultTeam_database = "//span[contains(text(),'default')]"
    firstTeam = "/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option[3]/span[1]"

    namespace_first = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div/form/div[3]/button[1]"
    database_ServerName = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    initial_AdminPassword = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/div[2]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    confirm_Password = "//*[@id='mat-input-2']"
    selectVersion_box = "//*[@id='mat-select-0']/div/div[2]"
    version_8_0_19 = "//span[contains(text(),'8.0.19')]"

    next_button = "//span[normalize-space()='Next']"
    enableWebClient = "//label[@for='mat-checkbox-2-input']//div[@class='mat-checkbox-inner-container']"
    confirm_button = "//button[@type='submit']"

    Database_CreatedMsg = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    # created validation by snapshot button
    WaitTo_Create = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"
    # waitTo_create = "//h3[contains(text(),'Allocated Resources Per Instance')]"
    # validation
    Event_log = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-details[1]/kc-page-layout[1]/kc-page-layout-content[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/span[1]"
    Database_FinalStatus = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-details/kc-page-layout/kc-page-layout-content/div/kc-database-initialization/div/div[2]/div[2]/pre[10]"
    Cancel_msg = "//body/kc-toastr[1]/div[1]/div[1]/button[1]/i[1]"

    # *********************************** delete database **********************************

    database_list = "(//span[@class='item-label'][normalize-space()='Database'])[1]"
    database_name = "//span[normalize-space()='test-sql-221']"
    database_Settings = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    database_Delete = "//span[normalize-space()='Delete']"
    database_nameBox = "(//input[@placeholder='Type here...'])[1]"
    deletePermanently = "//span[@class='ng-star-inserted']"

    # ************************************ create cache *********************************************
    cacheButton = "(//span[@class='ng-tns-c6-2'][normalize-space()='Cache'])[1]"
    redis_button = "//span[contains(text(),'5.0.7,6.0.5')]"
    teamBox_c = "//div[@class='mat-select-value']"
    Namespace_c = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/form[1]/div[3]/button[1]"
    serverNameBox_c = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    adminPassword_c = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/input[1]"
    confirmPassword_c = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]/input[1]"
    selectVersion_c = "(//div[@class='mat-select-value'])[1]"

    Cache_Version_5_0_7 = "//span[@class='mat-option-text'][normalize-space()='5.0.7']"
    Cache_Version_6_0_5 = "//span[contains(text(),'6.0.5')]"
    Web_Client_Email_cache = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[7]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    Web_Client_Password_cache = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[7]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/input[1]"
    next_Button_c = "(//span[normalize-space()='Next'])[1]"
    confirmButton_c = "(//span[@class='ml-auto mr-auto text-center ng-tns-c42-31'])[1]"
    enable_WebClient = "(//div[@class='mat-checkbox-inner-container'])[2]"

    DefaultTeam_cache = "//span[contains(text(),'default')]"
    Cache_createdMsg = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    Access_Terminal = "// a[contains(text(), 'Access Terminal')]"

    # ******************************** Delete Cache *****************************************

    Cache_S = "(//span[@class='item-label'][normalize-space()='Cache'])[1]"
    Cache_Settings = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    Cache_Delete = "//span[contains(text(),'Delete')]"
    Cache_namebox_D = "//input[@placeholder='Type here...']"
    # Delete_permanently_button = "//span[contains(text(),'I understand this, Delete permanently')]"
    Cache_Deleted_Success_msg = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    Enable_Web_Client_P3_X_Redis = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[6]/div[1]/div[1]/mat-checkbox[1]/label[1]/div[1]"

    # ******************************** namespace creation *************************
    Namespace_button = "//body/div[3]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]"  # XPATH

    NamespaceName_box = "input[placeholder='Namespace Name']"  # css selector
    # CPU_box = "//input[@class='ng-tns-c41-54 ng-pristine ng-valid ng-touched']"  # XPATH
    CPU_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[""1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[""1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[""1]"

    NamespaceButton = "button[role='menuitem']"
    Create_button_N = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]"
    NamespaceName_bar = "input[placeholder='Namespace Name']"
    wait_toCreateNamespace = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[1]/span/div"
    check_crateMessage = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    # with organization

    Organization = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]/span[1]/div[1]"
    Organization_searchBar = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]"
    Choose_Default = "//span[contains(text(),'default')]"
    Choose_firstOrganization = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"

    CPU_bar = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Memory_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Volume_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Bandwidth_box = "//div[contains(text(),'Moderate')]"

    Team = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]/div[1]"
    teamSearch_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]"
    Choose_TeamDefault = "//span[contains(text(),'default')]"
    Choose_firstTeam = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"

    # Namespace delete
    NamespaceButton_sidebar = "//span[normalize-space()='Namespace']"
    Namespace_settings = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    deleteButton_namespace = "(//button[@class='kc-delete-primary w-32 mat-button mat-button-base ng-trigger ng-trigger-fadeInRight'])[1]"
    input_namespaceName = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-delete-dialog[1]/div[1]/div[1]/div[1]/div[1]/input[1]"

    # Team_None = "//span[@class='mat-option-text'][normalize-space()='None']"

class Locator(object):
    # Login Page
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

    # Dashboard page
    Dashboard_button = "//span[contains(text(),'Dashboard')]"
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH
    Dashboard_title = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1"

    # header frame
    CreateNew_H = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/button[2]"  # XPATH
    CreateNew_H_test = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/buttn[2]"
    Namespace_H = "button[role='menuitem']"  # xpath
    NewApplication_H = "//span[contains(text(),'New Application')]"

    # Create Application page

    SpringBoot = "//span[contains(text(),'Spring Boot')]"
    SpringBoot_Version_box = "//mat-select[@id='mat-select-1']"
    SpringBoot_Version_2_1_11 = "//span[contains(text(),'2.1.11')]"  # XPATH
    Java_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]"
    Java_Version_11 = "//span[contains(text(),'11')]"
    Java_Version_8 = "//span[contains(text(),'8')]"

    JavaScript = "//span[contains(text(),'JavaScript')]"
    ExpressJS = "//mat-tab-body/div[1]/div[1]/div[2]"
    Express_Js_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # Xpath
    JS_V_4_17_1 = "//span[contains(text(),'4.17.1')]"

    Django = "//span[contains(text(),'Django')]"
    Python_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # XPATH
    Python_version_3_7_8 = "//span[contains(text(),'3.7.8')]"  # XPATH
    Python_version_3_6_11 = "//span[contains(text(),'3.6.11')]"  # XPATH
    Django_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Django_Version_2_2_14 = "//span[contains(text(),'2.2.14')]"  # XPATH

    DotNet = "//mat-tab-body/div[1]/div[1]/div[4]"
    DoNet_v_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]"
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
    GoLang = "//mat-tab-body/div[1]/div[1]/div[6]"
    Goecho_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"
    Goecho_V_4_1_14 = "//span[contains(text(),'4.1.14')]"

    ApplicationName_box = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    TeamBox_A = "//*[@id='mat-select-2']"
    Team_Default = "//mat-option[@id='mat-option-1']"
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

    # For create validation
    # Http failure response for https://api.eks.rakibefs'
    # message: Http failure response for https://api.eks.rakibefstestmaincluster782.klovercloud.io/api/application/create: 0 Unknown Error
    # Http_failure_response = "//span[contains(text(),'Http failure response for https://api.eks.rakibefs')]"

    New_Git_Commit_Pushed_msg = "//body/div[2]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"
    Application_build_finished_successfully_msg = "//span[contains(text(),'Application build finished successfully!')]"

    # Repository already exists with 'test-laravel = "//span[contains(text(),"Repository already exists with 'test-laravel' name")]"
    Live_Pipeline_Logs = "//h5[contains(text(),'Live Pipeline Logs')]"

    # To deploy application
    # Deployment is now in pending. It will take a moment to start = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    # Now we are deploying your application. Please wait for a while. It may take upto 3 minutes = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    # Application Deployed! = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"

    # From sidebar
    Applications = "//span[contains(text(),'Applications')]"
    find_Application_tolist = "//span[contains(text(),'101')]"

    # To_deploy = "//li[@id='6367295d806b560001d2dd50']//*[name()='svg']//*[name()='rect']"  # XPATH
    To_deploy = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    Deploy_button = "//span[normalize-space()='Deploy']"
    Okay_button = "//span[contains(text(),'Okay')]"
    Deployment_Pending_msg = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    deployment_failed = "//span[contains(text(),'[Alert] Application deployment failed!')]"
    close = "// span[contains(text(), 'close')]"
    Deployment_Pending_time_msg = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    Application_Deployed = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"

    to_check_deploy = "//*[@id='6384410f571f50000103b892']"
    Deployed_success_status = "//p[contains(text(),'Success')]"
    Deployed_status = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-ci-cd-pipeline/div[5]/div[2]/div[1]/div/p[2]"

    # To delete Application
    application_Settings = "(//span[contains(@class,'inline-block py-4 px-4')][normalize-space()='Settings'])[1]"
    # scroll
    application_Delete = "//span[contains(text(),'Delete')]"
    Application_namebox_D = "//input[@placeholder='Type here...']"
    Delete_permanently_button = "//span[contains(text(),'I understand this, Delete permanently')]"
    Application_Deleted_Success_msg = "//p[normalize-space()='Application Deleted Successfully']"

    # to namespace creation
    Namespace_button = "//body/div[3]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]"  # XPATH

    NamespaceName_box = "input[placeholder='Namespace Name']"  # css selector
    # CPU_box = "//input[@class='ng-tns-c41-54 ng-pristine ng-valid ng-touched']"  # XPATH
    CPU_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[""1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[""1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[""1]"


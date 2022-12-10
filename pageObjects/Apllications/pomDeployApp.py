from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class DeployApplications(object):
    def __init__(self, driver):
        self.driver = driver

        self.Applications = (By.XPATH, Locator.Applications)
        self.To_deploy = (By.XPATH, Locator.To_deploy)
        self.Deploy_button = (By.XPATH, Locator.Deploy_button)
        self.Okay_button = (By.XPATH, Locator.Okay_button)
        self.Deployment_Pending_msg = (By.XPATH, Locator.Deployment_Pending_msg)

        self.deployment_failed = (By.XPATH, Locator.deployment_failed)
        self.Deployment_Pending_time_msg = (By.XPATH, Locator.Deployment_Pending_time_msg)
        self.Application_Deployed = (By.XPATH, Locator.Application_Deployed)

        self.deployed_validation = (By.XPATH, Locator.deployed_validation)
        self.to_check_deploy = (By.XPATH, Locator.to_check_deploy)
        self.Deployed_status = (By.XPATH, Locator.Deployed_status)

    def getApplications(self):
        return self.Applications

    def getTo_deploy(self):
        return self.To_deploy

    def getDeploy_button(self):
        return self.Deploy_button

    def getOkay_button(self):
        return self.Okay_button

    def getDeployment_Pending_msg(self):
        return self.Deployment_Pending_msg

    def getdeployment_failed(self):
        return self.deployment_failed

    def getDeployment_Pending_time_msg(self):
        return self.Deployment_Pending_time_msg

    def getApplication_Deployed(self):
        return self.Application_Deployed

    def getdeployed_validation(self):
        return self.deployed_validation

    def getto_check_deploy(self):
        return self.to_check_deploy

    def getDeployed_status(self):
        return self.Deployed_status

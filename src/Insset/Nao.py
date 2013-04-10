#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "mirage"
__date__ = "$10 avr. 2013 09:22:56$"

from naoqi import ALProxy

class Remote:
    def __init__(self, robotIp):
        """Class de Commande"""
        self.robotIp = robotIp
        self.motionProxy = 0
        self.robotPostureProxy = 0
        self.behaviorManagerProxy = 0
        self.textToSpeechProxy = 0
        self.vitesse = 0.4

        print "Robotip : " + robotIp + "\n"

        err = False
        
        if(err == False):
            try:
                self.motionProxy = ALProxy("ALMotion", self.robotIp, 9559)
            except Exception, e:
                self.motionProxy = 0
                print "Could not create proxy to ALMotion"
                print "Error was: ", e

        if(err == False):
            try:
                self.robotPostureProxy = ALProxy("ALRobotPosture", self.robotIp, 9559)
            except Exception, e:
                self.robotPostureProxy = 0
                print "Could not create proxy to ALRobotPosture"
                print "Error was: ", e

        if(err == False):

            try:
                self.behaviorManagerProxy = ALProxy("ALBehaviorManager", self.robotIp, 9559)
            except Exception, e:
                self.behaviorManagerProxy = 0
                print "Could not create proxy to ALRobotPosture"
                print "Error was: ", e

        if(err == False):
            try:
                self.textToSpeechProxy = ALProxy("ALTextToSpeech", self.robotIp, 9559)
            except Exception, e:
                self.textToSpeechProxy = 0
                print "Could not create proxy to ALTextToSpeech"
                print "Error was: ", e

        if(err == True):
            print "Err: 001 : Erreur de Chargement des Proxy"
            
    def MoteurOn(self, part="Body"):
        # Head
        # LArm
        # RArm
        # LLeg
        # RLeg
        # Body
        if self.motionProxy != 0:
            pStiffnessLists = 1.0
            pTimeLists = 1.0
            self.motionProxy.stiffnessInterpolation(part, pStiffnessLists, pTimeLists)
        
    def MoteurOff(self, part="Body"):
        # Head
        # LArm
        # RArm
        # LLeg
        # RLeg
        # Body
        if self.motionProxy != 0:
            pStiffnessLists = 0.0
            pTimeLists = 1.0
            self.motionProxy.stiffnessInterpolation(part, pStiffnessLists, pTimeLists)

    def setPosture(self, posture, post=False):
        if posture == "sit":
            self.Posture_Sit(post)
        elif posture == "crouch":
            self.Posture_Crouch(post)
        elif posture == "lyingback":
            self.Posture_LyingBack(post)
        elif posture == "lyingbelly":
            self.Posture_LyingBelly(post)
        elif posture == "sitrelax":
            self.Posture_SitRelax(post)
        elif posture == "standinit":
            self.Posture_StandInit(post)
        elif posture == "standzero":
            
        elif posture == "stand":
            self.Posture_Stand(post)
        else:
            print "Err: 002 : Erreur posture inconnu"
            
    def getPosture(self):
        return "Null"

    def Posture_Sit(self, post=False):
        if self.robotPostureProxy != 0:
            self.MoteurOn();
            if post == True:
                self.robotPostureProxy.post.goToPosture("Sit", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("Sit", self.vitesse)
                self.MoteurOff();
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Posture_Crouch(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post) #Security
            if post == True:
                self.robotPostureProxy.post.goToPosture("Crouch", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("Crouch", self.vitesse)
                self.MoteurOff();
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Posture_LyingBack(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post) #Security
            if post == True:
                self.robotPostureProxy.post.goToPosture("LyingBack", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("LyingBack", self.vitesse)
                self.MoteurOff();
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Posture_LyingBelly(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post) #Security
            if post == True:
                self.robotPostureProxy.post.goToPosture("LyingBelly", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("LyingBelly", self.vitesse)
                self.MoteurOff();
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Posture_Stand(self, post=False):
        if self.robotPostureProxy != 0:
            self.MoteurOn();
            if post == True:
                self.robotPostureProxy.post.goToPosture("Stand", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("Stand", self.vitesse)
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"
    
    def Posture_SitRelax(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post) #Security
            if post == True:
                self.robotPostureProxy.post.goToPosture("SitRelax", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("SitRelax", self.vitesse)
                self.MoteurOff();
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Posture_StandInit(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post)
            if post == True:
                self.robotPostureProxy.post.goToPosture("StandInit", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("StandInit", self.vitesse)
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"
            
    def Posture_StandZero(self, post=False):
        if self.robotPostureProxy != 0:
            self.Posture_Stand(post)
            if post == True:
                self.robotPostureProxy.post.goToPosture("StandZero", self.vitesse)
            else:
                self.robotPostureProxy.goToPosture("StandZero", self.vitesse)
        else:
            print "Err: 003 : Erreur de Chargement des Proxy lors de l utilisation"

    def Say(self,text):
        sefl.textToSpeechProxy.say(text)

class Information:
    def __init__(self, robotIp):
        """Class d information"""
        self.robotIp = robotIp
        self.motionProxy = 0
        self.robotPostureProxy = 0
        self.behaviorManagerProxy = 0
        
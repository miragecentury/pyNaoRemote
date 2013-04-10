#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "mirage"
__date__ = "$10 avr. 2013 09:01:28$"

from Insset import Nao

if __name__ == "__main__":
    robotIp = "saintquentinnao.local"
    remote = Nao.Remote(robotIp)

    if len(sys.argv) <= 1:
        print "-h pour avoir l'aide"
    else:
        if len(sys.argv) <= 2:
            
            if sys.argv[2] == "-h":
                print "L'aide ne vous aidera pas."
            else:
                if cmd == "say":
                    remote.Say(text)
                elif cmd == "sit":
                    remote.setPosture("sit", False)
                elif cmd == "stand":
                    remote.setPosture("stand", False)
                elif cmd == "crouch":
                    remote.setPosture("crouch", False)
                elif cmd == "lyingbelly":
                    remote.setPosture("crouch", False)
                elif cmd == "forward":
                    print "notimplement"
                elif cmd == "backward":
                    print "notimplement"
                elif cmd == "stop":
                    print "notimplement"
                elif cmd == "right":
                    print "notimplement"
                elif cmd == "left":
                    print "notimplement"
                elif cmd == "rotateleft":
                    print "notimplement"
                elif cmd == "rotateright":
                    print "notimplement"
                elif cmd == "runbehavior":
                    print "notimplement"
                elif cmd == "stopbehavior":
                    print "notimplement"
                else:
                    print "none"
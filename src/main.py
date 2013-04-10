#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "mirage"
__date__ = "$10 avr. 2013 09:01:28$"

import sys

from Insset import Nao

def cmd(argv,pt):
    print pt

if __name__ == "__main__":
    robotIp = "nao.local"
    remote = Nao.Remote(robotIp)

    if len(sys.argv) <= 1 :
        print "-h pour avoir l'aide"
    else:
        if len(sys.argv) >= 1:
            
            if sys.argv[1] == "-h":
                print "L'aide ne vous aidera pas."
            elif sys.argv[1] == "-c" and len(sys.argv) >= 2:
                cmd = sys.argv[2]
                if cmd == "say":
                    if len(sys.argv) >= 3:
                        remote.Say(sys.argv[3])
                    else:
                        print sys.argv[3]
                elif cmd == "sit":
                    remote.setPosture("sit", False)
                elif cmd == "stand":
                    remote.setPosture("stand", False)
                elif cmd == "crouch":
                    remote.setPosture("crouch", False)
                elif cmd == "lyingbelly":
                    remote.setPosture("lyingbelly", False)
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
            else:
                print sys.argv[1]
        else:
            print len(sys.argv)
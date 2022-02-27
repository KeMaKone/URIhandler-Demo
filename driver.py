from urivalidator import URIhandler


def tests():
    testinputs = ["vima-identity://login?source=severa", "visma-identity://link?source=severa", "visma-identity://login?sauce=severa", "visma-identity://sign?source=vismasign&documentid=47ed9186-24ba0-4e8b-b9e2-7123575fdd5b", "visma-identity://login?source=severa", "visma-identity://confirm?source=netvisor&paymentnumber=102226",
                  "visma-identity://sign?source=vismasign&documentid=47ed9186-2ba0-4e8b-b9e2-7123575fdd5b"]
    for testinput in testinputs:
        try:
            urihandler = URIhandler(testinput)
            action = urihandler.getAction()
            params = urihandler.getParams()
            #source = urihandler.getValue("source")
            print(f"Action: {action}.")
            for key in params.keys():
                print(f"Parameter: {key}, Value: {params[key][0]}")
            #print(f"Source: {source}")
        except ValueError as e:
            print(e)
        finally:
            print("\n")
    return


def main():
    while(True):
        userinput = input("Insert URI, empty stops: ")
        if userinput == "":
            break
        try:
            urihandler = URIhandler(userinput)
            action = urihandler.getAction()
            params = urihandler.getParams()
            source = urihandler.getValue("source")
            print(f"Action: {action}.")
            for key in params.keys():
                print(f"Parameter: {key}, Value: {params[key][0]}")
            print(f"Source: {source}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    tests()
    main()

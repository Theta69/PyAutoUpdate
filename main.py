def getVersion():
    return 1.0
def PrintVer():
    print(f"This is the {getVersion()} version!")
    input()
if __name__ == "__main__":
    from updater import checkUpdates
    resp = checkUpdates()
    if resp == True:print("Update installed.\nPress any key to exit.");input()
    else:print("No new updates available.\nPress any key to exit.");input()
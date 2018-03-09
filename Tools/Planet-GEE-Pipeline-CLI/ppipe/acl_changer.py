import ee
import subprocess

##initialize earth engine


##request type of asset, asset path and email to give permission
def access(mode,asset,user):
    ee.Initialize()
    if mode=='folder':
        try:
            for line in subprocess.check_output("earthengine ls"+" "+asset).split('\n'):
                asst=line
                print(asst)
                asset_acl=subprocess.check_output("earthengine acl ch "+asst+" -u"+" "+user)
                print(ee.data.getAssetAcl(asst))
        except Exception:
            print("Permissions Changed")
    elif mode=='collection':
        try:
            asset_acl=subprocess.check_output("earthengine acl ch "+asset+" "+" -u"+" "+user)
            print(ee.data.getAssetAcl(asset))
            print("Permissions Changed")
        except Exception:
            print("Permissions Error Check Again")
    elif mode=='image':
        try:
            asset_acl=subprocess.check_output("earthengine acl ch "+asset+" "+" -u"+" "+user)
            print(ee.data.getAssetAcl(asset))
            print("Permissions Changed")
        except Exception:
            print("Permissions Error Check Again")

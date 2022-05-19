import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(folder_from, 'rb')
        dbx.folder_upload(f.read(),folder_to)

def main():
    access_token = 'sl.BH6LEOM8Z0gGnAcvxsSYR26pG7TX7bYT9zXy5-HuUuDwknECCzO-R3dwtSVGBepSxfXr9Ut87behlskdt7l6ltz0gVuZ-X5cu9Ytsna9rTM1ze4tcV14zPo_T24w2-9zGm0GD-w'
    TransferData = TransferData(access_token)
    folder_from = input("Enter the folder path to transfer :- ")
    folder_to = input("Enter the full path to upload to dropbox :- ")
    TransferData.upload_folder(folder_from,folder_to)
    print("Folder has been moved")
import vk

class SearchClass(Controller):

    api = vk.Session()
    def searchGroup(self, naem):
        
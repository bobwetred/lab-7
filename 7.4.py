class ChildElement:

    def __init__(self, *args):
        self.name = args[0]

    def printDetails(self):
        print("\t", end="")
        print(self.name)


class CompositeElement:

    def __init__(self, *args):
        self.name = args[0]
        self.children = []

    def appendChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def printDetails(self):
        print(self.name)
        for child in self.children:
            print("\t", end="")
            child.printDetails()


def main():
    host = CompositeElement("Host.folder")
    folder1 = CompositeElement("1.folder")
    folder2 = CompositeElement("2.folder")
    folder3 = CompositeElement("3.folder")
    folder4 = CompositeElement("4.folder")
    file1 = CompositeElement("1.xlsx")
    folder11 = ChildElement("11.folder")
    file12 = ChildElement("12.txt")
    file21 = ChildElement("21.exe")
    file22 = ChildElement("22.dtb")
    file31 = ChildElement("31.mp3")
    file32 = ChildElement("32.cfg")
    file41 = ChildElement("41.php")
    folder1.appendChild(folder11)
    folder1.appendChild(file12)
    folder2.appendChild(file21)
    folder2.appendChild(file22)
    folder3.appendChild(file31)
    folder3.appendChild(file32)
    folder4.appendChild(file41)
    host.appendChild(folder1)
    host.appendChild(folder2)
    host.appendChild(folder3)
    host.appendChild(folder4)
    host.appendChild(file1)
    host.printDetails()
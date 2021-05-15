
# Main Window Class
class MainWindow:
    """Main Window

                Summary:
                    A class for the Main window that includes:

                    - Position
                    - Size
                    - Title

                Attributes:
                    title, top, left, width, height

                Methods:
                    None

                Attributes
                ----------
                    title : str
                    top : int
                    left : int
                    width : int
                    height : int


                Methods
                -------
                    None

            """
    def __init__(self):
        """Constructor:
           Initialize Main Window object

                            Parameters:
                                self
                            Returns:
                                None
                        """
        self.title = "Glass Carbide"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
